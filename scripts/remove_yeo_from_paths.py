# coding: utf-8
import os
import sys

old_path = os.environ['PATH']
old_path = old_path.split(os.path.pathsep)
new_path = os.path.pathsep.join(x for x in old_path if 'yeo' not in x)
sys.stdout.write('PATH_NO_YEO=' + new_path + '\n')
old_ld_library_path = os.environ['LD_LIBRARY_PATH']
new_ld_library_path = os.path.pathsep.join(x for x in old_ld_library_path if 'yeo' not in x)
new_ld_library_path = os.path.pathsep.join(x for x in old_ld_library_path.split(os.path.pathsep) if 'yeo' not in x)
sys.stdout.write('LD_LIBRARY_PATH_NO_YEO=' + new_ld_library_path + '\n')
