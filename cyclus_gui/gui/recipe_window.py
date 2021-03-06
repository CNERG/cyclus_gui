from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
import xmltodict
import uuid
import os
import shutil
import json
from cyclus_gui.gui.read_xml import *


class RecipeWindow(Frame):
    """ Note: Recipes are generated with <root> parent node for xml for parsing reasons

        recipe_dict:
        key: recipe name
        val: dict
             key: 'base', 'composition'
             val: str(base), dict(composition)
                             key: isotope name
                             val: frac (base-frac)
    """

    def __init__(self, master, output_path):
        self.screen_width = master.winfo_screenwidth()
        self.screen_height = master.winfo_screenheight()
        self.master = Toplevel(master)
        self.master.title('Define recipes')
        self.output_path = output_path
        self.master.geometry('+0+%s' %int(self.screen_height/4))
        self.scrape_for_recipes_in_facility()
        self.guide()
        browse_button = Button(self.master, text='Add From File [atomic]', command=lambda : self.askopenfile('atom')).grid(row=1)
        browse_button = Button(self.master, text='Add From File [mass]', command= lambda : self.askopenfile('mass')).grid(row=2)
        Button(self.master, text='Add all from Directory [atomic]', command=lambda : self.askopendir('atom')).grid(row=3)
        Button(self.master, text='Add all from Directory [mass]', command=lambda : self.askopendir('mass')).grid(row=4)
        Button(self.master, text='Add Recipe Manually [atomic]', command=lambda : self.add_recipe('atom')).grid(row=5)
        Button(self.master, text='Add Recipe Manually [mass]', command=lambda : self.add_recipe('mass')).grid(row=6)
        Button(self.master, text='Add dummy recipe', command=lambda: self.add_dummy()).grid(row=7)

        Label(self.master, text='').grid(row=8)

        Button(self.master, text='Finish', command=lambda: self.done()).grid(row=9)
        self.recipe_dict = {}

        if os.path.isfile(os.path.join(self.output_path, 'recipe.xml')):
            self.recipe_dict, n = read_xml(os.path.join(self.output_path, 'recipe.xml'), 'recipe')
        

        self.update_loaded_recipes()


    def scrape_for_recipes_in_facility(self):
        self.defined_recipe_dict = {}
        already_in = []
        if os.path.exists(os.path.join(self.output_path, 'facility.xml')):
            with open(os.path.join(self.output_path, 'facility.xml'), 'r') as f:
                xml_list = xmltodict.parse(f.read())['root']['facility']
                if not isinstance(xml_list, list):
                    xml_list = [xml_list]
                for facility in xml_list:
                    for key, val in facility['config'].items():
                        for key2, val2 in val.items():
                            if 'recipe' in key2 and val2 not in already_in:
                                self.defined_recipe_dict[facility['name']+' [%s]' %key2] = val2
                                already_in.append(val2)
        new_ = {}
        for key, val in self.defined_recipe_dict.items():
            if 'ict' in str(type(val)):
                new_[key] = val['val']
            else:
                new_[key] = val
        self.defined_recipe_dict = new_
        if len(self.defined_recipe_dict.keys()) != 0:
            self.recipes_defined = True
        else:
            self.recipes_defined = False


    def add_dummy(self):
        dummy_recipe = {'H1': 100}
        if 'dummy' not in self.recipe_dict.keys():
            self.recipe_dict['dummy'] = {'base': 'mass', 'composition': dummy_recipe}
        else:
            z = 0
            while True:
                k = 'dummy' + str(z)
                if k in self.recipe_dict.keys():
                    z += 1
                else:
                    self.recipe_dict[k] = {'base': 'mass', 'composition': dummy_recipe}
                    break
        self.update_loaded_recipes()



    def update_loaded_recipes(self):
        try:
            self.status_window.destroy()
        except:
            z=0

        self.status_window = Toplevel(self.master)
        self.status_window.title('Defined Recipes')
        self.status_window.geometry('+%s+0' %int(self.screen_width/3))
        Label(self.status_window, text='Loaded recipes:', bg='yellow').grid(row=0, columnspan=2)
        row=1
        print(self.recipe_dict)
        for key in self.recipe_dict:
            Button(self.status_window, text='x', command=lambda key=key: self.del_recipe(key)).grid(row=row, column=0)
            Button(self.status_window, text=key, command=lambda key=key: self.edit_recipe(key)).grid(row=row, column=1)
            row += 1


    def del_recipe(self, recipename):
        self.recipe_dict.pop(recipename, None)
        self.update_loaded_recipes()

    def edit_recipe(self, recipename):
        self.add_recipe(self.recipe_dict[recipename]['base'])
        self.name_entry.insert(END, recipename)
        string = ''
        for iso, val in self.recipe_dict[recipename]['composition'].items():
            string += '%s\t%s\n' %(iso,val)
        self.textfield.insert(INSERT, string)


    def add_recipe(self, atom_or_mass):
        """
        Button add recipe will prompt user-input recipe name and text
        """
        self.addrecipe_window = Toplevel(self.master)
        self.addrecipe_window.title('New recipe definition (%s)' %atom_or_mass)
        self.addrecipe_window.geometry('+%s+%s' %(int(self.screen_width/4), int(self.screen_height/1.8)))
        

        Button(self.addrecipe_window, text='Done!',
               command= lambda : self.send_input(self.name_entry, self.textfield, self.addrecipe_window, atom_or_mass)).grid(row=0, columnspan=2)
        Label(self.addrecipe_window, text='Recipe name').grid(row=1, column=0)
        self.name_entry = Entry(self.addrecipe_window)
        self.name_entry.grid(row=1, column=1)
        Label(self.addrecipe_window, text='Recipe:').grid(row=2, columnspan=2)
        self.textfield = ScrolledText(self.addrecipe_window, wrap=WORD)
        self.textfield.grid(row=3, columnspan=2)


    def send_input(self, name, text, window, atom_or_mass):
        """
        Gets the entry and scrolltext objects and obtains the actual data
        and sends it to recipe_input for testing and storage.
        """
        name = name.get() + '_' + atom_or_mass
        text = str(text.get(1.0, END))
        self.recipe_input(name, text, window)



    def recipe_input(self, name, text, window):
        if name == '' or text == '':
            messagebox.showerror('Name or text missing! :(')
            return
        if name.split('_')[-1] not in ['atom', 'mass']:
            raise ValueError('Something Wrong man, either has to have _atom or _mass appended')
        base = name.split('_')[-1]
        name = name.replace('_'+base, '')


        # check input
        # if it recognizes a comma, then we are going to
        # look at it as a csv file
        # if not, its just the plaintext format
        if ',' in text:
            text = text.replace(',', ' ')    
        composition_dict = self.parse_plaintext(text)
        

        if composition_dict == None:
            messagebox.showerror('Error', 'The recipe text (%s) is malformed! :( ' %name)
            return


        self.recipe_dict[name] = {'base': base,
                                  'composition': composition_dict}
        # if not good, error message
        # if good, kill window
        messagebox.showinfo('Recipe Saved', 'Recipe %s is saved!' %name)
        if window != None:
            window.destroy()
        self.update_loaded_recipes()


    def parse_plaintext(self, text):
        composition_dict = {}
        for row in text.split('\n'):
            if row == '':
                continue
            e = row.split()
            composition_dict[e[0]] = float(e[1])        
        return composition_dict


    def askopenfile(self, base):
        file = filedialog.askopenfile(parent=self.master, mode='r', title='Choose a file')
        if not file:
            # nonetype, user cancelled
            return
        filename = os.path.splitext(os.path.basename(file.name))[0] + '_' + base
        data = file.read()
        
        self.recipe_input(filename, data, None)

    def askopendir(self, base):
        file = filedialog.askdirectory()
        files = os.listdir(file)
        for filename in files:
            f = open(os.path.join(file, filename), 'r')
            data = f.read()
            filename = filename.split('.')[0]
            filename_base = filename+'_'+base
            self.recipe_input(filename_base, data, None)



    def done(self):
        string = '<root>\n'
        if len(self.recipe_dict.keys()) == 0:
            messagebox.showerror('Error', 'There are no recipes to output :(')
            return
        temp = '<recipe>\n\t<name>{name}</name>\n\t<basis>{base}</basis>\n{recipe}</recipe>\n'

        for key in self.recipe_dict:
            comp_string = ''
            for iso, comp in self.recipe_dict[key]['composition'].items():
                comp_string += '\t<nuclide>\t<id>%s</id>\t<comp>%f</comp>\t</nuclide>\n' %(iso, float(comp))
            name = key
            base = self.recipe_dict[key]['base']
            string += temp.format(name=name,
                                  base=base,
                                  recipe=comp_string)
            string += '\n'
        string += '</root>'
        with open(os.path.join(self.output_path, 'recipe.xml'), 'w') as f:
            f.write(string)
        messagebox.showinfo('Success', 'Successfully rendered %i recipes! :)' %len(self.recipe_dict.keys()))
        self.master.destroy()

    def guide(self):
        self.guide_window = Toplevel(self.master)
        self.guide_window.title('Recipe guide')
        self.guide_window.geometry('+%s+0' %int(self.screen_width/1.5))
        guide_string = """
The format of recipes could be comma, space, or tab separated.
For example:
92235 0.7
92238 99.3
OR
92235, 0.7
92238, 99.3
OR
92235   0.7
92238   99.3

Note:
1. The compositions are automatically normalized by Cyclus :)
2. Acceptable formats for isotope symbols are:
    ZZAAA, ZZAAASSSS, name (e.g. Pu-239, Pu239, pu-239)

When you add recipe from a file, the filename becomes the recipe name.
You can also add multiple recipes at a time by selecting a directory
that contains multiple recipe files.

If there are no recipes to define, just define a dummy one manually and move on.
        """
        if self.recipes_defined:
            guide_string += '\nThe following recipe names are defined in the facility block:\n\n'
        for key, val in self.defined_recipe_dict.items():
            if isinstance(val, list):
                guide_string += 'FROM %s:\n' %key
                for i in val:
                    guide_string += '\t%s\n' %i
                guide_string += '\n'
            else:
                guide_string += 'FROM %s:\n\t%s\n\n' %(key, val)

        st = ScrolledText(master=self.guide_window,
                  wrap=WORD)
        st.pack()
        st.insert(INSERT, guide_string)
