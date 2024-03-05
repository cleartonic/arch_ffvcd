from BaseClasses import Location
from BaseClasses import ItemClassification
from worlds.generic.Rules import add_item_rule
from .items import arch_item_offset
loc_id_start = 342000000



class LocationData:
    def __init__(self, name, address = None, parent = None, area = None, location_type="", type="Item"):
        self.name = name
        try:
            self.address = address + loc_id_start
        except:
            print("No address for %s" % name)
            self.address = None
        self.address_hex = address
        self.parent = parent
        self.area = area
        self.location_type = location_type
        self.type = type

class FFVCDLocation(Location):
    game = "ffvcd"

    def __init__(self, player, location_data, parent=None, progression_checks_setting = 0):
        super(FFVCDLocation, self).__init__(
            player, location_data.name,
            location_data.address,
            parent
        )
        
        self.item_rule = lambda x: True
        
        
        # when progression_checks_setting == 0, this is the "bosses" setting
        # meaning only bosses will give progression checks
        
        # if progression_checks_setting == 1, then the following rule does not need
        # to be applied        
        if not progression_checks_setting:
            if location_data.location_type != "key":
                add_item_rule(self, lambda item: not (item.classification & ItemClassification.progression))


        
        
        # disallow lone wolf/under bal castle related checks for some weird progression problems

        # if location_data.address - loc_id_start in [0xC0FB38, 0xC0FB3A]:
        #     add_item_rule(self, lambda item: item.player == self.player)

        # kuzar shouldn't have key items because of the permanent choice of using tablets
        # mua shouldn't have key items because of chicken knife/brave blade
        # void shouldn't have key items because of ragnarok chest/too late in the game
        if location_data.area in ["Kuzar", "Mua", "Void"]:
            add_item_rule(self, lambda item: not (item.classification & ItemClassification.progression))



        # the fire crystal post-karnak cutscene should only give non-item rewards
        # this event is retriggerable, so giving multiple items would be 'cheap'
        # but forcing anything else on to these rewards is fine, because they
        # will simply overwrite/update (magic, abilities, crystals)
        # they can be other players' items too
        # they just can't be this world's own ITEMS 
        
        # this needs to be fixed - you cannot use other definitions in item class 
        # because its shared across world
        # it doesnt belong as an item rule 

        # if "fire crystal" in location_data.name.lower():
        #     add_item_rule(self, lambda item: not ('Item' in item.groups))

            


        # gil cannot be on events
        # item ids 900-999 are gil 
        if location_data.location_type == "event" or location_data.location_type == "key":
            add_item_rule(self, lambda item: not ((item.code - arch_item_offset) > 900 and \
                                                  (item.code - arch_item_offset) < 999))

        
            


def create_location(world, player, location_data, parent=None):
    progression_checks_setting = world.progression_checks[player].value
    return_location = FFVCDLocation(player, location_data, parent, progression_checks_setting)
    return return_location

location_data = [

LocationData("Wind Shrine - Wind Crystal (Knight)", address = 0xC0FAB2, area = "Wind Shrine", location_type="event"),
LocationData("Wind Shrine - Wind Crystal (BlueMage)", address = 0xC0FAB4, area = "Wind Shrine", location_type="event"),
LocationData("Wind Shrine - Wind Crystal (BlackMage)", address = 0xC0FAB6, area = "Wind Shrine", location_type="event"),
LocationData("Wind Shrine - Wind Crystal (WhiteMage)", address = 0xC0FAB8, area = "Wind Shrine", location_type="event"),
LocationData("Wind Shrine - Wind Crystal (Monk)", address = 0xC0FABA, area = "Wind Shrine", location_type="event"),
LocationData("Wind Shrine - Wind Crystal (Thief)", address = 0xC0FABC, area = "Wind Shrine", location_type="event"),
LocationData("Karnak - Fire Crystal (Trainer)", address = 0xC0FABE, area = "Karnak", location_type="event"),
LocationData("Karnak - Fire Crystal (Geomancer)", address = 0xC0FAC0, area = "Karnak", location_type="event"),
LocationData("Karnak - Fire Crystal (Ninja)", address = 0xC0FAC2, area = "Karnak", location_type="event"),
LocationData("Crescent Island - Black Choco Crystals (Bard)", address = 0xC0FAC4, area = "Crescent Island", location_type="event"),
LocationData("Crescent Island - Black Choco Crystals (Hunter)", address = 0xC0FAC6, area = "Crescent Island", location_type="event"),
LocationData("Flying Lonka Ruins - Earth Crystal (Samurai)", address = 0xC0FAC8, area = "Flying Lonka Ruins", location_type="event"),
LocationData("Flying Lonka Ruins - Earth Crystal (Dragoon)", address = 0xC0FACA, area = "Flying Lonka Ruins", location_type="event"),
LocationData("Flying Lonka Ruins - Earth Crystal (Chemist)", address = 0xC0FACC, area = "Flying Lonka Ruins", location_type="event"),
LocationData("Flying Lonka Ruins - Earth Crystal (Dancer)", address = 0xC0FACE, area = "Flying Lonka Ruins", location_type="event"),
LocationData("Istory Falls - Leviathan Esper (Levia)", address = 0xC0FAD0, area = "Istory Falls", location_type="event"),
LocationData("Karnak Meteor - Titan (Titan)", address = 0xC0FAD2, area = "Karnak Meteor", location_type="event"),
LocationData("Exdeath's Castle - Carbuncle (Crbnkl)", address = 0xC0FAD4, area = "Exdeath's Castle", location_type="event"),
LocationData("Pirate's Cave - Syldra (Syldra)", address = 0xC0FAD6, area = "Pirate's Cave", location_type="event"),
LocationData("Bal Castle Lower - Odin (Odin)", address = 0xC0FAD8, area = "Bal Castle Lower", location_type="event"),
LocationData("Phoenix Tower - Phoenix (Phenix)", address = 0xC0FADA, area = "Phoenix Tower", location_type="event"),
LocationData("North Mountain (World 3) - Bahamut (Bahmut)", address = 0xC0FADC, area = "North Mountain (World 3)", location_type="event"),
LocationData("Crescent Island - Life Song (Vitality)", address = 0xC0FADE, area = "Crescent Island", location_type="event"),
LocationData("Lix - Temptation Song at Lix (Charm)", address = 0xC0FAE0, area = "Lix", location_type="event"),
LocationData("Istory - Love Song at Istory (Love)", address = 0xC0FAE2, area = "Istory", location_type="event"),
LocationData("Kelb - Requiem Song at Kelb (Requiem)", address = 0xC0FAE4, area = "Kelb", location_type="event"),
LocationData("Surgate Castle - Speed Song at Surgate (Speed)", address = 0xC0FAE6, area = "Surgate Castle", location_type="event"),
LocationData("Ancient Library (World 3) - Magic Song at Ancient Library (Magic)", address = 0xC0FAE8, area = "Ancient Library (World 3)", location_type="event"),
LocationData("Crescent Island - Power Song from Crescent Town (Power)", address = 0xC0FAEA, area = "Crescent Island", location_type="event"),
LocationData("Crescent Island - Hero Song from Crescent Town (Hero)", address = 0xC0FAEC, area = "Crescent Island", location_type="event"),
LocationData("Fork Tower - Fork Tower, two Magics (Holy)", address = 0xC0FAEE, area = "Fork Tower", location_type="event"),
LocationData("Fork Tower - Fork Tower, two Magics (Flare)", address = 0xC0FAF0, area = "Fork Tower", location_type="event"),
LocationData("Great Trench - Meteo (Meteo)", address = 0xC0FAF2, area = "Great Trench", location_type="event"),
LocationData("Wind Shrine - 5 potions (from NPC) (Potion)", address = 0xC0FAF4, area = "Wind Shrine", location_type="event"),
LocationData("Pirate's Cave - 8 potions (from NPC) (Potion)", address = 0xC0FAF6, area = "Pirate's Cave", location_type="event"),
LocationData("Tycoon Castle - Chancellor at Tycoon (Healing Staff)", address = 0xC0FAF8, area = "Tycoon Castle", location_type="event"),
LocationData("North Mountain - Magisa & Forza (Mythril Helm)", address = 0xC0FAFA, area = "North Mountain", location_type="event"),
LocationData("Kelb - CornaJar at Kelb (CornaJar)", address = 0xC0FAFC, area = "Kelb", location_type="event"),
LocationData("Rugor - Ribbon from girl in Rugor (Ribbon)", address = 0xC0FAFE, area = "Rugor", location_type="event"),
LocationData("Kuzar - 12 Kuzar Events (Excalibur)", address = 0xC0FB06, area = "Kuzar", location_type="event"),
LocationData("Kuzar - 12 Kuzar Events (Assassin)", address = 0xC0FB02, area = "Kuzar", location_type="event"),
LocationData("Kuzar - 12 Kuzar Events (Hardened Dagger)", address = 0xC0FB16, area = "Kuzar", location_type="event"),
LocationData("Kuzar - 12 Kuzar Events (Holy Lance)", address = 0xC0FB0C, area = "Kuzar", location_type="event"),
LocationData("Kuzar - 12 Kuzar Events (Rune Axe)", address = 0xC0FB12, area = "Kuzar", location_type="event"),
LocationData("Kuzar - 12 Kuzar Events (Masamune)", address = 0xC0FB0E, area = "Kuzar", location_type="event"),
LocationData("Kuzar - 12 Kuzar Events (Yoichi Bow)", address = 0xC0FB18, area = "Kuzar", location_type="event"),
LocationData("Kuzar - 12 Kuzar Events (Flame Whip)", address = 0xC0FB08, area = "Kuzar", location_type="event"),
LocationData("Kuzar - 12 Kuzar Events (Sage's Staff)", address = 0xC0FB14, area = "Kuzar", location_type="event"),
LocationData("Kuzar - 12 Kuzar Events (Wizard Rod)", address = 0xC0FB10, area = "Kuzar", location_type="event"),
LocationData("Kuzar - 12 Kuzar Events (Apollo's Harp)", address = 0xC0FB04, area = "Kuzar", location_type="event"),
LocationData("Kuzar - 12 Kuzar Events (Earth Bell)", address = 0xC0FB0A, area = "Kuzar", location_type="event"),
LocationData("Walse Castle - Shiva (Shiva)", address = 0xC0FB1A, area = "Walse Castle", location_type="event"),
LocationData("Ancient Library - Ifrit (Ifrit)", address = 0xC0FB1C, area = "Ancient Library", location_type="event"),
LocationData("Walse Tower - Water Crystal (RedMage)", address = 0xC0FB1E, area = "Walse Tower", location_type="event"),
LocationData("Walse Tower - Water Crystal (Berserker)", address = 0xC0FB20, area = "Walse Tower", location_type="event"),
LocationData("Walse Tower - Water Crystal (MysticKnight)", address = 0xC0FB22, area = "Walse Tower", location_type="event"),
LocationData("Walse Tower - Water Crystal (TimeMage)", address = 0xC0FB24, area = "Walse Tower", location_type="event"),
LocationData("Walse Tower - Water Crystal (Summoner)", address = 0xC0FB26, area = "Walse Tower", location_type="event"),
LocationData("Mua - Secret Area (Brave Blade/Chicken Knife)", address = 0xC0FB28, area = "Mua", location_type="event"),
LocationData("Tycoon Castle - Tycoon Castle Cabin (Cabin (1))", address = 0xC0FB2C, area = "Tycoon Castle", location_type="event"),
LocationData("Tycoon Castle - Tycoon Castle Cabin (Cabin (2))", address = 0xC0FB2E, area = "Tycoon Castle", location_type="event"),
LocationData("Walse Tower Sunken - Walse Tower Chest (GoGo)", address = 0xC0FB30, area = "Walse Tower Sunken", location_type="event"),
LocationData("Pyramid - Pyramid Top (Pyramid Tablet)", address = 0xC0FB32, area = "Pyramid", location_type="event"),
LocationData("Istory Falls - Toad Event (Toad)", address = 0xC0FB34, area = "Istory Falls", location_type="event"),
LocationData("Mua - Aegis Shield Chest (Aegis Shield)", address = 0xC0FB36, area = "Mua", location_type="event"),
LocationData("Carwen - Lone Wolf Barrel (Cabin)", address = 0xC0FB38, area = "Carwen", location_type="event"),
LocationData("Bal Castle - Lone Wolf Chest (Thunder Whip)", address = 0xC0FB3A, area = "Bal Castle", location_type="event"),
LocationData("Bal Castle - Moat Item (Epee)", address = 0xC0FB3C, area = "Bal Castle", location_type="event"),
LocationData("Bal Castle - Shop Backdoor (Lamia Harp)", address = 0xC0FB3E, area = "Bal Castle", location_type="event"),
LocationData("Istory Falls - Top of the Falls (Magic Lamp)", address = 0xC0FB40, area = "Istory Falls", location_type="event"),
LocationData("Wind Shrine - Wind Shrine Chest (Broadsword)", address = 0xD13212, area = "Wind Shrine", location_type="chest"),
LocationData("Tule - Beginner's House Chest (Ether)", address = 0xD13216, area = "Tule", location_type="chest"),
LocationData("Tule - Beginner's House Chest (100)", address = 0xD1321A, area = "Tule", location_type="chest"),
LocationData("Tule - Beginner's House Chest (Potion)", address = 0xD1321E, area = "Tule", location_type="chest"),
LocationData("Tule - Beginner's House Chest (Phoenix Down)", address = 0xD13222, area = "Tule", location_type="chest"),
LocationData("Tule - Beginner's House Chest (Tent)", address = 0xD13226, area = "Tule", location_type="chest"),
LocationData("Tule - Beginner's House Chest MIB 1 (Leather Shoes)", address = 0xD1322A, area = "Tule", location_type="chest"),
LocationData("Pirate's Cave - Pirate's Cave Chest (Leather Cap)", address = 0xD1322E, area = "Pirate's Cave", location_type="chest"),
LocationData("Pirate's Cave - Pirate's Cave Chest (Tent)", address = 0xD13232, area = "Pirate's Cave", location_type="chest"),
LocationData("Pirate's Cave - Pirate's Cave Chest (Ether)", address = 0xD13236, area = "Pirate's Cave", location_type="chest"),
LocationData("Pirate's Cave - Pirate's Cave Chest (300)", address = 0xD1323A, area = "Pirate's Cave", location_type="chest"),
LocationData("Wind Shrine - Wind Shrine Chest (Tent)", address = 0xD1323E, area = "Wind Shrine", location_type="chest"),
LocationData("Wind Shrine - Wind Shrine Chest (Leather Cap)", address = 0xD13242, area = "Wind Shrine", location_type="chest"),
LocationData("Wind Shrine - Wind Shrine Chest (Staff)", address = 0xD13246, area = "Wind Shrine", location_type="chest"),
LocationData("Tule - Tule Barrel (150)", address = 0xD1324A, area = "Tule", location_type="chest"),
LocationData("Tule - Tule Box (Leather Shoes)", address = 0xD1324E, area = "Tule", location_type="chest"),
LocationData("Tule - Tule Barrel (Potion)", address = 0xD13252, area = "Tule", location_type="chest"),
LocationData("Tule - Tule Box (Tent)", address = 0xD13256, area = "Tule", location_type="chest"),
LocationData("Tule - Tule Bush (Phoenix Down)", address = 0xD1325A, area = "Tule", location_type="chest"),
LocationData("Ship Graveyard - Ship Graveyard Chest (Flail)", address = 0xD1325E, area = "Ship Graveyard", location_type="chest"),
LocationData("Ship Graveyard - Ship Graveyard Chest (Phoenix Down (1))", address = 0xD13262, area = "Ship Graveyard", location_type="chest"),
LocationData("Ship Graveyard - Ship Graveyard Chest (Tent)", address = 0xD13266, area = "Ship Graveyard", location_type="chest"),
LocationData("Ship Graveyard - Ship Graveyard Box (990)", address = 0xD1326A, area = "Ship Graveyard", location_type="chest"),
LocationData("Ship Graveyard - Ship Graveyard Chest (Potion)", address = 0xD1326E, area = "Ship Graveyard", location_type="chest"),
LocationData("Ship Graveyard - Ship Graveyard Chest (Antidote (1))", address = 0xD13272, area = "Ship Graveyard", location_type="chest"),
LocationData("Ship Graveyard - Ship Graveyard Chest (Antidote (2))", address = 0xD13276, area = "Ship Graveyard", location_type="chest"),
LocationData("Ship Graveyard - Ship Graveyard Chest (Phoenix Down (2))", address = 0xD1327A, area = "Ship Graveyard", location_type="chest"),
LocationData("Carwen - Carwen Barrel (Antidote)", address = 0xD1327E, area = "Carwen", location_type="chest"),
LocationData("Carwen - Carwen Box (Ice Rod)", address = 0xD13282, area = "Carwen", location_type="chest"),
LocationData("Carwen - Carwen Pot (1000)", address = 0xD13286, area = "Carwen", location_type="chest"),
LocationData("North Mountain - North Mountain Chest (Soft)", address = 0xD1328A, area = "North Mountain", location_type="chest"),
LocationData("North Mountain - North Mountain Chest (Phoenix Down)", address = 0xD1328E, area = "North Mountain", location_type="chest"),
LocationData("Walse Town - Walse Town Pot (Glasses)", address = 0xD13292, area = "Walse Town", location_type="chest"),
LocationData("Tycoon Castle - Tycoon Castle Pot (Hi-Potion)", address = 0xD13296, area = "Tycoon Castle", location_type="chest"),
LocationData("Tycoon Castle - Tycoon Castle Pot (Ether (1))", address = 0xD1329A, area = "Tycoon Castle", location_type="chest"),
LocationData("Tycoon Castle - Tycoon Castle Barrel (Elixir)", address = 0xD1329E, area = "Tycoon Castle", location_type="chest"),
LocationData("Tycoon Castle - Tycoon Castle Barrel (Phoenix Down)", address = 0xD132A2, area = "Tycoon Castle", location_type="chest"),
LocationData("Tycoon Castle - Tycoon Castle Barrel (Cabin)", address = 0xD132A6, area = "Tycoon Castle", location_type="chest"),
LocationData("Tycoon Castle - Tycoon Castle Pot (Ether 2)", address = 0xD132AA, area = "Tycoon Castle", location_type="chest"),
LocationData("Tycoon Castle - Tycoon Castle Pot (Elixir)", address = 0xD132AE, area = "Tycoon Castle", location_type="chest"),
LocationData("Tycoon Castle - Tycoon Castle Pot (Phoenix Down)", address = 0xD132B2, area = "Tycoon Castle", location_type="chest"),
LocationData("Tycoon Castle - Tycoon Castle Pot (Maiden's Kiss)", address = 0xD132B6, area = "Tycoon Castle", location_type="chest"),
LocationData("Tycoon Castle - Tycoon Castle Chest (Shuriken)", address = 0xD132BA, area = "Tycoon Castle", location_type="chest"),
LocationData("Tycoon Castle - Tycoon Castle Chest (Giyaman)", address = 0xD132BE, area = "Tycoon Castle", location_type="chest"),
LocationData("Tycoon Castle - Tycoon Castle Chest (Katana)", address = 0xD132C2, area = "Tycoon Castle", location_type="chest"),
LocationData("Walse Castle - Walse Castle Chest (Elf Cape)", address = 0xD132C6, area = "Walse Castle", location_type="chest"),
LocationData("Walse Castle - Walse Castle Pot (1000 (1))", address = 0xD132CA, area = "Walse Castle", location_type="chest"),
LocationData("Walse Castle - Walse Castle Pot (Drag)", address = 0xD132CE, area = "Walse Castle", location_type="chest"),
LocationData("Walse Castle - Walse Castle Pot (1000 (2))", address = 0xD132D2, area = "Walse Castle", location_type="chest"),
LocationData("Walse Castle - Walse Castle Box (490)", address = 0xD132D6, area = "Walse Castle", location_type="chest"),
LocationData("Walse Castle - Walse Castle Barrel (Tent)", address = 0xD132DA, area = "Walse Castle", location_type="chest"),
LocationData("Walse Castle - Walse Castle Barrel (Phoenix Down)", address = 0xD132DE, area = "Walse Castle", location_type="chest"),
LocationData("Walse Tower - Walse Tower Chest (Silk robe)", address = 0xD132E2, area = "Walse Tower", location_type="chest"),
LocationData("Walse Tower - Walse Tower Chest (Maiden's Kiss)", address = 0xD132E6, area = "Walse Tower", location_type="chest"),
LocationData("Walse Tower - Walse Tower Chest (Silver Armlet)", address = 0xD132EA, area = "Walse Tower", location_type="chest"),
LocationData("Walse Tower - Walse Tower Chest (Ether)", address = 0xD132EE, area = "Walse Tower", location_type="chest"),
LocationData("Tycoon Meteor - Tycoon Meteor Chest (Phoenix Down)", address = 0xD132F2, area = "Tycoon Meteor", location_type="chest"),
LocationData("Karnak - Karnak Castle Chest MIB 1 (Heavy Spear)", address = 0xD132F6, area = "Karnak", location_type="chest"),
LocationData("Karnak - Karnak Castle Chest MIB 2 (Thunder Scroll)", address = 0xD132FA, area = "Karnak", location_type="chest"),
LocationData("Karnak - Karnak Castle Chest (2000 (1))", address = 0xD132FE, area = "Karnak", location_type="chest"),
LocationData("Karnak - Karnak Castle Chest MIB 3 (Elixir)", address = 0xD13302, area = "Karnak", location_type="chest"),
LocationData("Karnak - Karnak Castle Chest (Elixir (1))", address = 0xD13306, area = "Karnak", location_type="chest"),
LocationData("Karnak - Karnak Castle Chest (Elixir (2))", address = 0xD1330A, area = "Karnak", location_type="chest"),
LocationData("Karnak - Karnak Castle Chest (2000 (2))", address = 0xD1330E, area = "Karnak", location_type="chest"),
LocationData("Karnak - Karnak Castle Chest (Elixir (3))", address = 0xD13312, area = "Karnak", location_type="chest"),
LocationData("Karnak - Karnak Castle Chest (Elixir (4))", address = 0xD13316, area = "Karnak", location_type="chest"),
LocationData("Karnak - Karnak Castle Chest (Ribbon)", address = 0xD1331A, area = "Karnak", location_type="chest"),
LocationData("Karnak - Karnak Castle Chest (Shuriken)", address = 0xD1331E, area = "Karnak", location_type="chest"),
LocationData("Karnak - Karnak Castle Chest (2000 (3))", address = 0xD13322, area = "Karnak", location_type="chest"),
LocationData("Karnak - Karnak Castle Chest (Elixir (5))", address = 0xD13326, area = "Karnak", location_type="chest"),
LocationData("Karnak - Karnak Castle Chest (Elf Cape)", address = 0xD1332A, area = "Karnak", location_type="chest"),
LocationData("Karnak - Karnak Castle Chest (Guardian)", address = 0xD1332E, area = "Karnak", location_type="chest"),
LocationData("Karnak - Karnak Town Barrel (Fire Rod)", address = 0xD13332, area = "Karnak", location_type="chest"),
LocationData("Steamship - Steamship Chest (Cabin)", address = 0xD13336, area = "Steamship", location_type="chest"),
LocationData("Steamship - Steamship Chest (Phoenix Down)", address = 0xD1333A, area = "Steamship", location_type="chest"),
LocationData("Steamship - Steamship Chest (Elixir 1)", address = 0xD1333E, area = "Steamship", location_type="chest"),
LocationData("Steamship - Steamship Chest (GrnBeret)", address = 0xD13342, area = "Steamship", location_type="chest"),
LocationData("Steamship - Steamship Chest (Thief's Glove)", address = 0xD13346, area = "Steamship", location_type="chest"),
LocationData("Steamship - Steamship Chest (Elixir 2)", address = 0xD1334A, area = "Steamship", location_type="chest"),
LocationData("Ancient Library - Ancient Library Chest (Ether)", address = 0xD1334E, area = "Ancient Library", location_type="chest"),
LocationData("Ancient Library Lower - Ancient Library Chest (Phoenix Down)", address = 0xD13352, area = "Ancient Library Lower", location_type="chest"),
LocationData("Ancient Library Lower - Ancient Library Chest (Stealth Suit)", address = 0xD13356, area = "Ancient Library Lower", location_type="chest"),
LocationData("Jacole - Jacole Cave Chest (Shuriken)", address = 0xD1335A, area = "Jacole", location_type="chest"),
LocationData("Jacole - Jacole Cave Chest (Tent)", address = 0xD1335E, area = "Jacole", location_type="chest"),
LocationData("Ruined City - Ruined City Chest (Shuriken 1)", address = 0xD13362, area = "Ruined City", location_type="chest"),
LocationData("Ruined City - Ruined City Chest (Shuriken 2)", address = 0xD13366, area = "Ruined City", location_type="chest"),
LocationData("Ruined City - Ruined City Chest (Size)", address = 0xD1336A, area = "Ruined City", location_type="chest"),
LocationData("Flying Lonka Ruins - Flying Lonka Ruins Chest (Golden Armor)", address = 0xD1336E, area = "Flying Lonka Ruins", location_type="chest"),
LocationData("Flying Lonka Ruins - Flying Lonka Ruins Chest (Elixir)", address = 0xD13372, area = "Flying Lonka Ruins", location_type="chest"),
LocationData("Flying Lonka Ruins - Flying Lonka Ruins Chest (Phoenix Down)", address = 0xD13376, area = "Flying Lonka Ruins", location_type="chest"),
LocationData("Flying Lonka Ruins - Flying Lonka Ruins Chest (Golden Shield)", address = 0xD1337A, area = "Flying Lonka Ruins", location_type="chest"),
LocationData("Steamship - Steamship Chest (Mythril Glove)", address = 0xD1337E, area = "Steamship", location_type="chest"),
LocationData("Steamship - Steamship Chest (Elixir 3)", address = 0xD13382, area = "Steamship", location_type="chest"),
LocationData("Steamship - Steamship Chest (Full Moon)", address = 0xD13386, area = "Steamship", location_type="chest"),
LocationData("Flying Lonka Ruins - Flying Lonka Ruins Chest (Hi-Potion)", address = 0xD1338A, area = "Flying Lonka Ruins", location_type="chest"),
LocationData("Flying Lonka Ruins - Flying Lonka Ruins Chest (5000)", address = 0xD1338E, area = "Flying Lonka Ruins", location_type="chest"),
LocationData("Flying Lonka Ruins - Flying Lonka Ruins Chest (Shuriken)", address = 0xD13392, area = "Flying Lonka Ruins", location_type="chest"),
LocationData("Flying Lonka Ruins - Flying Lonka Ruins Chest (Ancient Sword)", address = 0xD13396, area = "Flying Lonka Ruins", location_type="chest"),
LocationData("Flying Lonka Ruins - Flying Lonka Ruins Chest (Full Moon)", address = 0xD1339A, area = "Flying Lonka Ruins", location_type="chest"),
LocationData("Flying Lonka Ruins - Flying Lonka Ruins Chest (Power Wrist)", address = 0xD1339E, area = "Flying Lonka Ruins", location_type="chest"),
LocationData("Flying Lonka Ruins - Flying Lonka Ruins Chest (Ether)", address = 0xD133A2, area = "Flying Lonka Ruins", location_type="chest"),
LocationData("Flying Lonka Ruins - Flying Lonka Ruins Chest (Cabin)", address = 0xD133A6, area = "Flying Lonka Ruins", location_type="chest"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (Ether 1)", address = 0xD133AA, area = "Exdeath's Castle", location_type="chest"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (Diamond Shield)", address = 0xD133AE, area = "Exdeath's Castle", location_type="chest"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (Ice Shield)", address = 0xD133B2, area = "Exdeath's Castle", location_type="chest"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (Ether 2)", address = 0xD133B6, area = "Exdeath's Castle", location_type="chest"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (Elixir 1)", address = 0xD133BA, area = "Exdeath's Castle", location_type="chest"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (Gale Bow)", address = 0xD133BE, area = "Exdeath's Castle", location_type="chest"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (IceBrand)", address = 0xD133C2, area = "Exdeath's Castle", location_type="chest"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (Kotetsu)", address = 0xD133C6, area = "Exdeath's Castle", location_type="chest"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (9900)", address = 0xD133CA, area = "Exdeath's Castle", location_type="chest"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (Elixir 2)", address = 0xD133CE, area = "Exdeath's Castle", location_type="chest"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (8000)", address = 0xD133D2, area = "Exdeath's Castle", location_type="chest"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (DblLance)", address = 0xD133D6, area = "Exdeath's Castle", location_type="chest"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (Partisan)", address = 0xD133DA, area = "Exdeath's Castle", location_type="chest"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (Pinwheel)", address = 0xD133DE, area = "Exdeath's Castle", location_type="chest"),
LocationData("Moogle Village - Moogle Cave Chest (4400)", address = 0xD133E2, area = "Moogle Village", location_type="chest"),
LocationData("Moogle Village - Moogle Cave Chest (Phoenix Down)", address = 0xD133E6, area = "Moogle Village", location_type="chest"),
LocationData("Moogle Village - Moogle Village Chest (Cabin)", address = 0xD133EA, area = "Moogle Village", location_type="chest"),
LocationData("Moogle Village - Moogle Village Chest (Dancing Dagger)", address = 0xD133EE, area = "Moogle Village", location_type="chest"),
LocationData("Moogle Village - Moogle Village Chest (1)", address = 0xD133F2, area = "Moogle Village", location_type="chest"),
LocationData("Moogle Village - Moogle Village Chest (10000)", address = 0xD133F6, area = "Moogle Village", location_type="chest"),
LocationData("Moogle Village - Moogle Village Chest (Phoenix Down)", address = 0xD133FA, area = "Moogle Village", location_type="chest"),
LocationData("Moogle Village - Moogle Village Chest (Ether)", address = 0xD133FE, area = "Moogle Village", location_type="chest"),
LocationData("Moogle Village - Moogle Village Chest (Elf Cape)", address = 0xD13402, area = "Moogle Village", location_type="chest"),
LocationData("Bal Castle - Bal Castle Chest (Angel Gwn)", address = 0xD13406, area = "Bal Castle", location_type="chest"),
LocationData("Bal Castle - Bal Castle Chest (Hero Drink)", address = 0xD1340A, area = "Bal Castle", location_type="chest"),
LocationData("Bal Castle - Bal Castle Chest (Exit)", address = 0xD1340E, area = "Bal Castle", location_type="chest"),
LocationData("Hiryuu Valley - Hiryuu Valley Skull (Bone Mail)", address = 0xD13412, area = "Hiryuu Valley", location_type="chest"),
LocationData("Hiryuu Valley - Hiryuu Valley Chest (5000)", address = 0xD13416, area = "Hiryuu Valley", location_type="chest"),
LocationData("Hiryuu Valley - Hiryuu Valley Chest (Cabin)", address = 0xD1341A, area = "Hiryuu Valley", location_type="chest"),
LocationData("Hiryuu Valley - Hiryuu Valley Chest (7000)", address = 0xD1341E, area = "Hiryuu Valley", location_type="chest"),
LocationData("Hiryuu Valley - Hiryuu Valley Chest (Hypno Helm)", address = 0xD13422, area = "Hiryuu Valley", location_type="chest"),
LocationData("Hiryuu Valley - Hiryuu Valley Chest (Air Blade)", address = 0xD13426, area = "Hiryuu Valley", location_type="chest"),
LocationData("Hiryuu Valley - Hiryuu Valley Chest (Phoenix Down)", address = 0xD1342A, area = "Hiryuu Valley", location_type="chest"),
LocationData("Surgate Castle - Surgate Castle Chest (5000)", address = 0xD1342E, area = "Surgate Castle", location_type="chest"),
LocationData("Surgate Castle - Surgate Castle Chest (Float)", address = 0xD13432, area = "Surgate Castle", location_type="chest"),
LocationData("Barrier Tower - Barrier Tower Chest MIB 1 (Drain Sword)", address = 0xD13436, area = "Barrier Tower", location_type="chest"),
LocationData("Barrier Tower - Barrier Tower Chest (9000)", address = 0xD1343A, area = "Barrier Tower", location_type="chest"),
LocationData("Barrier Tower - Barrier Tower Chest (18000)", address = 0xD1343E, area = "Barrier Tower", location_type="chest"),
LocationData("Barrier Tower - Barrier Tower Chest MIB 2 (Gold Hairpin)", address = 0xD13442, area = "Barrier Tower", location_type="chest"),
LocationData("Mua - Mua Town Barrel (Guardian)", address = 0xD13446, area = "Mua", location_type="chest"),
LocationData("Mua Forest - Mua Forest Chest (2500)", address = 0xD1344A, area = "Mua Forest", location_type="chest"),
LocationData("Mua Forest - Mua Forest Chest (Ether)", address = 0xD1344E, area = "Mua Forest", location_type="chest"),
LocationData("Mua Forest - Mua Forest Chest (4900)", address = 0xD13452, area = "Mua Forest", location_type="chest"),
LocationData("Mua Forest - Mua Forest Chest (Phoenix Down)", address = 0xD13456, area = "Mua Forest", location_type="chest"),
LocationData("Mua Forest - Mua Forest Chest (9500)", address = 0xD1345A, area = "Mua Forest", location_type="chest"),
LocationData("Mua Forest - Mua Forest Chest (Soot)", address = 0xD1345E, area = "Mua Forest", location_type="chest"),
LocationData("Mua Forest - Mua Forest Chest (Flametongue)", address = 0xD13462, area = "Mua Forest", location_type="chest"),
LocationData("Mua Forest - Mua Forest Chest (Cabin)", address = 0xD13466, area = "Mua Forest", location_type="chest"),
LocationData("Mua Forest - Mua Forest Chest (Giant Drink)", address = 0xD1346A, area = "Mua Forest", location_type="chest"),
LocationData("Mua Forest - Mua Forest Chest (Elixir)", address = 0xD1346E, area = "Mua Forest", location_type="chest"),
LocationData("Mua Forest - Mua Forest Chest (Morning Star)", address = 0xD13472, area = "Mua Forest", location_type="chest"),
LocationData("Solitary Island - Solitary Island Chest (Ether 1)", address = 0xD13476, area = "Solitary Island", location_type="chest"),
LocationData("Solitary Island - Solitary Island Chest (DragonFang)", address = 0xD1347A, area = "Solitary Island", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (Elixir 1)", address = 0xD1347E, area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (Elixir 2)", address = 0xD13482, area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest MIB 1 (Black Robe)", address = 0xD13486, area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (Thornlet)", address = 0xD1348A, area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest MIB 2 (DarkMatter)", address = 0xD1348E, area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest MIB 3 (Crystal Armor)", address = 0xD13492, area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (Cursed Ring)", address = 0xD13496, area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (Ice Shield)", address = 0xD1349A, area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (Flame Shield)", address = 0xD1349E, area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (DarkMatter 1)", address = 0xD134A2, area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (White Robe)", address = 0xD134A6, area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (DarkSuit)", address = 0xD134AA, area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (DarkMatter 2)", address = 0xD134AE, area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (DarkMatter 3)", address = 0xD134B2, area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (DarkMatter 4)", address = 0xD134B6, area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (9000)", address = 0xD134BA, area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (8000)", address = 0xD134BE, area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (Earth Hammer)", address = 0xD134C2, area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (10000)", address = 0xD134C6, area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (Cabin)", address = 0xD134CA, area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (Elixir 3)", address = 0xD134CE, area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (12000)", address = 0xD134D2, area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (DarkMatter 5)", address = 0xD134D6, area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (Elixir 4)", address = 0xD134DA, area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (DarkMatter 6)", address = 0xD134DE, area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (Guard Ring)", address = 0xD134E2, area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (Ribbon)", address = 0xD134E6, area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (Gold Hairpin)", address = 0xD134EA, area = "Pyramid", location_type="chest"),
LocationData("Solitary Island - Solitary Island Chest (12000)", address = 0xD134EE, area = "Solitary Island", location_type="chest"),
LocationData("Solitary Island - Solitary Island Chest (Hi-Potion)", address = 0xD134F2, area = "Solitary Island", location_type="chest"),
LocationData("Solitary Island - Solitary Island Chest (Protect Drink)", address = 0xD134F6, area = "Solitary Island", location_type="chest"),
LocationData("Solitary Island - Solitary Island Chest (BeastKiller)", address = 0xD134FA, area = "Solitary Island", location_type="chest"),
LocationData("Solitary Island - Solitary Island Chest MIB 1 (RisingSun)", address = 0xD134FE, area = "Solitary Island", location_type="chest"),
LocationData("Solitary Island - Solitary Island Chest (Ether 2)", address = 0xD13502, area = "Solitary Island", location_type="chest"),
LocationData("Solitary Island - Solitary Island Chest MIB 2 (Guard Ring)", address = 0xD13506, area = "Solitary Island", location_type="chest"),
LocationData("Solitary Island - Solitary Island Chest (Crystal Helm)", address = 0xD1350A, area = "Solitary Island", location_type="chest"),
LocationData("Solitary Island - Solitary Island Chest (9000)", address = 0xD1350E, area = "Solitary Island", location_type="chest"),
LocationData("Solitary Island - Solitary Island Chest (Elixir)", address = 0xD13512, area = "Solitary Island", location_type="chest"),
LocationData("Solitary Island - Solitary Island Chest (DarkMatter)", address = 0xD13516, area = "Solitary Island", location_type="chest"),
LocationData("Solitary Island - Solitary Island Chest (Circlet)", address = 0xD1351A, area = "Solitary Island", location_type="chest"),
LocationData("Fork Tower - Fork Tower L. Chest (Ether)", address = 0xD1351E, area = "Fork Tower", location_type="chest"),
LocationData("Fork Tower - Fork Tower L. Chest (Wonder Wand)", address = 0xD13522, area = "Fork Tower", location_type="chest"),
LocationData("Fork Tower - Fork Tower R. Chest (Hi-Potion)", address = 0xD13526, area = "Fork Tower", location_type="chest"),
LocationData("Fork Tower - Fork Tower R. Chest (Defender Sword)", address = 0xD1352A, area = "Fork Tower", location_type="chest"),
LocationData("Great Trench - Great Trench Chest (Water Scroll)", address = 0xD1352E, area = "Great Trench", location_type="chest"),
LocationData("Great Trench - Great Trench Chest (Flame Ring)", address = 0xD13532, area = "Great Trench", location_type="chest"),
LocationData("Great Trench - Great Trench Chest (DragonFang)", address = 0xD13536, area = "Great Trench", location_type="chest"),
LocationData("Great Trench - Great Trench Chest (Ether)", address = 0xD1353A, area = "Great Trench", location_type="chest"),
LocationData("Great Trench - Great Trench Chest (Phoenix Down)", address = 0xD1353E, area = "Great Trench", location_type="chest"),
LocationData("Great Trench - Great Trench Chest (Kaiser Knuckles)", address = 0xD13542, area = "Great Trench", location_type="chest"),
LocationData("Istory Falls - Istory Falls Chest (Ether)", address = 0xD13546, area = "Istory Falls", location_type="chest"),
LocationData("Istory Falls - Istory Falls Chest (TurtleShell)", address = 0xD1354A, area = "Istory Falls", location_type="chest"),
LocationData("Istory Falls - Istory Falls Chest (Air Knife)", address = 0xD1354E, area = "Istory Falls", location_type="chest"),
LocationData("Istory Falls - Istory Falls Chest (Giant Drink)", address = 0xD13552, area = "Istory Falls", location_type="chest"),
LocationData("Istory Falls - Istory Falls Chest (RuneEdge)", address = 0xD13556, area = "Istory Falls", location_type="chest"),
LocationData("Istory Falls - Istory Falls Chest (Guard Ring)", address = 0xD1355A, area = "Istory Falls", location_type="chest"),
LocationData("Istory Falls - Istory Falls Chest (Wall Ring)", address = 0xD1355E, area = "Istory Falls", location_type="chest"),
LocationData("Istory Falls - Istory Falls Chest (Phoenix Down)", address = 0xD13562, area = "Istory Falls", location_type="chest"),
LocationData("Istory Falls - Istory Falls Chest (Enhancer)", address = 0xD13566, area = "Istory Falls", location_type="chest"),
LocationData("Istory Falls - Istory Falls Chest (12000)", address = 0xD1356A, area = "Istory Falls", location_type="chest"),
LocationData("Istory Falls - Istory Falls Chest (Artemis Bow)", address = 0xD1356E, area = "Istory Falls", location_type="chest"),
LocationData("Istory Falls - Istory Falls Chest (Pinwheel)", address = 0xD13572, area = "Istory Falls", location_type="chest"),
LocationData("Istory Falls - Istory Falls Chest (Aegis Shield)", address = 0xD13576, area = "Istory Falls", location_type="chest"),
LocationData("Istory Falls - Istory Falls Chest (Giant's Axe)", address = 0xD1357A, area = "Istory Falls", location_type="chest"),
LocationData("Phoenix Tower - Phoenix Tower Pot (5000)", address = 0xD1357E, area = "Phoenix Tower", location_type="chest"),
LocationData("Phoenix Tower - Phoenix Tower Pot (Phoenix Down 1)", address = 0xD13582, area = "Phoenix Tower", location_type="chest"),
LocationData("Phoenix Tower - Phoenix Tower Pot (10000)", address = 0xD13586, area = "Phoenix Tower", location_type="chest"),
LocationData("Phoenix Tower - Phoenix Tower Pot (Phoenix Down 2)", address = 0xD1358A, area = "Phoenix Tower", location_type="chest"),
LocationData("Phoenix Tower - Phoenix Tower Pot (Phoenix Down 3)", address = 0xD1358E, area = "Phoenix Tower", location_type="chest"),
LocationData("Phoenix Tower - Phoenix Tower Pot (15000)", address = 0xD13592, area = "Phoenix Tower", location_type="chest"),
LocationData("Phoenix Tower - Phoenix Tower Pot (20000)", address = 0xD13596, area = "Phoenix Tower", location_type="chest"),
LocationData("Phoenix Tower - Phoenix Tower Pot (Phoenix Down 4)", address = 0xD1359A, area = "Phoenix Tower", location_type="chest"),
LocationData("Phoenix Tower - Phoenix Tower Pot (Avis Killer)", address = 0xD1359E, area = "Phoenix Tower", location_type="chest"),
LocationData("Phoenix Tower - Phoenix Tower Pot (25000)", address = 0xD135A2, area = "Phoenix Tower", location_type="chest"),
LocationData("Mirage Village - Mirage Village Barrel (Thief Knife)", address = 0xD135A6, area = "Mirage Village", location_type="chest"),
LocationData("Rift (1 Tablet) - Rift (Ruins) Chest (Ether)", address = 0xD135AA, area = "Rift (1 Tablet)", location_type="chest"),
LocationData("Rift (1 Tablet) - Rift (Ruins) Chest (Cabin)", address = 0xD135AE, area = "Rift (1 Tablet)", location_type="chest"),
LocationData("Rift (1 Tablet) - Rift (Ruins) Chest (Elixir 1)", address = 0xD135B2, area = "Rift (1 Tablet)", location_type="chest"),
LocationData("Rift (1 Tablet) - Rift (Ruins) Chest (DarkMatter)", address = 0xD135B6, area = "Rift (1 Tablet)", location_type="chest"),
LocationData("Rift (1 Tablet) - Rift (Ruins) Chest (Elixir 2)", address = 0xD135BA, area = "Rift (1 Tablet)", location_type="chest"),
LocationData("Rift (1 Tablet) - Rift (Ruins) Chest (Drain Sword)", address = 0xD135BE, area = "Rift (1 Tablet)", location_type="chest"),
LocationData("Rift (1 Tablet) - Rift (Forest) Chest (DragonFang)", address = 0xD135C2, area = "Rift (1 Tablet)", location_type="chest"),
LocationData("Rift (1 Tablet) - Rift (Forest) Chest (Ribbon)", address = 0xD135C6, area = "Rift (1 Tablet)", location_type="chest"),
LocationData("Rift (1 Tablet) - Rift (Forest) Chest (Enhancer)", address = 0xD135CA, area = "Rift (1 Tablet)", location_type="chest"),
LocationData("Rift (1 Tablet) - Rift (Forest) Chest (Lillith Rod)", address = 0xD135CE, area = "Rift (1 Tablet)", location_type="chest"),
LocationData("Rift (2 Tablets) - Rift (Cave) Chest (Angel Ring)", address = 0xD135D2, area = "Rift (2 Tablets)", location_type="chest"),
LocationData("Rift (2 Tablets) - Rift (Cave) Chest (Coral Ring)", address = 0xD135D6, area = "Rift (2 Tablets)", location_type="chest"),
LocationData("Rift (3 Tablets) - Rift (Castle) Chest (Thor Hammer)", address = 0xD135DA, area = "Rift (3 Tablets)", location_type="chest"),
LocationData("Rift (3 Tablets) - Rift (Castle) Chest (Running Shoes)", address = 0xD135DE, area = "Rift (3 Tablets)", location_type="chest"),
LocationData("Rift (3 Tablets) - Rift (Castle) Chest (Red Shoes)", address = 0xD135E2, area = "Rift (3 Tablets)", location_type="chest"),
LocationData("Rift (3 Tablets) - Rift (Castle) Chest (Rainbow Dress)", address = 0xD135E6, area = "Rift (3 Tablets)", location_type="chest"),
LocationData("Rift (3 Tablets) - Rift (Castle) Chest (ManEater)", address = 0xD135EA, area = "Rift (3 Tablets)", location_type="chest"),
LocationData("Void - The Void Chest (Pinwheel 1)", address = 0xD135EE, area = "Void", location_type="chest"),
LocationData("Void - The Void Chest (Pinwheel 2)", address = 0xD135F2, area = "Void", location_type="chest"),
LocationData("Void - The Void Chest (Elixir)", address = 0xD135F6, area = "Void", location_type="chest"),
LocationData("Void - The Void Chest (Ragnarok)", address = 0xD135FA, area = "Void", location_type="chest"),
LocationData("Void - The Void Chest (Pinwheel 3)", address = 0xD135FE, area = "Void", location_type="chest"),
LocationData("Ancient Library Lower - Byblos (Boss)", address = 0xC0FB70, area = "Ancient Library Lower", location_type="key"),
LocationData("Wind Shrine - WingRaptor (Boss)", address = 0xC0FB72, area = "Wind Shrine",location_type="key"),
LocationData("Torna Canal - Karlabos (Boss)", address = 0xC0FB74, area = "Torna Canal",location_type="key"),
LocationData("Ship Graveyard - Siren (Boss)", address = 0xC0FB76, area = "Ship Graveyard",location_type="key"),
LocationData("North Mountain - Magisa & Forza (Boss)", address = 0xC0FB78, area = "North Mountain",location_type="key"),
LocationData("Walse Tower - Galura (Boss)", address = 0xC0FB7A, area = "Walse Tower",location_type="key"),
LocationData("Steamship - LiquiFlame (Boss)", address = 0xC0FB7C, area = "Steamship",location_type="key"),
LocationData("Karnak - Sergeant & DeathClaw (Boss)", address = 0xC0FB7E, area = "Karnak",location_type="key"),
LocationData("Desert of Shifting Sands - Sandworm (Boss)", address = 0xC0FB80, area = "Desert of Shifting Sands",location_type="key"),
LocationData("Tycoon Meteor - AdamanTiMi (Boss)", address = 0xC0FB82, area = "Tycoon Meteor",location_type="key"),
LocationData("Flying Lonka Ruins - Sol Cannon (Boss)", address = 0xC0FB84, area = "Flying Lonka Ruins",location_type="key"),
LocationData("Flying Lonka Ruins - ArchaeAvis (Boss)", address = 0xC0FB86, area = "Flying Lonka Ruins",location_type="key"),
LocationData("Lonka Meteor - Chim.Brain (Boss)", address = 0xC0FB88, area = "Lonka Meteor",location_type="key"),
LocationData("Walse Meteor - Puroboros (Boss)", address = 0xC0FB8A, area = "Walse Meteor",location_type="key"),
LocationData("Karnak Meteor - Titan (Boss)", address = 0xC0FB8C, area = "Karnak Meteor",location_type="key"),
LocationData("Ancient Library - Ifrit (Boss)", address = 0xC0FBB6, area = "Ancient Library",location_type="key"),
LocationData("Walse Castle - Shiva (Boss)", address = 0xC0FBB8, area = "Walse Castle",location_type="key"),
LocationData("Catapult - Crayclaw (Boss)", address = 0xC0FBBA, area = "Catapult",location_type="key"),
LocationData("Exdeath's Castle Lower - Gilgamesh 1 (Boss)", address = 0xC0FB8E, area = "Exdeath's Castle Lower",location_type="key"),
LocationData("Big Bridge - Gilgamesh 2 (Boss)", address = 0xC0FB90, area = "Big Bridge",location_type="key"),
LocationData("Moogle Waterway - Tyrasaurus (Boss)", address = 0xC0FB92, area = "Moogle Waterway",location_type="key"),
LocationData("Bal Castle - Abductor (Boss)", address = 0xC0FB94, area = "Bal Castle",location_type="key"),
LocationData("Hiryuu Valley - HiryuuPlant (Boss)", address = 0xC0FB96, area = "Hiryuu Valley",location_type="key"),
LocationData("Zeza Fleet - Gilgamesh 3 & Enkidou (Boss)", address = 0xC0FB98, area = "Zeza Fleet",location_type="key"),
LocationData("Barrier Tower - Atmos (Boss)", address = 0xC0FB9A, area = "Barrier Tower",location_type="key"),
LocationData("Mua Forest - Guardians (Boss)", address = 0xC0FB9C, area = "Mua Forest",location_type="key"),
LocationData("Exdeath's Castle - Carbunkle (Boss)", address = 0xC0FB9E, area = "Exdeath's Castle",location_type="key"),
LocationData("Exdeath's Castle - Gilgamesh 4 (Boss)", address = 0xC0FBA0, area = "Exdeath's Castle",location_type="key"),
LocationData("Tule Pass - Antlion (Boss)", address = 0xC0FBA2, area = "Tule Pass",location_type="key"),
LocationData("Pyramid - Merugene (Boss)", address = 0xC0FBA4, area = "Pyramid",location_type="key"),
LocationData("Bal Castle Lower - Odin (Boss)", address = 0xC0FBA6, area = "Bal Castle Lower",location_type="key"),
LocationData("Great Trench - Triton, Neregeid & Phobos (Boss)", address = 0xC0FBA8, area = "Great Trench",location_type="key"),
LocationData("Fork Tower - Omniscient (Boss)", address = 0xC0FBAA, area = "Fork Tower",location_type="key"),
LocationData("Fork Tower - Minotauros (Boss)", address = 0xC0FBAC, area = "Fork Tower",location_type="key"),
LocationData("Istory Falls - Leviathan (Boss)", address = 0xC0FBAE, area = "Istory Falls",location_type="key"),
LocationData("Solitary Island - Stalker (Boss)", address = 0xC0FBB0, area = "Solitary Island",location_type="key"),
LocationData("Walse Tower Sunken - GoGo (Boss)", address = 0xC0FBB2, area = "Walse Tower Sunken",location_type="key"),
LocationData("North Mountain (World 3) - Bahamut (Boss)", address = 0xC0FBB4, area = "North Mountain (World 3)", location_type="key"),
LocationData("ExDeath", address = 0xC0FFFF, area = "Void", location_type="key"),
]