
from os.path import dirname, basename, isfile, join
from RePoE.parser import Parser_Module
import glob
import inspect
import importlib

def _get_child_classes(module, parent_class):
    child_classes = []
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and obj.__bases__[0] == parent_class:
            child_classes.append(obj)
    return child_classes

def get_all_modules():
    file_names = glob.glob(join(dirname(__file__), "*.py"))
    module_strings = [ basename(f)[:-3] for f in file_names if isfile(f) and not f.endswith('__init__.py')]
    return [importlib.import_module(f"RePoE.parser.modules.{module_string}") for module_string in module_strings]

def get_parser_modules():
    parser_modules = []
    
    for module in get_all_modules():
        classes = _get_child_classes(module, Parser_Module)
        for parser_module in classes:
            parser_modules.append(parser_module)

        if len(classes) == 0:
            print(f"Warning: module {module} has no Parser_Module")
    
    return parser_modules

