#!/usr/bin/python
"""Scale runtime environment"""

# standard imports
import os
import sys
import json
# super import
import workbench
here = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(here, 'cyclus'))
import generate_cyclus_sch


class CyclusRuntimeEnvironment(workbench.WorkbenchRuntimeEnvironment):
    """scale-specific runtime environment"""
    def __init__(self):
        """constructor"""
        print('Init')

        # call super class constructor
        super(CyclusRuntimeEnvironment, self).__init__()

    def app_name(self):
        """returns the app's self-designated name"""
        return "cyclus"


    def app_options(self):
        """list of app-specific options"""
        opts = []
        # no options
        return opts

    def environment(self):
        return {}


    def run_args(self, option):
        args = [options.input]
        args.append('-o')
        args.append(os.path.join(options.output_directory, options.output_basename))

        return args


    def update_and_print_grammar(self, grammar_path):
        print('I am getting grammar')
        if self.executable == None:            
            import argparse
            # if the -grammar flag appears earlier in the arg list than the -e, it won't have been set
            # so, we must parse the argv for that case
            parser_for_grammar = argparse.ArgumentParser()
            parser_for_grammar.add_argument("-e", type=str)    
            known, unknown = parser_for_grammar.parse_known_args(sys.argv)        
            self.executable = known.e

        if self.executable == None:
            sys.stderr.write("***Error: The -grammar option requires -e argument!\n")
            sys.exit(1)

        """Checks the provided grammar file and determines if it is out of date
        and if so, updates it accordingly"""        
        cyclus_bin_dir = os.path.dirname(self.executable)
        cyclus_dir = os.path.dirname(cyclus_bin_dir)


        #! technically here the grammar file would be generated from cyclus -m
        #! from the user defined executable
        # this whole thing is taken care:
        # import generate_sch
        # define paths to schema // template // highlight // grammar files
        workbench_basedir = os.path.join(os.path.abspath(self.rte_dir), os.pardir)

        workbench_cyclus_dir = os.path.join(workbench_basedir, 'cyclus')
        if not os.path.isdir(workbench_cyclus_dir):
            os.mkdir(workbench_cyclus_dir)
        self.schema_file_path = os.path.join(workbench_cyclus_dir, 'cyclus.sch')
        # create cyclus template folder if it does not exist:
        self.template_dir_path = os.path.join(workbench_basedir, 'etc', 'Templates', 'cyclus')
        if not os.path.isdir(self.template_dir_path):
            os.mkdir(self.template_dir_path)
        self.highlight_file_path = os.path.join(workbench_basedir, 'etc', 'grammars', 'highlighters', 'cyclus.wbh') 
        self.grammar_file_path = os.path.join(workbench_basedir, 'etc', 'grammars', 'cyclus.wbg')
        print('Generating schema, grammar template, highlight files...\n')
        generate_cyclus_sch.generate_cyclus_workbench_files(schema_path=self.schema_file_path,
                                                     template_dir=self.template_dir_path,
                                                     highlight_path=self.highlight_file_path,
                                                     grammar_path=self.grammar_file_path,
                                                     cyclus_cmd=self.executable)
        return


    def get_grammar_additional_resources(self, grammar_file_path):
        """Returns a list of filepaths that need included which are not normally included"""
        if grammar_file_path is None:
            raise ValueError("The provided path to the grammar file is null")
        if grammar_file_path == "":
            raise ValueError("The provided path to the grammar file is empty")


        #! I don't think Cyclus will need this

        # add path to wasp2py.py to PYTHONPATH
        # Because scale is installed in Workbench/rte, and wasp2py is installed in Workbench/wasppy
        # include the path from rte to wasppy
        pathToSon2py= os.path.join(os.path.dirname(__file__),os.path.pardir,"wasppy")
        if not os.path.isdir(pathToSon2py):
            print ("***Error: Workbench Analysis Sequence Process (WASP) Python wrapper (WASPPY) is not in expected location: ",pathToSon2py)
        sys.path.append(pathToSon2py)
        import wasp2py # son2py
        # TODO: add a check to test the existence of the directory 'build/wasp/wasppy' 

        # read grammar file to get the absolute schema file path
        utildir = os.path.abspath(os.path.join(os.path.abspath(__file__),os.pardir,"util"))
        gschema_filepath = os.path.join(utildir,'grammar.sch')
        grammar_dict = wasp2py.get_json_dict(gschema_filepath,grammar_file_path)

        pdir = os.path.abspath(os.path.join(grammar_file_path,os.pardir))
        schema_path = grammar_dict["schema"]["value"]
        # ../projects/scale/etc/InputDefinitions/finaloutput/scale.sch
        components_path = os.path.abspath(os.path.join(pdir,schema_path,os.pardir,os.pardir,"components"))
        # ../projects/scale/etc/InputDefinitions/components/
        return [str(components_path)]

   

if __name__ == "__main__":
    # execute runtime, ignoring first argument (the python script itself)
    CyclusRuntimeEnvironment().execute(sys.argv[1:])
