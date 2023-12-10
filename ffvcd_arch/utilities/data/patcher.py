import subprocess
import random
import os
import ips
import sys
import logging
import zipfile

THIS_FILEPATH = os.path.dirname(__file__)
sys.path.append(THIS_FILEPATH)


ASAR_PATH = os.path.join(THIS_FILEPATH,os.pardir, os.pardir, 'process', 'asar', 'asar')
MAIN_PATCH = os.path.join(THIS_FILEPATH,os.pardir, os.pardir, 'projects', 'career_day', 'asm', 'all_patches.asm')
TRANSLATE_PATCH = os.path.join(THIS_FILEPATH,os.pardir, os.pardir, 'process', 'patches', 'rpge.ips')
RANDOMIZER_ASM = os.path.join(THIS_FILEPATH,os.pardir, os.pardir, 'process', 'r-patch.asm')

EXTRA_PATCH4 = os.path.join(THIS_FILEPATH,os.pardir, os.pardir, 'process', 'patches', 'ff5_lr_menu-1.0.ips')
EXTRA_PATCH5 = os.path.join(THIS_FILEPATH,os.pardir, os.pardir, 'process', 'patches', 'ff5_optimize.ips')
EXTRA_PATCH6 = os.path.join(THIS_FILEPATH,os.pardir, os.pardir, 'process', 'patches', 'ff5_reequip.ips')


HEADERED_J_SIZE = 2097664
UNHEADERED_J_SIZE = 2097152
HEADERED_U_SIZE = 2621952
UNHEADERED_U_SIZE = 2621440

FAKE_HEADER = bytearray.fromhex('''0001 0080 0000 0000 aabb 0400 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000''')

logging.basicConfig(filename="error.log", level=logging.ERROR, format="%(asctime)-15s %(message)s")


def patch_and_return(filename):
    

    logging.error("Begin patch & return process")
    reheader = False
    smc = False
    rpge = False
    extra_patches_flag = True

    with open(filename, "rb") as file:
        romdata = bytearray(file.read())

    if len(romdata) == UNHEADERED_J_SIZE:
        logging.error("Detected unheadered, untranslated rom")
        reheader = True
        smc = False
        rpge = True
    if len(romdata) == HEADERED_J_SIZE:
        logging.error("Detected headered, untranslated rom")
        reheader = False
        smc = True
        rpge = True
    if len(romdata) == UNHEADERED_U_SIZE:
        logging.error("Detected unheadered, translated rom")
        reheader = True
        smc = False
        rpge = False
    if len(romdata) == HEADERED_U_SIZE:
        logging.error("Detected headered, translated rom")
        reheader = False
        smc = True
        rpge = False

    smc = headers_and_translate(filename, reheader, rpge, extra_patches_flag, smc)

    if smc:
        os.rename(filename, filename.replace(".sfc",".smc"))
        filename = filename.replace(".sfc",".smc")
    else:
        os.rename(filename, filename.replace(".smc",".sfc"))
        filename = filename.replace(".smc",".sfc")



    patch_careerday(filename)

    patch_random(filename, RANDOMIZER_ASM)
    
    
    
    
    
    
    
    
    

def headers_and_translate(filename, reheader, rpge, extra_patches, smc):

    # reheader = there is no header on the rom 
    # not reheader = there is a header on the rom 



    try:
        if extra_patches:
            logging.error("Applying extra patches")

            logging.error("Checking for unheadered files")
            if not reheader:
                logging.error("REMOVING header from rom for extra_patches")
                with open(filename, "r+b") as file:
                    data = bytearray(file.read())
                    data = remove_header(data)
                    file.seek(0)
                    logging.error(len(data))
                    file.write(data)
                logging.error("Rom REMOVED header")
                smc = True
                reheader = True

            # ips.apply(EXTRA_PATCH1, filename)
            # ips.apply(EXTRA_PATCH2, filename)
            # ips.apply(EXTRA_PATCH3, filename)
            ips.apply(EXTRA_PATCH4, filename)
            ips.apply(EXTRA_PATCH5, filename)
            ips.apply(EXTRA_PATCH6, filename) 
            # ips.apply(EXTRA_PATCH7, filename)
            logging.error("Extra patches applied successfully")
    except FileNotFoundError as e:
        logging.error("Error applying extra patches")
        logging.error("Extra patches missing. Verify patches files exist in patches directory")
    except Exception as e:
        logging.error("Error applying extra patches")
        logging.error("Unknown exception: "+str(e))
        
        
        
    if reheader:
        logging.error("Reheadering rom for RPGe patch application")
        with open(filename, "r+b") as file:
            data = bytearray(file.read())
            data = add_header(data)
            file.seek(0)
            logging.error(len(data))
            file.write(data)
        logging.error("Rom reheadered")
        smc = True

    try:
        if rpge:
            logging.error("Applying RPGe Translation")
            ips.apply(TRANSLATE_PATCH, filename)
            logging.error("RPGe Translation applied successfully")
    except FileNotFoundError as e:
        logging.error("Error applying RPGe Translation Patch")
        logging.error("RPGe Patch Missing. Verify rpge.ips file exists in patches directory")
    except Exception as e:
        logging.error("Error applying RPGe Translation Patch")
        logging.error("Unknown exception: "+str(e))

    return smc


def add_header(byte_list):
    return FAKE_HEADER + byte_list

def remove_header(byte_list):
    new_bytes = byte_list[512:]
    return new_bytes

def translateBool(boolean):
    if type(boolean) == bool:
        return boolean
    if boolean == "false":
        return False
    if boolean == "true":
        return True
    else:
        return None

def bool_to_int(boolean):
    if boolean:
        return 1
    else:
        return 0
    

def copy_ffv(seed):

    new_filename = "FFVCD_%s.smc" % seed
    if "win" in os.sys.platform:
        cd_path = os.path.abspath(os.path.join(THIS_FILEPATH,os.pardir,os.pardir,'process'))
        command = '''(cd %s && copy "Final Fantasy V (J).smc" "output/%s")''' % (cd_path, new_filename)
        logging.error(command)    
        response = subprocess.run(command, shell=True)
        new_filename = os.path.abspath(os.path.join(THIS_FILEPATH, os.pardir, os.pardir,'process' ,'output', new_filename))
    
        
        if os.path.exists(new_filename):
            return new_filename
        else:
            return None
        
        
    else:
        return None
    
def patch_careerday(filename):
    fjf = 0
    fourjoblock = 0
    progressive_rewards = 0
    abbreviated = 1
    grantkeyitems = 0
    free_tablets = 0
    starting_cara = 0
    everysteprandomencounter = 1
    explv50 = 0
    end_on_exdeath1 = 0
    remove_ned = 0
    kuzar_credits_warp = 0
    # world_lock should be passed as an integer (either 0, 1 or 2). If it's not, make a function to do so
    world_lock = 1
    remove_flashes = 0
    
    command = "{} --define dash=1 --define learning=1 --define pitfalls=1 \
    --define passages=1 --define double_atb=0 --define progressive={} --define abbreviated={} --define grantkeyitems={} --define boss_exp=1 --define free_tablets={} \
    --define fourjobmode={} --define fourjoblock={} --define world_lock={} --define starting_cara={} --define end_on_exdeath1={}  --define remove_ned={} --define everysteprandomencounter={} --define explv50={} --define remove_flashes={} --define kuzar_credits_warp={} \
    --fix-checksum=off --define vanillarewards=0 --no-title-check {} {}".format(ASAR_PATH,progressive_rewards, abbreviated, grantkeyitems, free_tablets, fjf, fourjoblock, world_lock, starting_cara, end_on_exdeath1, remove_ned, everysteprandomencounter, explv50, remove_flashes, kuzar_credits_warp, MAIN_PATCH, os.path.abspath(filename))

    logging.error(command)
    
    response = subprocess.run(command, shell=True)

def patch_random(filename, patchname):
    command = "{} --fix-checksum=off {} {}".format(ASAR_PATH, patchname, filename)
    logging.error(command)
    response = subprocess.run(command, shell=True)


def process_new_seed(seed = random.randint(0,999999)):
    new_filename = copy_ffv(str(seed))
    filename = new_filename
    patch_and_return(new_filename)


