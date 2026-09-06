import sys; sys.path.insert(0,"/home/claude/work")
import importlib.util as iu
sp=iu.spec_from_file_location("l2","/home/claude/work/ladder_index2.py"); m=iu.module_from_spec(sp)
import builtins; sp.loader.exec_module(m)