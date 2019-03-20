from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
import xml.etree.ElementTree as et
import xmltodict
import uuid
import os
import shutil
import json
import copy


class RegionWindow(Frame):
    def __init__(self, master, output_path):
        """
        Region dict looks like:
        key: region name
        val: dictionary
            key: institution name
            val: array
                [0] prototype name
                [1] n_build
                [2] entertime
                [3] lifetime
        """

        self.master = Toplevel(master)
        self.output_path = output_path
        self.master.geometry('+150+850')
        self.load_prototypes()
        self.status_var = StringVar()
        self.guide()
        self.region_dict = {}

        Label(self.master, text='Region Name:').grid(row=0, column=0)
        region_name = Entry(self.master)
        region_name.grid(row=0, column=1)
        Button(self.master, text='Add Institution', command=lambda : self.add_inst(region_name.get())).grid(row=1, column=0)
        Label(self.master, text='').grid(row=2, column=0)
        Button(self.master, text='Done', command=lambda : self.done_region()).grid(row=3, column=0)

        if os.path.isfile(os.path.join(self.output_path, 'regions.xml')):
            self.read_xml()

        self.status_window = Toplevel(self.master)
        self.status_window.geometry('+500+920')
        Label(self.status_window, text='Current regions:').pack()
        
        self.update_region_status()
        Label(self.status_window, textvariable=self.status_var, justify=LEFT).pack()


    def load_prototypes(self):
        self.prototypes = []
        if os.path.isfile(os.path.join(self.output_path, 'prototypes.xml')):
            with open(os.path.join(self.output_path, 'prototypes.xml'), 'r') as f:
                xml_list = xmltodict.parse(f.read())['root']['facility']
                for facility in xml_list:
                    self.prototypes.append(facility['name'])
 
        else:
            return

    def read_xml(self):
        """
        read xml has wayy too many if else statements
        becasuse xmltodict reads single entries as strings
        while multiple entries as lists..
        """
        with open(os.path.join(self.output_path, 'regions.xml'), 'r') as f:
            xml_list = xmltodict.parse(f.read())['root']['region']
            if isinstance(xml_list, dict):
                xml_list = [xml_list]
            for region in xml_list:
                self.region_dict[region['name']] = {}
                if not isinstance(region['institution'], list):
                    do_it = 1
                else:
                    do_it = len(region['institution'])
                for i in range(do_it):
                    inst_array = []
                    if do_it == 1:
                        prototypes = region['institution']['config']['DeployInst']['prototypes']['val']
                        instname = region['institution']['name']
                    else:
                        prototypes = region['institution'][i]['config']['DeployInst']['prototypes']['val']
                        instname = region['institution'][i]['name']

                    if isinstance(prototypes, str):
                        entry_length = 1
                    else:
                        entry_length = len(prototypes)

                    for indx in range(entry_length):
                        entry_list = []
                        if do_it == 1:
                            entry_dict = region['institution']['config']['DeployInst']
                        else:
                            entry_dict = region['institution'][i]['config']['DeployInst']
                        for cat in ['prototypes', 'n_build', 'build_times', 'lifetimes']:
                            if entry_length == 1:
                                entry_list.append(entry_dict[cat]['val'])
                            else:
                                entry_list.append(entry_dict[cat]['val'][indx])
                        inst_array.append(entry_list)


                    self.region_dict[region['name']][instname] = inst_array

        self.update_region_status()

        # also get from the prototype file



    def done_region(self):
        if len(self.region_dict) == 0:
            messagebox.showerror('Error', 'No Regions were defined!')
            return
        self.compile_dict_to_xml()
        self.master.destroy()

    def compile_dict_to_xml(self):
        # name, institution
        region_template = '<region>\n\t<name>{name}</name>\n\t<config><NullRegion/></config>\n{institution}\n</region>\n'
        # name, deployinst
        inst_template = '\t<institution>\n\t\t<name>{name}</name>\n\t\t<config>\n\t\t\t<DeployInst>\n{deployinst}\n\t\t\t</DeployInst>\n\t\t</config>\n\t</institution>'
        val_template = '\t\t\t\t\t<val>{entry}</val>\n'
        string = '<root>\n'
        for regionname, inst_dict in self.region_dict.items():
            inst_chunk = ''
            for inst_name, inst_array in inst_dict.items():
                proto_string = '\t\t\t\t<prototypes>\n'
                n_build_string = '\t\t\t\t<n_build>\n'
                buildtime_string = '\t\t\t\t<build_times>\n'
                lifetime_string = '\t\t\t\t<lifetimes>\n'
                for entry in inst_array:
                    proto_string += val_template.format(entry=entry[0])
                    n_build_string += val_template.format(entry=entry[1])
                    buildtime_string += val_template.format(entry=entry[2])
                    lifetime_string += val_template.format(entry=entry[3])
                proto_string += '\t\t\t\t</prototypes>\n'
                n_build_string += '\t\t\t\t</n_build>\n'
                buildtime_string += '\t\t\t\t</build_times>\n'
                lifetime_string += '\t\t\t\t</lifetimes>\n'
                all_four = proto_string + n_build_string + buildtime_string + lifetime_string
                inst_chunk += inst_template.format(name=inst_name, deployinst=all_four)
            string += region_template.format(name=regionname, institution=inst_chunk)
        string += '\n</root>'
        with open(os.path.join(self.output_path, 'regions.xml'), 'w') as f:
            f.write(string)
        messagebox.showinfo('Success', 'Successfully rendered %i regions!' %len(self.region_dict))


    def add_inst(self, region_name):
        if region_name == '':
            messagebox.showerror('Error', 'You have to define the region name before adding and institution!')
            return
        self.add_inst_window = Toplevel(self.master)
        self.add_inst_window.geometry('+100+1000')
        self.inst_dict = {}
        self.region_dict[region_name] = {}
        self.current_region = region_name
        Label(self.add_inst_window, text='Institution Name:').grid(row=0, column=1)
        inst_name_entry = Entry(self.add_inst_window)
        inst_name_entry.grid(row=0, column=2)
        Button(self.add_inst_window, text='Done', command= lambda : self.submit_inst(inst_name_entry.get())).grid(row=1, column=0)
        Label(self.add_inst_window, text='Add new prototypes here:').grid(row=2, columnspan=3)
        Button(self.add_inst_window, text='Add Row', command= lambda: self.add_inst_row()).grid(row=3, column=3)
        self.inst_entry_dict = {'prototypes': [], 'lifetimes': [],
                                'n_build': [], 'build_times': []}
        self.cat_list = ['prototypes', 'n_build', 'build_times', 'lifetimes']
        for indx, val in enumerate(self.cat_list):
            Label(self.add_inst_window, text=val).grid(row=4, column=indx)
            self.inst_entry_dict[val].append(Entry(self.add_inst_window))
            self.inst_entry_dict[val][-1].grid(row=5, column=indx)
        self.rownum = 6

        # show realtime institutions added

    def submit_inst(self, inst_name):
        # check input correctness:
        if inst_name == '':
            messagebox.showerror('Error', 'You have to define an Institution Name')
            return
        inst_array = []
        for indx in range(len(self.inst_entry_dict['prototypes'])):
            prototype_ = self.inst_entry_dict['prototypes'][indx].get()
            lifetime_ = self.inst_entry_dict['lifetimes'][indx].get()
            build_time_ = self.inst_entry_dict['build_times'][indx].get()
            n_build_ = self.inst_entry_dict['n_build'][indx].get()
            # skip missing rows
            if prototype_ == lifetime_ == build_time_ == n_build_ == '':
                continue
            # check if there are missing parameters
            elif '' in [prototype_, lifetime_, build_time_, n_build_]:
                messagebox.showerror('Error', 'You are missing a parameter for line %i' %indx)
                return
            # check if the ints are ints
            if not (self.check_if_int(lifetime_) & self.check_if_int(build_time_)
                    & self.check_if_int(n_build_)):
                messagebox.showerror('Error', 'Entertime, lifetime, and n_build have to be integers.')
                return
            inst_array.append([prototype_, n_build_, build_time_, lifetime_])
            
        if len(inst_array) == 0:
            messagebox.showerror('Error', 'There are no entries! ')
            return
        self.inst_dict[inst_name] = inst_array
        messagebox.showinfo('Added', 'Added institution %s' %inst_name)
        self.region_dict[self.current_region] = self.inst_dict
        self.update_region_status()
        self.add_inst_window.destroy()


    def check_if_int(self, string):
        try:
            int(string)
            return True
        except ValueError:
            return False


    def add_inst_row(self):
        for indx, val in enumerate(self.cat_list):
            self.inst_entry_dict[val].append(Entry(self.add_inst_window))
            self.inst_entry_dict[val][-1].grid(row=self.rownum, column=indx)
        self.rownum += 1

    def update_region_status(self):
        string = '\t\t\t\t\tN_build\tBuild Time\t Lifetime'
        for key, val in self.region_dict.items():
            string += '\n' + key + '\n'
            for key2, val2 in val.items():
                string += '\t-> ' + key2 + '\t\t\t' + '\t' + '\t' + '\n'
                for i in val2:
                    if i[0] not in self.prototypes:
                        i[0] += ' (x)'
                    string += '\t\t->> ' + i[0] + '\t\t' + i[1] +'\t' + i[2] + '\t' + i[3] + '\n'
        self.status_var.set(string)


    def close_window(self):
        self.master.destroy()

    def guide(self):
        string = """
        This is where you define how the prototypes you defined will be played
        in the simulation - when they enter, how many enters, and when they exit.

        The region definition in this GUI by default uses 
        NullInst and DeployInst. A region has one or many institutions.
        Click on `Add Region', specify a Region Name, and click 'Add Institution'
        to define a single institution. The institution will be part of the region
        you specified.

        One row in the institution definition window is for one prototype.
        Define the name, how many to build, when to enter, and how long to stay
        for each prototype. Click 'Add Row' if you want to add more prototypes.

        Once done, click done to add the institution into the region. The status
        window will reflect the changes you've made.

        A prototype with a `(x)' next to it means that the prototype has not
        been defined by the prototype definition section.

        Once done, clikc Done in the region window.
        """
        self.guide_window = Toplevel(self.master)
        self.guide_window.geometry('+0+400')
        Label(self.guide_window, text=string).pack(padx=30, pady=30)

