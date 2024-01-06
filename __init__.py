import os
import threading
import base64
from BaseClasses import Item, MultiWorld, Tutorial, ItemClassification
from worlds.AutoWorld import World, WebWorld
from .items import item_table, item_groups, create_item, create_world_items, FFVCDItem, arch_item_offset, WORLD2_ACCESS_ITEM_ID, WORLD3_ACCESS_ITEM_ID
from .locations import location_data, loc_id_start
from .options import ffvcd_options
from .regions import create_regions
from .rules import set_rules
from worlds.ffvcd.ffvcd_arch.utilities.data import conductor
from .rom import LocalRom, get_base_rom_path, patch_rom
from collections import Counter

# lots of credit to others in the repository, such as pokemonrb, dkc3 and tloz

class FFVCDWebWorld(WebWorld):
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to playing Final Fantasy V with Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["cleartonic"]
    )
    theme = 'ice'
    tutorials = [setup_en]


class FFVCDWorld(World):
    """Final Fantasy V: Career Day"""

    game = "Final Fantasy V Career Day"
    option_definitions = ffvcd_options
    settings: None
    
    
    topology_present = False
    data_version = 1
    base_id = 776000
    
    item_name_to_id = {name: data.id for name, data in item_table.items()}
    location_name_to_id = {location.name: location.address for location in location_data}

    item_name_groups = item_groups

    web = FFVCDWebWorld()
    set_rules = set_rules
    
    cond = None

    
    def __init__(self, world: MultiWorld, player: int):
        self.rom_name_available_event = threading.Event()
        super().__init__(world, player)


    @classmethod
    def stage_assert_generate(cls, multiworld: MultiWorld):
        rom_file = get_base_rom_path()
        if not os.path.exists(rom_file):
            raise FileNotFoundError(rom_file)
        else:
            import Utils
            cls.rom_file = rom_file
            cls.source_rom_abs_path = os.path.abspath(Utils.user_path(rom_file))


    def generate_early(self):
        self.starting_items = Counter()
        world_lock = [i for i in self.multiworld.world_lock[self.player].value][0]
        if world_lock == '2':
            new_item = create_item("World 2 Access (Item)",  
                        ItemClassification.progression, 
                        WORLD2_ACCESS_ITEM_ID + arch_item_offset, 
                        self.player, ['World Access'])
            self.starting_items[new_item] = 1
            self.multiworld.push_precollected(new_item)
        if world_lock == '3':
            new_item = create_item("World 2 Access (Item)",  
                        ItemClassification.progression, 
                        WORLD2_ACCESS_ITEM_ID + arch_item_offset, 
                        self.player, ['World Access'])
            self.starting_items[new_item] = 1
            self.multiworld.push_precollected(new_item)
            new_item = create_item("World 3 Access (Item)",  
                        ItemClassification.progression, 
                        WORLD3_ACCESS_ITEM_ID + arch_item_offset, 
                        self.player, ['World Access'])
            self.starting_items[new_item] = 1
            self.multiworld.push_precollected(new_item)

            



    def create_items(self):        
        create_world_items(self)
        
    def post_fill(self):


        locs = [i for i in self.multiworld.get_locations(self.player)]
        data = {}
        
        for loc in locs:
            if loc.address:
                lname = loc.item.name
                data[hex(loc.address - loc_id_start).replace("0x","").upper()] = {'loc_name' : lname,
                                                                   'loc_player' : loc.item.player,
                                                                   'loc_progression' : loc.item.advancement}

        
        options_conductor = self.parse_options_for_conductor()

        
        self.cond = conductor.Conductor(self.multiworld.random, options_conductor, arch_data = data, player = self.player, seed = self.multiworld.seed)
        self.cond.randomize()
        

    def parse_options_for_conductor(self):
        # this sets up a config file from archipelago's options
        # for FFVCD's base randomizer to work with
        options_conductor = {}
        if self.multiworld.job_palettes[self.player]:
            options_conductor['job_palettes'] = True
        else:
            options_conductor['job_palettes'] = False
            
        if self.multiworld.four_job[self.player]:
            options_conductor['four_job'] = True
        else:
            options_conductor['four_job'] = False

           
        if self.multiworld.remove_flashes[self.player]:
            options_conductor['remove_flashes'] = True
        else:
            options_conductor['remove_flashes'] = False

            
        options_conductor['source_rom_abs_path'] = self.source_rom_abs_path
        options_conductor['world_lock'] = [i for i in self.multiworld.world_lock[self.player].value][0]
        options_conductor['player'] = self.player
        
        self.options_conductor = options_conductor
            
        return options_conductor
                
    def create_regions(self):
        create_regions(self.multiworld, self.player)

    def generate_output(self, output_directory: str):
        # move 

        r_patch_file, spoiler_file, temp_patch_path, temp_spoiler_path = self.cond.save_spoiler_and_patch(output_directory)
        self.filename_randomized = self.cond.patch_file(output_directory, r_patch_file, spoiler_file)


        rompath = os.path.join(output_directory, f"{self.multiworld.get_out_file_name_base(self.player)}.smc")

        ################
        # temporarily copy file over 
        ################
        import shutil
        print("Copying %s -> %s" % (self.filename_randomized, rompath))
        shutil.copy(self.filename_randomized, rompath)
        print("File moved")
        ################

        
        rom = LocalRom(rompath) # obsolete file=get_base_rom_path() for now, but later will need to use it somehow
        patch_rom(self.multiworld, rom, self.player)
        self.rom_name = rom.name
        
        
        rom.write_to_file(rompath)
        
        
        # breakpoint()



        ################
        # new system
        ################
        import bsdiff4 
        four_job = "" if self.options_conductor['four_job'] else 'no'
        basepatch_to_use = os.path.join('worlds',
                                        'ffvcd',
                                        'ffvcd_arch', 
                                        'process',
                                        'basepatch',
                                        "ffv_%sfjf_world%slock.bsdiff4" % (four_job,
                                                              self.options_conductor['world_lock'])
                                        )
        
        
            

        

        
        ################
        rompath2 = rompath.replace(".smc", "_v2.smc")
        print("Copying %s -> %s" % (self.source_rom_abs_path, rompath2))
        shutil.copy(self.source_rom_abs_path, rompath2)
        print("File moved")
        ################
        
        
        
        rom2 = LocalRom(rompath2) # obsolete file=get_base_rom_path() for now, but later will need to use it somehow
        with open(basepatch_to_use, "rb") as f:
            delta: bytes = f.read()
        rom2.rom_data = bsdiff4.patch(rom2.rom_data, delta)        
        rom2.write_rom_data_to_file(rompath2)


        rom2.read_from_file(rom2.original_file)

        
        with open(r_patch_file,'r') as f:
            data = f.readlines()


            
        master = {}
        new_loc = 0
        for line in data:
            line = line.split(";")[0]
            print(line)
            if "org" not in line and "db" not in line:
                continue
            
            if "org" in line:
                new_loc = int(line.split("$")[1],base=16) - 12582912
                continue
            if "db" in line:
                each_byte = line.split(" ")[1:]
                each_byte = [i.replace(",","").replace("$","").strip() for i in each_byte if i]
                for b in each_byte:
                    if b:
                        master[new_loc] = int(b, base=16)
                        new_loc += 1
                    
                    
        
        for idx, b in master.items():
            rom2.buffer[idx] = b

        # dragon
        new_loc = int('C33320', base=16) - 12582912
        rom2.buffer[new_loc] = 0
        rom2.buffer[new_loc + 1] = 1
        rom2.buffer[new_loc + 2] = 0
        rom2.buffer[new_loc + 3] = 0
        
        b = data[-6].split("dw ")[1].split("\n")[0].replace("$","")
        b1 = b[:2]
        b2 = b[2:]


        
        for i in range(15):
            rom2.buffer[new_loc + 4 + i * 2] = int(b2,base=16)
            rom2.buffer[new_loc + 4 + i * 2 + 1] = int(b1,base=16)






        patch_rom(self.multiworld, rom2, self.player)
        
            
        rom2.write_to_file(rompath2)
        
        self.rom_name = rom.name
                

        print(rompath2)
            
                

        # patch = FFVCDDeltaPatch(os.path.splitext(rompath)[0]+FFVCDDeltaPatch.patch_file_ending, player=self.player,
        #                         player_name=self.multiworld.player_name[self.player], patched_path=rompath)
        
        # patch.write()
    
        # if os.path.exists(rompath):
        #     os.unlink(rompath)

        if os.path.exists(self.filename_randomized):
            os.unlink(self.filename_randomized)
        if os.path.exists(r_patch_file):
            os.unlink(r_patch_file)
        if os.path.exists(spoiler_file):
            os.unlink(spoiler_file)
        
        
        self.rom_name_available_event.set() # make sure threading continues and errors are collected
        print("Finished generate_output function")
        
        
    def modify_multidata(self, multidata: dict):
        # wait for self.rom_name to be available.
        self.rom_name_available_event.wait()
        rom_name = getattr(self, "rom_name", None)
        # we skip in case of error, so that the original error in the output thread is the one that gets raised
        if rom_name:
            new_name = base64.b64encode(bytes(self.rom_name)).decode()
            multidata["connect_names"][new_name] = multidata["connect_names"][self.multiworld.player_name[self.player]]
            
            
