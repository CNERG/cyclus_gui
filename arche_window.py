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
import subprocess


class ArchetypeWindow(Frame):
    def __init__(self, master, output_path):
        """
        arche looks like:
        array = []
        [0] = library
        [1] = archetype name
        """
        self.master = Toplevel(master)
        self.output_path = output_path
        self.master.geometry('+0+900')
        self.guide()
        self.arche = [['agents', 'NullInst'], ['agents', 'NullRegion'], ['cycamore', 'Source'],
                      ['cycamore', 'Sink'], ['cycamore', 'DeployInst'], ['cycamore', 'Enrichment'],
                      ['cycamore', 'FuelFab'], ['cycamore', 'GrowthRegion'], ['cycamore', 'ManagerInst'],
                      ['cycamore', 'Mixer'], ['cycamore', 'Reactor'], ['cycamore', 'Separations'],
                      ['cycamore', 'Storage']]
        try:
            path = os.path.join(self.output_path, 'm.json')
            command = 'cyclus -m'
            process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
            jtxt = process.stdout.read()
            print(jtxt)
            with open(path, 'wb') as f:
                f.write(jtxt)
            j = json.loads(jtxt)
            messagebox.showinfo('Found', 'Found Cyclus, automatically grabbing archetype libraries :)')
            self.arche = j['specs']
            self.arche = [[q[0], q[1]] for q in (i[1:].split(':') for i in self.arche)]
        except:
            messagebox.showinfo('Cyclus not found', 'Cyclus is not found. Using all cyclus/cycamore arcehtypes as default.')
        self.default_arche = copy.deepcopy(self.arche)
        if os.path.isfile(os.path.join(self.output_path, 'archetypes.xml')): 
            self.read_xml()



        Button(self.master, text='Add Row', command= lambda : self.add_more()).grid(row=1)
        Button(self.master, text='Add!', command= lambda : self.add()).grid(row=2)
        Button(self.master, text='Default', command= lambda: self.to_default()).grid(row=3)

        Label(self.master, text='').grid(row=4)

        Button(self.master, text='Done', command= lambda: self.done()).grid(row=5)
        Label(self.master, text='Library').grid(row=0, column=2)
        Label(self.master, text='Archetype').grid(row=0, column=3)
        self.entry_list = []
        self.additional_arche = []
        self.rownum = 1

        # status window
        self.update_loaded_modules_window()


    def update_loaded_modules_window(self):
        """ this functions updates the label object in the status window
            so the loaded archetypes are updated live"""
        try:
            self.status_window.destroy()
        except:
            z=0

        self.status_window = Toplevel(self.master)
        self.status_window.geometry('+700+1000')
        Label(self.status_window, text='Loaded modules:').grid(row=0, columnspan=2)
        row = 1
        for i in self.arche:
            Label(self.status_window, text=i[0] + '::' + i[1]).grid(row=row, column=0)
            # lib_name = [copy.deepcopy(i[0]), copy.deepcopy(i[1])]
            Button(self.status_window, text='x', command=lambda i=i: self.delete_arche([i[0], i[1]])).grid(row=row, column=1)
            row += 1


    def delete_arche(self, lib_name):
        print(self.arche)
        print(lib_name)
        for indx, val in enumerate(self.arche):
            if val == lib_name:
                it = indx
                print('IT', it)
        del self.arche[it]
        print(self.arche)
        self.update_loaded_modules_window()


    def read_xml(self):
        new_arche = []
        with open(os.path.join(self.output_path, 'archetypes.xml'), 'r') as f:
            xml_dict = xmltodict.parse(f.read())['archetypes']
        for entry in xml_dict['spec']:
            new_arche.append([entry['lib'], entry['name']])
        self.arche = new_arche

    def add_more(self):
        row_list = []
        # library and archetype set
        row_list.append(Entry(self.master))
        row_list.append(Entry(self.master))
        row_list[0].grid(row=self.rownum, column=2)
        row_list[1].grid(row=self.rownum, column=3)
        self.entry_list.append(row_list)
        self.rownum += 1

    def to_default(self):
        self.arche = self.default_arche
        self.update_loaded_modules_window()

    def add(self):
        enter = [[x[0].get(), x[1].get()] for x in self.entry_list]
        dont_add_indx = []
        messed_up_indx = []
        err = False
        for indx,entry in enumerate(enter):
            if entry[0] == '' and entry[1] == '':
                dont_add_indx.append(indx)
            if entry[0] == '' and entry[1] != '':
                messed_up_indx.append(indx)
                err = True
        if len(dont_add_indx) == len(enter):
            messagebox.showerror('Error', 'You did not input any libraries. Click Done if you do not want to add more libraries.')
            return
        if err:
            message = 'You messed up on rows:\n'
            for indx in messed_up_indx:
                message += indx + '\t'
            messagebox.showerror('Error', message)
            return
        else:

            string = 'Adding %i new libraries' %(len(enter) - len(dont_add_indx))
            if len(dont_add_indx) != 0:
                string += '\n Ignoring empty rows: '
                for r in dont_add_indx:
                    string += r + '  '
            for indx, val in enumerate(enter):
                if indx in dont_add_indx:
                    continue
                self.arche.append(val)
            self.update_loaded_modules_window()


    def done(self):
        string = '<archetypes>\n'
        for pair in self.arche:
            string += '\t<spec>\t<lib>%s</lib>\t<name>%s</name></spec>\n' %(pair[0], pair[1])
        string += '</archetypes>\n'
        with open(os.path.join(self.output_path, 'archetypes.xml'), 'w') as f:
            f.write(string)
        self.master.destroy()

    def guide(self):

        self.guide_window = Toplevel(self.master)
        self.guide_window.geometry('+0+3500')
        guide_string = """
        All Cyclus and Cycamore archetypes are already added. If there are additional archetypes
        you would like to add, click the `Add Row' button, type in the library and archetype,
        and press `Add!'.

        Try not to delete cycamore::DeployInst and agents::NullRegion, since they are the
        default for this gui.

        If you made a mistake, you can go back to the default Cyclus + Cycamore
        archetypes by clicking `Default'.

        Once you're done, click `Done'.


        FOR MORE INFORMATION:
        http://fuelcycle.org/user/input_specs/archetypes.html
        """
        Label(self.guide_window, text=guide_string, justify=LEFT).pack(padx=30, pady=30)
