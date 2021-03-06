from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
import xmltodict
import http.client
import uuid
import os
import shutil
import json
import copy
import paramiko
import uuid
import subprocess
import time
import os


class cyclus_run:
    def __init__(self, master, input_path, output_path, get_metadata=False):
        self.screen_width = master.winfo_screenwidth()
        self.screen_height = master.winfo_screenheight()
        self.input_path = input_path
        self.output_path = output_path
        self.get_metadata = get_metadata

        # open new window
        self.master = Toplevel(master)
        self.master.title('Running Cyclus')
        self.master.geometry('+0+%s' %int(self.screen_height/4))
        # configure page
        columnspan = 5
        Label(self.master, text='Cyclus Run configuration').grid(row=0, columnspan=columnspan)
        Label(self.master, text='========================').grid(row=1, columnspan=columnspan)
        
        local_run = Button(self.master, text='Run Locally', command=lambda:self.run_locally())
        local_run.grid(row=2, column=0)
        Label(self.master, text='Cyclus command/path:').grid(row=2, column=1)
        self.cyclus_cmd = Entry(self.master)
        self.cyclus_cmd.insert(END, 'cyclus')
        self.cyclus_cmd.grid(row=2, column=2)


        Label(self.master, text='========================').grid(row=3, columnspan=columnspan)
        

        cloud_run = Button(self.master, text='Run on Cloud', command=lambda:self.run_on_cloud())
        cloud_run.grid(row=4, column=0)
        Label(self.master, text='server:').grid(row=4, column=1)
        self.server = Entry(self.master)
        self.server.insert(END, 'azure')
        self.server.grid(row=4, column=2)


        Label(self.master, text='username:').grid(row=5, column=0)
        self.username = Entry(self.master)
        self.username.grid(row=5, column=1)
        Label(self.master, text='password:').grid(row=5, column=2)
        self.password = Entry(self.master)
        self.password.grid(row=5, column=3)


        Label(self.master, text='Proxy Hostname:').grid(row=6, column=0)
        self.proxy_hostname = Entry(self.master)
        self.proxy_hostname.grid(row=6, column=1)
        Label(self.master, text='Proxy Port:').grid(row=6, column=2)
        self.proxy_port = Entry(self.master)
        self.proxy_port.grid(row=6, column=3)
        
        
        frame = Frame(self.master)
        frame.grid(row=7, columnspan=columnspan)

        s = Scrollbar(frame)
        s.pack(side=RIGHT, fill=Y)
        self.output_pipe = Text(frame, wrap='word')
        s.config(command=self.output_pipe.yview)
        self.output_pipe.pack(side=LEFT, fill=Y)
        self.output_pipe.config(yscrollcommand=s.set)
        guide = """This is where you run Cyclus with the generated input file!
You have the choice to run locally or run on the cloud (Azure VM). If you do not
have Cyclus installed in your local drive, you'd have to run on the cloud. 

Locally: define the Cyclus command/path for the run (default `cyclus')

Cloud: if you're connected to an open network, leave the proxy hostname/port blank. However, if you are in a secured network (like in a national lab) and might need to tunnel your ssh, list the proxy hostname and port in the blanks. For ORNL, the hostname is `snowman.ornl.gov' and port is `3128'."""

        self.output_pipe.insert(END, guide+'\n\n')


    def run_locally(self):
        # check if output exists, and if it does, change its name to temp_whatever
        self.check_existing_output()
        # run cyclus 
        self.output_pipe.insert(END, '\nAttempting to run Cyclus locally:')
        cyclus_cmd = self.cyclus_cmd.get()

        if self.get_metadata:
            metapath = os.path.join(os.path.dirname(self.output_path), 'new_m.json')
            command = '%s -m > %s' %(cyclus_cmd, metapath)
            self.output_pipe.insert(END, '\nTrying to get Cyclus metadata:')
            self.output_pipe.insert(END, '\nRunning command:')
            self.output_pipe.insert(END, '\n'+command)
            proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
            out, err = proc.communicate()
            with open(metapath, 'r') as f:
                meta = f.read()
            if meta == '':
                self.output_pipe.insert(END, 'This failed! Refer to the error message below:')
                self.output_pipe.insert(END, '\n\n' + err.decode('utf-8') + '\n\n')
            else:
                messagebox.showinfo('Done', 'Successfully read metadata file!')
                self.master.destroy()

        else:
            command = '%s %s -o %s' %(cyclus_cmd, self.input_path, self.output_path)
            self.output_pipe.insert(END, '\nRunning command:')
            self.output_pipe.insert(END, '\n'+command)
            proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
            out, err = proc.communicate()
            self.output_pipe.insert(END, '\n\n'+out.decode('utf-8'))
            if 'success' in out.decode('utf-8'):
                self.output_pipe.insert(END, '\n\nGreat! move on to the backend analysis!')

    def check_existing_output(self):
        self.output_pipe.insert(END, '\nChecking if output `cyclus.sqlite` already exists...')
        if os.path.isfile(self.output_path):
            i = 1
            self.outdir = os.path.dirname(self.output_path)
            while os.path.isfile(os.path.join(self.outdir, 'temp_%s.sqlite' %str(i))):
                i += 1
            self.output_pipe.insert(END, '\n`cyclus.sqlite` already exists! Changing the previous filename to temp_%s.sqlite\n' %str(i))
            shutil.move(self.output_path, os.path.join(self.outdir, 'temp_%s.sqlite' %str(i)))

    def run_on_cloud(self):
        # microsoft azure account
        if self.server.get() == 'azure':
            ip = '40.121.41.236'
        else:
            ip = self.server.get()
        username = self.username.get()
        password = self.password.get()
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.output_pipe.insert(END, '\nAttempting to connect to Azure VM:')
        proxy_hostname = self.proxy_hostname.get()
        proxy_port = self.proxy_port.get()
        try:
            self.err_message = """Did not connect! Check Internet connection or contact baej@ornl.gov

If using the Azure server, the Azure VM might not be turned on. If so, ask baej@ornl.gov to turn it on.

If you are using this in a secure network, that might be the reason as well.
Try using a tunneling application (ex. Corkscrew) to use a proxy, by defining the `hostname' and `port' blocks.
https://wiki.archlinux.org/index.php/HTTP_tunneling

Error message:\n"""
            if proxy_hostname != '':
                self.output_pipe.insert(END, '\n' + 'with Proxy hostname=%s and port=%s' %(proxy_hostname, proxy_port))
                
                http_con  = http.client.HTTPConnection(proxy_hostname, proxy_port)
                # this should be changed?
                headers = {}

                http_con.set_tunnel(ip, 22, headers)
                http_con.connect()
                sock = http_con.sock
                self.ssh.connect(ip, username=username,
                                 password=password, sock=sock,
                                 allow_agent=False, look_for_keys=False)

            else:
                self.ssh.connect(ip, username=username,
                                 password=password,
                                 allow_agent=False, look_for_keys=False)
            self.output_pipe.insert(END, '\n\n CONNECTED. Now uploading generated input file, running the file on the VM, and downloading the file:\n\n')
            self.err_message = """Did connect, but Cyclus Run was unsuccessful. 

Check the error message.
"""
            if not self.get_metadata:
                self.upload_run_download(self.input_path, self.output_path)
            else:
                self.remote_metadata(self.output_path)
            self.return_code = 0

        except Exception as e:
            self.output_pipe.insert(END, '\n\n' + self.err_message + str(e))
            self.return_code = -1



    def run_and_print(self, command, p=False):
        if p:
            self.output_pipe.insert(END, 'Running command:\n%s\n' %command)
            self.output_pipe.insert(END, '============================\n')
        i, o, e = self.ssh.exec_command(command)
        output = '\n'.join(o.readlines())
        error = '\n'.join(e.readlines())
        if len(error) != 0:
            if p:
                self.output_pipe.insert(END, 'Error:\n')
                self.output_pipe.insert(END, error)
                self.output_pipe.insert(END, '\n\n')
            return error
        if p:
            self.output_pipe.insert(END, 'Output:\n')
            self.output_pipe.insert(END,output)
            self.output_pipe.insert(END, '\n')
            self.output_pipe.insert(END, '============================\n')
            self.output_pipe.insert(END, 'Finish\n')
        return 0


    def remote_metadata(self, output_path):
        i, o, e = self.ssh.exec_command('cyclus -m')
        output = '\n'.join(o.readlines())
        error = '\n'.join(e.readlines())
        if len(error) != 0:
            self.output_pipe.insert(END, 'Metadata reading failed:\n')
            self.output_pipe.insert(END, error)
            self.output_pipe.insert(END, '\n\n')
            return error
        else:
            # if it succeeded
            with open(os.path.join(os.path.dirname(output_path, 'new_m.json')), 'w') as f:
                f.write(output)
            messagebox.showinfo('Done', 'Successfully read metadata file!')
            self.master.destroy()


    def upload_run_download(self, input_path, output_path):
        ftp = self.ssh.open_sftp()
        # upload yo

        rnd_dir = '/home/%s/%s' %(self.username.get(), str(uuid.uuid4()))
        remote_input_path = rnd_dir + '/input.xml' 

        # make temporary directory with random hash so no overlap
        # during simultaneous run
        if self.run_and_print('mkdir %s' %rnd_dir) != 0:
            raise ValueError('That hash file already exists..')
        # upload generated input file
        self.output_pipe.insert(END, '\n Uploading input file to %s' %remote_input_path)
        ftp.put(input_path, remote_input_path)
        
        # run Cyclus
        remote_output_path = remote_input_path.replace('input.xml',
                                                       'cyclus.sqlite')
        
        c = self.run_and_print('/home/baej/.local/bin/cyclus %s -o %s --warn-limit 0' %(remote_input_path,
                                                                         remote_output_path), p=True)

        if c == 0 or ('Error' not in c and 'error' not in c and 'Abort' not in c and 'fatal' not in c and 'Invalid' not in c):
            # download yo
            self.output_pipe.insert(END, '\n Run Successful. Now downloading output back into local drive:\n')
            self.check_existing_output()
            ftp.get(remote_output_path, output_path)
            time.sleep(5)
            self.output_pipe.insert(END, '\n All done! Now proceed to backend analysis for some plots and data\n')
                        
        else:
            self.err_message = 'Cyclus run failed! Check terminal output'
            self.output_pipe.insert(END, '\n\n')
            self.output_pipe.insert(END, self.err_message)
            self.return_code = -2
        # delete file
        self.run_and_print('rm -rf %s' %rnd_dir)


