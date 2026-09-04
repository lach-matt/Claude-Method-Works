import sys; sys.path.insert(0,"/home/claude/work")
import importlib.util as iu
sp=iu.spec_from_file_location("li","/home/claude/work/ladder_index.py")
li=iu.module_from_spec(sp)
import builtins
_n=builtins.__name__
sp.loader.exec_module.__self__ if False else None