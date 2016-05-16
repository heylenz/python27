#!D:\yinhailin\pyvfx-x\python\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'anyconfig==0.5.0','console_scripts','anyconfig_cli'
__requires__ = 'anyconfig==0.5.0'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('anyconfig==0.5.0', 'console_scripts', 'anyconfig_cli')()
    )
