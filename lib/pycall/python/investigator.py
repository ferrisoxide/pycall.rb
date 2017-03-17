from distutils.sysconfig import get_config_var
import sys
for var in ('executable', 'exec_prefix', 'prefix'):
  print(var + ': ' + str(getattr(sys, var)))
for var in ('VERSION', 'LIBRARY', 'LDLIBRARY', 'LIBDIR', 'PYTHONFRAMEWORKPREFIX'):
  print(var + ': ' + str(get_config_var(var)))
