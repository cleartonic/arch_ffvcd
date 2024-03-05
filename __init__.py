import os
import threading
import base64
from BaseClasses import MultiWorld, Tutorial, ItemClassification
from worlds.AutoWorld import World, WebWorld
from .items import item_table, item_groups, create_item, create_world_items, arch_item_offset, \
    WORLD2_ACCESS_ITEM_ID, WORLD3_ACCESS_ITEM_ID
from .locations import location_data, loc_id_start
from .options import ffvcd_options
from .regions import create_regions
from .rules import set_rules
from worlds.ffvcd.ffvcd_arch.utilities.data import conductor
from .client import FFVCDSNIClient
from .rom import LocalRom, get_base_rom_path, patch_rom, FFVCDDeltaPatch
from collections import Counter
import shutil
import logging
import pkgutil
from Fill import fill_restrictive

logger = logging.getLogger("Final Fantasy V Career Day")

THIS_FILEPATH = os.path.dirname(__file__)

# lots of credit to others in the repository, such as pokemonrb, dkc3 and tloz

class FFVCDWebWorld(WebWorld):
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to playing Final Fantasy V Career Day with Archipelago.",
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
    starting_crystals = None # passed to conductor later

    
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
        self.world_lock = self.multiworld.world_lock[self.player].value + 1
        
        if self.world_lock == 2:
            new_item = create_item("World 2 Access (Item)",  
                        ItemClassification.progression, 
                        WORLD2_ACCESS_ITEM_ID + arch_item_offset, 
                        self.player, ['World Access'])
            self.starting_items[new_item] = 1
            self.multiworld.push_precollected(new_item)
        if self.world_lock == 3:
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

        self.starting_crystals = create_world_items(self)
        
        # state = self.multiworld.get_all_state(False)
        
        
        # locations_to_place_this_world = [self.multiworld.get_location("Carwen - Lone Wolf Barrel (Cabin)"\
        #                                                               ,self.player),
        #                                  self.multiworld.get_location("Bal Castle - Lone Wolf Chest (Thunder Whip)"\
        #                                                               ,self.player)]

        # items_to_place = self.random.sample([i for i in self.multiworld.itempool if i.player == self.player \
        #                                      and not i.advancement], len(locations_to_place_this_world))
        
        # for item in items_to_place:
        #     state.remove(item)
        #     self.multiworld.itempool.remove(item)

        # for attempts_remaining in range(2, -1, -1):
        #     fill_restrictive(self.multiworld, state, locations_to_place_this_world, items_to_place,
        #                      single_player_placement=True, lock=True, allow_excluded=True)

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
        options_conductor['world_lock'] = self.world_lock
        options_conductor['player'] = self.player
        
        self.options_conductor = options_conductor
        
        options_conductor['starting_crystals'] = self.starting_crystals
            
        return options_conductor
                
    def create_regions(self):
        create_regions(self.multiworld, self.player)

    def generate_output(self, output_directory: str):
        
        locs = [i for i in self.multiworld.get_locations(self.player)]
        data = {}
        
        for loc in locs:
            if loc.address:
                lname = loc.item.name
                data[hex(loc.address - loc_id_start).replace("0x","").upper()] = {'loc_name' : lname,
                                                                   'loc_player' : loc.item.player,
                                                                   'loc_progression' : loc.item.advancement}

        
        options_conductor = self.parse_options_for_conductor()

        
        self.cond = conductor.Conductor(self.multiworld.per_slot_randoms[self.player], options_conductor, arch_data = data, \
                                        player = self.player, seed = self.multiworld.seed)

        self.cond.randomize()
        

        # move 
        temp_patch_path = self.cond.save_patch(output_directory)
        self.filename_randomized = self.cond.patch_file(output_directory)

        rompath = os.path.join(output_directory, f"{self.multiworld.get_out_file_name_base(self.player)}.smc")

        ################
        # new system
        ################
        four_job = "" if self.options_conductor['four_job'] else 'no'
        basepatch_to_use = os.path.join('ffvcd_arch', 
                                        'process',
                                        'basepatch',
                                        "ffv_%sfjf_world%slock.bsdiff4" % (four_job,
                                                              self.options_conductor['world_lock'])
                                        )
        logger.debug("Copying %s -> %s" % (self.source_rom_abs_path, rompath))        
        shutil.copy(self.source_rom_abs_path, rompath)
        rom = LocalRom(rompath)
        rom.write_randomizer_asm_to_file(basepatch_to_use, temp_patch_path, rompath)
        patch_rom(self.multiworld, rom, self.player)
        self.rom_name = rom.name
        rom.write_to_file(rompath)


        patch = FFVCDDeltaPatch(os.path.splitext(rompath)[0]+FFVCDDeltaPatch.patch_file_ending, player=self.player,
                                player_name=self.multiworld.player_name[self.player], patched_path=rompath)
        
        patch.write()
    
        if os.path.exists(rompath):
            os.unlink(rompath)

        if os.path.exists(self.filename_randomized):
            os.unlink(self.filename_randomized)
            
        if os.path.exists(temp_patch_path):
            os.unlink(temp_patch_path)
        
        self.rom_name_available_event.set() # make sure threading continues and errors are collected
        logger.debug("Finished generate_output function")
        
        
    def modify_multidata(self, multidata: dict):
        # wait for self.rom_name to be available.
        self.rom_name_available_event.wait()
        rom_name = getattr(self, "rom_name", None)
        # we skip in case of error, so that the original error in the output thread is the one that gets raised
        if rom_name:
            new_name = base64.b64encode(bytes(self.rom_name)).decode()
            multidata["connect_names"][new_name] = multidata["connect_names"][self.multiworld.player_name[self.player]]
            
        
    def write_spoiler(self, spoiler_handle) -> None:
        output = '\n----------------------------------------\n\
FINAL FANTASY V: CAREER DAY ARCHIPELAGO\nPlayer: %s\n\
----------------------------------------\n' % (self.player)
        
        data = output + self.cond.spoiler
        spoiler_handle.write(data)