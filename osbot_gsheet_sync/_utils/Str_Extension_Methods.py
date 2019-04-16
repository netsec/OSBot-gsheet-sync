import ctypes as c

from pbx_gs_python_utils.utils.Dev import Dev
from pbx_gs_python_utils.utils.Files import Files

get_dict           = c.pythonapi._PyObject_GetDictPtr
get_dict.restype   = c.POINTER(c.py_object)
get_dict.argtypes  = [c.py_object]


bool_patch = get_dict(bool)[0]
bool_patch['print'           ] = lambda self      : print(self)

str_patch = get_dict(str)[0]

str_patch['line_before'      ] = lambda self      : '\r\n' + self
str_patch['file_exists'      ] = lambda self      : Files.exists(self)
str_patch['print'            ] = lambda self      : print(self)
str_patch['path_combine'     ] = lambda self,path : Files.path_combine(self,path)


list_patch = get_dict(list)[0]

list_patch['print'           ] = lambda self      : Dev.pprint(self)
list_patch['size'            ] = lambda self      : len(self)
