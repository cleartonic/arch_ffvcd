import subprocess
import random
import os
import sys
import logging
import zipfile
import shutil

import logging
logger = logging.getLogger("Final Fantasy V Career Day")

THIS_FILEPATH = os.path.abspath(os.path.dirname(__file__))


ASAR_PATH = os.path.join(THIS_FILEPATH, os.pardir, os.pardir, 'process', 'asar', 'asar')
MAIN_PATCH = os.path.join(THIS_FILEPATH, os.pardir,  os.pardir, 'projects', 'career_day', 'asm', 'all_patches.asm')
TRANSLATE_PATCH = os.path.join(THIS_FILEPATH, os.pardir, os.pardir,  os.pardir, 'basepatch', 'patches', 'rpge.ips')
EXTRA_PATCH4 = os.path.join(THIS_FILEPATH, os.pardir,  os.pardir, os.pardir, 'basepatch', 'patches', 'ff5_lr_menu-1.0.ips')
EXTRA_PATCH5 = os.path.join(THIS_FILEPATH, os.pardir,  os.pardir,  os.pardir,'basepatch', 'patches', 'ff5_optimize.ips')
EXTRA_PATCH6 = os.path.join(THIS_FILEPATH, os.pardir,  os.pardir, os.pardir, 'basepatch', 'patches', 'ff5_reequip.ips')



def copy_ffv(seed, arch_options, output_directory):

    new_filename = "FFVCD_%s_%s.smc" % (arch_options['player'], seed)
    source_path = arch_options['source_rom_abs_path']
    new_filename = os.path.abspath(os.path.join(output_directory, new_filename))
    cd_path = os.path.abspath(output_directory)
    
    shutil.copy(os.path.join(cd_path,source_path), new_filename)
    # command = '''(cd %s && copy "%s" "%s")''' % (cd_path, source_path, new_filename)
    # logger.debug(command)    
    # subprocess.run(command, shell=True)
    if os.path.exists(new_filename):
        return new_filename
    else:
        return None

def process_new_seed(seed = random.randint(0,999999), arch_options = {}, output_directory = ''):

    new_filename = copy_ffv(str(seed), arch_options, output_directory)
    return new_filename





























