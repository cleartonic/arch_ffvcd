import logging
import asyncio

from NetUtils import ClientStatus, color
from worlds.AutoSNIClient import SNIClient
from .locations import loc_id_start
from .items import item_table, arch_item_offset
from .rom import crystal_ram_data, magic_ram_data, ability_ram_data, item_ram_data, key_item_data
from .ram_watch_util import address_to_ram, ram_to_address, full_flag_dict

snes_logger = logging.getLogger("SNES")

# FXPAK Pro protocol memory mapping used by SNI
ROM_START = 0x000000
WRAM_START = 0xF50000
WRAM_SIZE = 0x20000
SRAM_START = 0xE00000

FFVCD_ROMNAME_START = 0x00FFC0
FFVCD_ROMHASH_START = 0x7FC0
ROMNAME_SIZE = 0x15
ROMHASH_SIZE = 0x15


FFVCD_EVENT_FLAG_ADDR = WRAM_START + 0x000A14
FFVCD_EVENT_FLAG_BRBLADE_CHKN_ADDR = WRAM_START + 0x001443
FFVCD_CHESTS_ADDR = WRAM_START + 0x0009D4


FFVCD_RECV_PROGRESS_ADDR = WRAM_START + 0x9F4
FFVCD_FILE_NAME_ADDR = WRAM_START + 0x5D9



class FFVCDSNIClient(SNIClient):
    game = "Final Fantasy V Career Day"
    async def deathlink_kill_player(self, ctx):
        pass
        # FFVCD_TODO: Handle Receiving Deathlink


    async def validate_rom(self, ctx):
        # print("Validating FFVCD rom")
        from SNIClient import snes_buffered_write, snes_flush_writes, snes_read

        rom_name = await snes_read(ctx, FFVCD_ROMHASH_START, ROMHASH_SIZE)
        
        # print("rom_name: %s" % rom_name)
        # if rom_name:
            # print("rom_name[:2]: %s" % (str(rom_name)[:2]))

        if rom_name is None or rom_name == bytes([0] * ROMHASH_SIZE) or rom_name[:2] != b"K7":
            # print("Fail validate_rom")
            return False
        
        # print("Pass validate_rom")
        ctx.game = self.game
        ctx.items_handling = 0b111  # remote items

        ctx.rom = rom_name
        return True


    async def game_watcher(self, ctx):
        from SNIClient import snes_buffered_write, snes_flush_writes, snes_read
        import base64

        
        
        
        ##############
        # EVENTS
        ##############
        d1 = await snes_read(ctx, FFVCD_EVENT_FLAG_ADDR, 0x100)
        # import pickle
        # with open('pickle.p', 'wb') as f:
        #     pickle.dump(d, f)

            
        ram_dict = {} 
        start = 'A14'
        for idx, entry in enumerate(d1):
            x1 = hex(int(str(start),base=16) + idx).replace("0x","").upper()
            if len(x1) == 3:
                x1 = "0%s" % x1
            ram_dict[x1] =    hex(entry).replace("0x","").upper()
        for k, v in ram_dict.items():
            if len(v) == 1:
                ram_dict[k] = "0%s" % v

        ##############
        # Brave Blade/Chicken Knife EVENT
        ##############
        d2 = await snes_read(ctx, FFVCD_EVENT_FLAG_BRBLADE_CHKN_ADDR, 0x01)


        start = '1443'
        for idx, entry in enumerate(d2):
            x1 = hex(int(str(start),base=16) + idx).replace("0x","").upper()
            if len(x1) == 3:
                x1 = "0%s" % x1
            ram_dict[x1] =    hex(entry).replace("0x","").upper()
        for k, v in ram_dict.items():
            if len(v) == 1:
                ram_dict[k] = "0%s" % v



        ##############
        # CHESTS
        ##############
        d3 = await snes_read(ctx, FFVCD_CHESTS_ADDR, 0x40)


        start = '9D4'
        for idx, entry in enumerate(d3):
            x1 = hex(int(str(start),base=16) + idx).replace("0x","").upper()
            if len(x1) == 3:
                x1 = "0%s" % x1
            ram_dict[x1] =    hex(entry).replace("0x","").upper()
        for k, v in ram_dict.items():
            if len(v) == 1:
                ram_dict[k] = "0%s" % v
                
                
                    
            

        # import pickle
        # with open('pickle.p', 'wb') as f:
        #     pickle.dump(d4, f)

                
                
                
        def check_status_bits(ram_bit, loc_bit, direction):
            if direction == "ON":
                return int(ram_bit, base=16) & int(loc_bit, base=16) != 0
            elif direction == "OFF":
                return int(ram_bit, base=16) & int(loc_bit, base=16) == 0
                
                
        def hex_or_return_int(a, b):
            return min(int(a,base=16) | int(b, base=16), 255)
        def hex_xor_return_int(a, b):
            return min(int(a,base=16) ^ int(b, base=16), 255)
        def hex_and_return_int(a, b):
            return min(int(a,base=16) & int(b, base=16), 255)
                
                
        def convert_int_to_two_bytes_as_list(i):
            return [i % 256, i // 256]
        def convert_two_bytes_to_int(a, b):
            return a + b * 256

        new_checks = []
        for event_flag_addr, event_flag_data in full_flag_dict.items():
            try:
                ram_byte = event_flag_data['byte']
                ram_bit = ram_dict[ram_byte]
                loc_bit = event_flag_data['bit']
                direction = event_flag_data['direction']
                loc_id = int(event_flag_addr,base=16) + loc_id_start
                status = check_status_bits(ram_bit, loc_bit, direction)
                if loc_id not in ctx.locations_checked and status:
                    new_checks.append(loc_id)
                # print("%s%s" % ("{:<60}".format(event_flag_data['name']), status))
            except Exception as e:
                print(e)    
                

        for new_check_id in new_checks:
            ctx.locations_checked.add(new_check_id)
            location = ctx.location_names[new_check_id]
            snes_logger.info(
                f'New Check: {location} ({len(ctx.locations_checked)}/{len(ctx.missing_locations) + len(ctx.checked_locations)})')
            await ctx.send_msgs([{"cmd": 'LocationChecks', "locations": [new_check_id]}])

        recv_count = await snes_read(ctx, FFVCD_RECV_PROGRESS_ADDR, 2)
        recv_index = convert_two_bytes_to_int(recv_count[0], recv_count[1])

        print("recv_index %s -> items_received %s" % (recv_index, len(ctx.items_received)))
        if recv_index < len(ctx.items_received):
            item = ctx.items_received[recv_index]
            recv_index += 1
            logging.info('Received %s from %s (%s) (%d/%d in list)' % (
                color(ctx.item_names[item.item], 'red', 'bold'),
                color(ctx.player_names[item.player], 'yellow'),
                ctx.location_names[item.location], recv_index, len(ctx.items_received)))

            recv_index_list = convert_int_to_two_bytes_as_list(recv_index)
            print("Writing bytes recv_index %s to %s -> %s" % (FFVCD_RECV_PROGRESS_ADDR, recv_index_list, bytes(recv_index_list)))
            snes_buffered_write(ctx, FFVCD_RECV_PROGRESS_ADDR, bytes(recv_index_list))
            
            arch_item_id = item.item - arch_item_offset
            print(arch_item_id)
            
            print("This game's slot %s -> item player %s" % (ctx.slot, item.player))
            

            ####################            
            # RECEIVE CRYSTALS
            ####################
            
            if arch_item_id in crystal_ram_data.keys():
                crystal_data = crystal_ram_data[arch_item_id]
                crystal_data_bit, crystal_data_ram_addr = crystal_data
                
                current_bit = await snes_read(ctx, WRAM_START + crystal_data_ram_addr, 0x01)
                new_bit = hex_or_return_int(hex(current_bit[0]), crystal_data_bit)
                snes_buffered_write(ctx, WRAM_START + crystal_data_ram_addr, bytes([new_bit]))
                print("Write crystal")
                    
            ####################            
            # RECEIVE MAGIC
            ####################
            
            if arch_item_id in magic_ram_data.keys():
                magic_data = magic_ram_data[arch_item_id]
                magic_data_bit, magic_data_ram_addr = magic_data
                
                current_bit = await snes_read(ctx, WRAM_START + magic_data_ram_addr, 0x01)
                new_bit = hex_or_return_int(hex(current_bit[0]), magic_data_bit)
                snes_buffered_write(ctx, WRAM_START + magic_data_ram_addr, bytes([new_bit]))
                print("Write magic")
                    
            ####################            
            # RECEIVE ABILITY
            ####################
            
            if arch_item_id in ability_ram_data.keys():
                ability_data = ability_ram_data[arch_item_id]
                ability_data_bit, ability_data_ram_addr = ability_data
                
                current_bit = await snes_read(ctx, WRAM_START + ability_data_ram_addr, 0x01)
                new_bit = hex_or_return_int(hex(current_bit[0]), ability_data_bit)
                snes_buffered_write(ctx, WRAM_START + ability_data_ram_addr, bytes([new_bit]))
                print("Write ability 1")

                current_bit = await snes_read(ctx, WRAM_START + ability_data_ram_addr + 0x14, 0x01)
                new_bit = hex_or_return_int(hex(current_bit[0]), ability_data_bit)
                snes_buffered_write(ctx, WRAM_START + ability_data_ram_addr + 0x14, bytes([new_bit]))
                print("Write ability 2")

                current_bit = await snes_read(ctx, WRAM_START + ability_data_ram_addr + 0x28, 0x01)
                new_bit = hex_or_return_int(hex(current_bit[0]), ability_data_bit)
                snes_buffered_write(ctx, WRAM_START + ability_data_ram_addr + 0x28, bytes([new_bit]))
                print("Write ability 3")

                current_bit = await snes_read(ctx, WRAM_START + ability_data_ram_addr + 0x3C, 0x01)
                new_bit = hex_or_return_int(hex(current_bit[0]), ability_data_bit)
                snes_buffered_write(ctx, WRAM_START + ability_data_ram_addr + 0x3C, bytes([new_bit]))
                print("Write ability 4")
                    
            ##############
            # RECEIVE ITEMS
            ##############
            
            
            # If items are found in own world, do not award via this method
            # This prevents getting 2 rewards (one in game, one from server)
            # All other types of rewards are fine for getting 2 of technically
            
            # if you want to skip own items for stuff like weapons/armor etc, use below
            
            if ctx.slot == item.player:
                pass
                # print("Self item, skip")
                
            else:
                if arch_item_id in item_ram_data.keys():
                    d4 = await snes_read(ctx, WRAM_START + 0x640, 0x100)
            
                    ram_current_item_map = {}
                    
                    for idx, i in enumerate(d4):
                        ram_current_item_map[idx] = hex(i).replace("0x","").upper()
                    
                    for k, v in ram_current_item_map.items():
                        if len(v) == 1:
                            ram_current_item_map[k] = "0%s" % v
                            
                    new_item_byte = item_ram_data[arch_item_id]
                    
                    match_idx = None
                    for k, v in ram_current_item_map.items():
                        if v == new_item_byte:
                            match_idx = k
                            break
                            
                    if match_idx:
                        # if a match was found, find its corresponding inventory count then add 1
                        item_count_in_inventory = await snes_read(ctx, WRAM_START + 0x740 + match_idx, 0x01)
                        item_count_in_inventory = min(item_count_in_inventory[0] + 1, 99)
                        snes_buffered_write(ctx, WRAM_START + 0x740 + match_idx, bytes([item_count_in_inventory]))
                    else:
                        # if a match was not found, find the first 00 slot in inventory ids, then assign it and give it 1 count
                        new_item_idx = None
                        for k, v in ram_current_item_map.items():
                            if v == '00':
                                new_item_idx = k
                                break
                        
                        if new_item_idx:
                            # this should always be true, or else something real bad is happening in inventory >_>;....
                            print("Adding new item %s at %s" % (new_item_byte, WRAM_START + 0x640 + new_item_idx))
                            snes_buffered_write(ctx, WRAM_START + 0x640 + new_item_idx, bytes([int(new_item_byte,base=16)]))
                            snes_buffered_write(ctx, WRAM_START + 0x740 + new_item_idx, bytes([1]))
                        else:
                            pass
                            print("Could not create for %s " % new_item_byte)


            ####################            
            # RECEIVE KEY ITEMS
            ####################
            
            if arch_item_id in key_item_data.keys():
                key_item_data_entries = key_item_data[arch_item_id]
                
                if arch_item_id != 1005 and arch_item_id != 1006:    
                    for key_item_data_entry in key_item_data_entries:
                        key_item_bit, key_item_addr_offset, key_item_direction = key_item_data_entry

                        current_bit = await snes_read(ctx, WRAM_START + 0xA00 + key_item_addr_offset, 0x01)
                        if key_item_direction == "ON":
                            new_bit = hex_or_return_int(hex(current_bit[0]), key_item_bit)
                        elif key_item_direction == "OFF":
                            new_bit = hex_xor_return_int(hex(current_bit[0]), key_item_bit)
                        else:
                            break
                            
                        snes_buffered_write(ctx, WRAM_START + 0xA00 + key_item_addr_offset, bytes([new_bit]))
                        print("Write key item")

                elif arch_item_id == 1005 or arch_item_id == 1006:   # handle hiryuu / submarine
                    # first handle key item for menu text
                    key_item_bit, key_item_addr_offset, key_item_direction = key_item_data_entries[0]
                    current_bit = await snes_read(ctx, WRAM_START + 0xA00 + key_item_addr_offset, 0x01)
                    new_bit = hex_or_return_int(hex(current_bit[0]), key_item_bit)
                    snes_buffered_write(ctx, WRAM_START + 0xA00 + key_item_addr_offset, bytes([new_bit]))
                    print("Write key item")
                    
                    # then handle coords writing
                    for key_item_data_entry in key_item_data_entries[1:]:
                        key_item_byte, key_item_addr_offset, key_item_direction = key_item_data_entry
                        snes_buffered_write(ctx, WRAM_START + 0xA00 + key_item_addr_offset, bytes([int(key_item_byte,base=16)]))
                        print("Write key item")
                        
            await snes_flush_writes(ctx)
                    
                    
        return 
    
    
    
        
        
        
        
        
        
        
        
        save_file_name = await snes_read(ctx, FFVCD_FILE_NAME_ADDR, 0x5)
        if save_file_name is None or save_file_name[0] == 0x00 or save_file_name == bytes([0x55] * 0x05):
            # We haven't loaded a save file
            return

        new_checks = []
        from worlds.FFVCD.Rom import location_rom_data, item_rom_data, boss_location_ids, level_unlock_map
        location_ram_data = await snes_read(ctx, WRAM_START + 0x5FE, 0x81)
        for loc_id, loc_data in location_rom_data.items():
            if loc_id not in ctx.locations_checked:
                data = location_ram_data[loc_data[0] - 0x5FE]
                masked_data = data & (1 << loc_data[1])
                bit_set = (masked_data != 0)
                invert_bit = ((len(loc_data) >= 3) and loc_data[2])
                if bit_set != invert_bit:
                    # FFVCD_TODO: Handle non-included checks
                    new_checks.append(loc_id)

        verify_save_file_name = await snes_read(ctx, FFVCD_FILE_NAME_ADDR, 0x5)
        if verify_save_file_name is None or verify_save_file_name[0] == 0x00 or verify_save_file_name == bytes([0x55] * 0x05) or verify_save_file_name != save_file_name:
            # We have somehow exited the save file (or worse)
            ctx.rom = None
            return

        rom = await snes_read(ctx, FFVCD_ROMHASH_START, ROMHASH_SIZE)
        if rom != ctx.rom:
            ctx.rom = None
            # We have somehow loaded a different ROM
            return

        for new_check_id in new_checks:
            ctx.locations_checked.add(new_check_id)
            location = ctx.location_names[new_check_id]
            snes_logger.info(
                f'New Check: {location} ({len(ctx.locations_checked)}/{len(ctx.missing_locations) + len(ctx.checked_locations)})')
            await ctx.send_msgs([{"cmd": 'LocationChecks', "locations": [new_check_id]}])

        # FFVCD_TODO: Make this actually visually display new things received (ASM Hook required)
        recv_count = await snes_read(ctx, FFVCD_RECV_PROGRESS_ADDR, 1)
        recv_index = recv_count[0]

        if recv_index < len(ctx.items_received):
            item = ctx.items_received[recv_index]
            recv_index += 1
            logging.info('Received %s from %s (%s) (%d/%d in list)' % (
                color(ctx.item_names[item.item], 'red', 'bold'),
                color(ctx.player_names[item.player], 'yellow'),
                ctx.location_names[item.location], recv_index, len(ctx.items_received)))

            snes_buffered_write(ctx, FFVCD_RECV_PROGRESS_ADDR, bytes([recv_index]))
            if item.item in item_rom_data:
                item_count = await snes_read(ctx, WRAM_START + item_rom_data[item.item][0], 0x1)
                new_item_count = item_count[0] + 1
                for address in item_rom_data[item.item]:
                    snes_buffered_write(ctx, WRAM_START + address, bytes([new_item_count]))

                # Handle Coin Displays
                current_level = await snes_read(ctx, WRAM_START + 0x5E3, 0x5)
                overworld_locked = ((await snes_read(ctx, WRAM_START + 0x5FC, 0x1))[0] == 0x01)
                if item.item == 0xDC3002 and not overworld_locked and (current_level[0] == 0x0A and current_level[2] == 0x00 and current_level[4] == 0x03):
                    # Bazaar and Barter
                    item_count = await snes_read(ctx, WRAM_START + 0xB02, 0x1)
                    new_item_count = item_count[0] + 1
                    snes_buffered_write(ctx, WRAM_START + 0xB02, bytes([new_item_count]))
                elif item.item == 0xDC3002 and not overworld_locked and current_level[0] == 0x04:
                    # Swanky
                    item_count = await snes_read(ctx, WRAM_START + 0xA26, 0x1)
                    new_item_count = item_count[0] + 1
                    snes_buffered_write(ctx, WRAM_START + 0xA26, bytes([new_item_count]))
                elif item.item == 0xDC3003 and not overworld_locked and (current_level[0] == 0x0A and current_level[2] == 0x08 and current_level[4] == 0x01):
                    # Boomer
                    item_count = await snes_read(ctx, WRAM_START + 0xB02, 0x1)
                    new_item_count = item_count[0] + 1
                    snes_buffered_write(ctx, WRAM_START + 0xB02, bytes([new_item_count]))
            else:
                # Handle Patch and Skis
                if item.item == 0xDC3007:
                    num_upgrades = 1
                    inventory = await snes_read(ctx, WRAM_START + 0x605, 0xF)

                    if (inventory[0] & 0x02):
                        num_upgrades = 3
                    elif (inventory[13] & 0x08) or (inventory[0] & 0x01):
                        num_upgrades = 2

                    if num_upgrades == 1:
                        snes_buffered_write(ctx, WRAM_START + 0x605, bytes([inventory[0] | 0x01]))
                        if inventory[4] == 0:
                            snes_buffered_write(ctx, WRAM_START + 0x609, bytes([0x01]))
                        elif inventory[6] == 0:
                            snes_buffered_write(ctx, WRAM_START + 0x60B, bytes([0x01]))
                        elif inventory[8] == 0:
                            snes_buffered_write(ctx, WRAM_START + 0x60D, bytes([0x01]))
                        elif inventory[10] == 0:
                            snes_buffered_write(ctx, WRAM_START + 0x60F, bytes([0x01]))

                        cove_mekanos_progress = await snes_read(ctx, WRAM_START + 0x691, 0x2)
                        snes_buffered_write(ctx, WRAM_START + 0x691, bytes([cove_mekanos_progress[0] | 0x01]))
                        snes_buffered_write(ctx, WRAM_START + 0x692, bytes([cove_mekanos_progress[1] | 0x01]))
                    elif num_upgrades == 2:
                        snes_buffered_write(ctx, WRAM_START + 0x605, bytes([inventory[0] | 0x02]))
                        if inventory[4] == 0:
                            snes_buffered_write(ctx, WRAM_START + 0x609, bytes([0x02]))
                        elif inventory[6] == 0:
                            snes_buffered_write(ctx, WRAM_START + 0x60B, bytes([0x02]))
                        elif inventory[8] == 0:
                            snes_buffered_write(ctx, WRAM_START + 0x60D, bytes([0x02]))
                        elif inventory[10] == 0:
                            snes_buffered_write(ctx, WRAM_START + 0x60F, bytes([0x02]))
                    elif num_upgrades == 3:
                        snes_buffered_write(ctx, WRAM_START + 0x606, bytes([inventory[1] | 0x20]))

                        k3_ridge_progress = await snes_read(ctx, WRAM_START + 0x693, 0x2)
                        snes_buffered_write(ctx, WRAM_START + 0x693, bytes([k3_ridge_progress[0] | 0x01]))
                        snes_buffered_write(ctx, WRAM_START + 0x694, bytes([k3_ridge_progress[1] | 0x01]))
                elif item.item == 0xDC3000:
                    # Handle Victory
                    if not ctx.finished_game:
                        await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
                        ctx.finished_game = True
                else:
                    print("Item Not Recognized: ", item.item)
                pass

            await snes_flush_writes(ctx)

        # Handle Collected Locations
        levels_to_tiles = await snes_read(ctx, ROM_START + 0x3FF800, 0x60)
        tiles_to_levels = await snes_read(ctx, ROM_START + 0x3FF860, 0x60)
        for loc_id in ctx.checked_locations:
            if loc_id not in ctx.locations_checked and loc_id not in boss_location_ids:
                loc_data = location_rom_data[loc_id]
                data = await snes_read(ctx, WRAM_START + loc_data[0], 1)
                invert_bit = ((len(loc_data) >= 3) and loc_data[2])
                if not invert_bit:
                    masked_data = data[0] | (1 << loc_data[1])
                    snes_buffered_write(ctx, WRAM_START + loc_data[0], bytes([masked_data]))

                    if (loc_data[1] == 1):
                        # Make the next levels accessible
                        level_id = loc_data[0] - 0x632
                        tile_id = levels_to_tiles[level_id] if levels_to_tiles[level_id] != 0xFF else level_id
                        tile_id = tile_id + 0x632
                        if tile_id in level_unlock_map:
                            for next_level_address in level_unlock_map[tile_id]:
                                next_level_id = next_level_address - 0x632
                                next_tile_id = tiles_to_levels[next_level_id] if tiles_to_levels[next_level_id] != 0xFF else next_level_id
                                next_tile_id = next_tile_id + 0x632
                                next_data = await snes_read(ctx, WRAM_START + next_tile_id, 1)
                                snes_buffered_write(ctx, WRAM_START + next_tile_id, bytes([next_data[0] | 0x01]))

                    await snes_flush_writes(ctx)
                else:
                    masked_data = data[0] & ~(1 << loc_data[1])
                    snes_buffered_write(ctx, WRAM_START + loc_data[0], bytes([masked_data]))
                    await snes_flush_writes(ctx)
                ctx.locations_checked.add(loc_id)

        # Calculate Boomer Cost Text
        boomer_cost_text = await snes_read(ctx, WRAM_START + 0xAAFD, 2)
        if boomer_cost_text[0] == 0x31 and boomer_cost_text[1] == 0x35:
            boomer_cost = await snes_read(ctx, ROM_START + 0x349857, 1)
            boomer_cost_tens = int(boomer_cost[0]) // 10
            boomer_cost_ones = int(boomer_cost[0]) % 10
            snes_buffered_write(ctx, WRAM_START + 0xAAFD, bytes([0x30 + boomer_cost_tens, 0x30 + boomer_cost_ones]))
            await snes_flush_writes(ctx)

        boomer_final_cost_text = await snes_read(ctx, WRAM_START + 0xAB9B, 2)
        if boomer_final_cost_text[0] == 0x32 and boomer_final_cost_text[1] == 0x35:
            boomer_cost = await snes_read(ctx, ROM_START + 0x349857, 1)
            boomer_cost_tens = boomer_cost[0] // 10
            boomer_cost_ones = boomer_cost[0] % 10
            snes_buffered_write(ctx, WRAM_START + 0xAB9B, bytes([0x30 + boomer_cost_tens, 0x30 + boomer_cost_ones]))
            await snes_flush_writes(ctx)
