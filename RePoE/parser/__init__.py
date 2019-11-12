from RePoE.parser.util import write_json  
import sys, inspect

class Parser_Module(): 

    @classmethod
    def write(self): 
        ''' method which writes json files to data_path'''
        raise NotImplementedError



def _get_child_classes(module, parent_class):
    child_classes = []
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and obj.__bases__[0] == parent_class:
            child_classes.append(obj)
    return child_classes

def get_all_parser_modules():
    from os.path import dirname, basename, isfile, join
    import glob
    modules = glob.glob(join(dirname(__file__), "/modules/*.py"))
    __all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]
