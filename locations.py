from BaseClasses import Location
from BaseClasses import ItemClassification
from worlds.generic.Rules import add_item_rule
from .items import arch_item_offset
loc_id_start = 342000000



class LocationData:
    def __init__(self, name, address = None, parent = None, area = None, location_type="", type="Item"):
        self.name = name
        try:
            self.address = int(address, base=16) + loc_id_start
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


        
        
        # only allow kuzar to place this seed's items
        # disallow mua from being progression, both town (brave/chicken) and dungeon (non burning vs burning)
        # only allow karnak to place this seed's items
        # disallow lone wolf/under bal castle related checks for some weird progression problems
        if location_data.area in ["Kuzar", "Mua", "Karnak"] or location_data.address in ['C0FB38', 'C0FB3A']:
            add_item_rule(self, lambda item: item.player == self.player)

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
                                                  (item.code - arch_item_offset) < 999)\
                                                  and item.player == self.player)

        
            


def create_location(world, player, location_data, parent=None):
    progression_checks_setting = world.progression_checks[player].value
    return_location = FFVCDLocation(player, location_data, parent, progression_checks_setting)
    return return_location

location_data = [

LocationData("Wind Shrine - Wind Crystal (Knight)", address = "C0FAB2", area = "Wind Shrine", location_type="event"),
LocationData("Wind Shrine - Wind Crystal (BlueMage)", address = "C0FAB4", area = "Wind Shrine", location_type="event"),
LocationData("Wind Shrine - Wind Crystal (BlackMage)", address = "C0FAB6", area = "Wind Shrine", location_type="event"),
LocationData("Wind Shrine - Wind Crystal (WhiteMage)", address = "C0FAB8", area = "Wind Shrine", location_type="event"),
LocationData("Wind Shrine - Wind Crystal (Monk)", address = "C0FABA", area = "Wind Shrine", location_type="event"),
LocationData("Wind Shrine - Wind Crystal (Thief)", address = "C0FABC", area = "Wind Shrine", location_type="event"),
LocationData("Karnak - Fire Crystal (Trainer)", address = "C0FABE", area = "Karnak", location_type="event"),
LocationData("Karnak - Fire Crystal (Geomancer)", address = "C0FAC0", area = "Karnak", location_type="event"),
LocationData("Karnak - Fire Crystal (Ninja)", address = "C0FAC2", area = "Karnak", location_type="event"),
LocationData("Crescent Island - Black Choco Crystals (Bard)", address = "C0FAC4", area = "Crescent Island", location_type="event"),
LocationData("Crescent Island - Black Choco Crystals (Hunter)", address = "C0FAC6", area = "Crescent Island", location_type="event"),
LocationData("Flying Lonka Ruins - Earth Crystal (Samurai)", address = "C0FAC8", area = "Flying Lonka Ruins", location_type="event"),
LocationData("Flying Lonka Ruins - Earth Crystal (Dragoon)", address = "C0FACA", area = "Flying Lonka Ruins", location_type="event"),
LocationData("Flying Lonka Ruins - Earth Crystal (Chemist)", address = "C0FACC", area = "Flying Lonka Ruins", location_type="event"),
LocationData("Flying Lonka Ruins - Earth Crystal (Dancer)", address = "C0FACE", area = "Flying Lonka Ruins", location_type="event"),
LocationData("Istory Falls - Leviathan Esper (Levia)", address = "C0FAD0", area = "Istory Falls", location_type="event"),
LocationData("Karnak Meteor - Titan (Titan)", address = "C0FAD2", area = "Karnak Meteor", location_type="event"),
LocationData("Exdeath's Castle - Carbuncle (Crbnkl)", address = "C0FAD4", area = "Exdeath's Castle", location_type="event"),
LocationData("Pirate's Cave - Syldra (Syldra)", address = "C0FAD6", area = "Pirate's Cave", location_type="event"),
LocationData("Bal Castle Lower - Odin (Odin)", address = "C0FAD8", area = "Bal Castle Lower", location_type="event"),
LocationData("Phoenix Tower - Phoenix (Phenix)", address = "C0FADA", area = "Phoenix Tower", location_type="event"),
LocationData("North Mountain (World 3) - Bahamut (Bahmut)", address = "C0FADC", area = "North Mountain (World 3)", location_type="event"),
LocationData("Crescent Island - Life Song (Vitality)", address = "C0FADE", area = "Crescent Island", location_type="event"),
LocationData("Lix - Temptation Song at Lix (Charm)", address = "C0FAE0", area = "Lix", location_type="event"),
LocationData("Istory - Love Song at Istory (Love)", address = "C0FAE2", area = "Istory", location_type="event"),
LocationData("Kelb - Requiem Song at Kelb (Requiem)", address = "C0FAE4", area = "Kelb", location_type="event"),
LocationData("Surgate Castle - Speed Song at Surgate (Speed)", address = "C0FAE6", area = "Surgate Castle", location_type="event"),
LocationData("Ancient Library - Magic Song at Ancient Library (Magic)", address = "C0FAE8", area = "Ancient Library", location_type="event"),
LocationData("Crescent Island - Power Song from Crescent Town (Power)", address = "C0FAEA", area = "Crescent Island", location_type="event"),
LocationData("Crescent Island - Hero Song from Crescent Town (Hero)", address = "C0FAEC", area = "Crescent Island", location_type="event"),
LocationData("Fork Tower - Fork Tower, two Magics (Holy)", address = "C0FAEE", area = "Fork Tower", location_type="event"),
LocationData("Fork Tower - Fork Tower, two Magics (Flare)", address = "C0FAF0", area = "Fork Tower", location_type="event"),
LocationData("Great Trench - Meteo (Meteo)", address = "C0FAF2", area = "Great Trench", location_type="event"),
LocationData("Wind Shrine - 5 potions (from NPC) (Potion)", address = "C0FAF4", area = "Wind Shrine", location_type="event"),
LocationData("Pirate's Cave - 8 potions (from NPC) (Potion)", address = "C0FAF6", area = "Pirate's Cave", location_type="event"),
LocationData("Tycoon Castle - Chancellor at Tycoon (Healing Staff)", address = "C0FAF8", area = "Tycoon Castle", location_type="event"),
LocationData("North Mountain - Magisa & Forza (Mythril Helm)", address = "C0FAFA", area = "North Mountain", location_type="event"),
LocationData("Kelb - CornaJar at Kelb (CornaJar)", address = "C0FAFC", area = "Kelb", location_type="event"),
LocationData("Rugor - Ribbon from girl in Rugor (Ribbon)", address = "C0FAFE", area = "Rugor", location_type="event"),
LocationData("Kuzar - 12 Kuzar Events (Excalibur)", address = "C0FB06", area = "Kuzar", location_type="event"),
LocationData("Kuzar - 12 Kuzar Events (Assassin)", address = "C0FB02", area = "Kuzar", location_type="event"),
LocationData("Kuzar - 12 Kuzar Events (Hardened Dagger)", address = "C0FB16", area = "Kuzar", location_type="event"),
LocationData("Kuzar - 12 Kuzar Events (Holy Lance)", address = "C0FB0C", area = "Kuzar", location_type="event"),
LocationData("Kuzar - 12 Kuzar Events (Rune Axe)", address = "C0FB12", area = "Kuzar", location_type="event"),
LocationData("Kuzar - 12 Kuzar Events (Masamune)", address = "C0FB0E", area = "Kuzar", location_type="event"),
LocationData("Kuzar - 12 Kuzar Events (Yoichi Bow)", address = "C0FB18", area = "Kuzar", location_type="event"),
LocationData("Kuzar - 12 Kuzar Events (Flame Whip)", address = "C0FB08", area = "Kuzar", location_type="event"),
LocationData("Kuzar - 12 Kuzar Events (Sage's Staff)", address = "C0FB14", area = "Kuzar", location_type="event"),
LocationData("Kuzar - 12 Kuzar Events (Wizard Rod)", address = "C0FB10", area = "Kuzar", location_type="event"),
LocationData("Kuzar - 12 Kuzar Events (Apollo's Harp)", address = "C0FB04", area = "Kuzar", location_type="event"),
LocationData("Kuzar - 12 Kuzar Events (Earth Bell)", address = "C0FB0A", area = "Kuzar", location_type="event"),
LocationData("Walse Castle - Shiva (Shiva)", address = "C0FB1A", area = "Walse Castle", location_type="event"),
LocationData("Ancient Library - Ifrit (Ifrit)", address = "C0FB1C", area = "Ancient Library", location_type="event"),
LocationData("Walse Tower - Water Crystal (RedMage)", address = "C0FB1E", area = "Walse Tower", location_type="event"),
LocationData("Walse Tower - Water Crystal (Berserker)", address = "C0FB20", area = "Walse Tower", location_type="event"),
LocationData("Walse Tower - Water Crystal (MysticKnight)", address = "C0FB22", area = "Walse Tower", location_type="event"),
LocationData("Walse Tower - Water Crystal (TimeMage)", address = "C0FB24", area = "Walse Tower", location_type="event"),
LocationData("Walse Tower - Water Crystal (Summoner)", address = "C0FB26", area = "Walse Tower", location_type="event"),
LocationData("Mua - Brave Blade (Brave Blade)", address = "C0FB28", area = "Mua", location_type="event"),
LocationData("Mua - Chicken Knife (Chicken Knife)", address = "C0FB2A", area = "Mua", location_type="event"),
LocationData("Tycoon Castle - Tycoon Castle Cabin (Cabin (1))", address = "C0FB2C", area = "Tycoon Castle", location_type="event"),
LocationData("Tycoon Castle - Tycoon Castle Cabin (Cabin (2))", address = "C0FB2E", area = "Tycoon Castle", location_type="event"),
LocationData("Walse Tower Sunken - Walse Tower Chest (GoGo)", address = "C0FB30", area = "Walse Tower Sunken", location_type="event"),
LocationData("Pyramid - Pyramid Top (Pyramid Tablet)", address = "C0FB32", area = "Pyramid", location_type="event"),
LocationData("Istory Falls - Toad Event (Toad)", address = "C0FB34", area = "Istory Falls", location_type="event"),
LocationData("Mua - Aegis Shield Chest (Aegis Shield)", address = "C0FB36", area = "Mua", location_type="event"),
LocationData("Carwen - Lone Wolf Barrel (Cabin)", address = "C0FB38", area = "Carwen", location_type="event"),
LocationData("Bal Castle - Lone Wolf Chest (Thunder Whip)", address = "C0FB3A", area = "Bal Castle", location_type="event"),
LocationData("Bal Castle - Moat Item (Epee)", address = "C0FB3C", area = "Bal Castle", location_type="event"),
LocationData("Bal Castle - Shop Backdoor (Lamia Harp)", address = "C0FB3E", area = "Bal Castle", location_type="event"),
LocationData("Istory Falls - Top of the Falls (Magic Lamp)", address = "C0FB40", area = "Istory Falls", location_type="event"),
LocationData("Wind Shrine - Wind Shrine Chest (Broadsword)", address = "D13212", area = "Wind Shrine", location_type="chest"),
LocationData("Tule - Beginner's House Chest (Ether)", address = "D13216", area = "Tule", location_type="chest"),
LocationData("Tule - Beginner's House Chest (100)", address = "D1321A", area = "Tule", location_type="chest"),
LocationData("Tule - Beginner's House Chest (Potion)", address = "D1321E", area = "Tule", location_type="chest"),
LocationData("Tule - Beginner's House Chest (Phoenix Down)", address = "D13222", area = "Tule", location_type="chest"),
LocationData("Tule - Beginner's House Chest (Tent)", address = "D13226", area = "Tule", location_type="chest"),
LocationData("Tule - Beginner's House Chest MIB 1 (Leather Shoes)", address = "D1322A", area = "Tule", location_type="chest"),
LocationData("Pirate's Cave - Pirate's Cave Chest (Leather Cap)", address = "D1322E", area = "Pirate's Cave", location_type="chest"),
LocationData("Pirate's Cave - Pirate's Cave Chest (Tent)", address = "D13232", area = "Pirate's Cave", location_type="chest"),
LocationData("Pirate's Cave - Pirate's Cave Chest (Ether)", address = "D13236", area = "Pirate's Cave", location_type="chest"),
LocationData("Pirate's Cave - Pirate's Cave Chest (300)", address = "D1323A", area = "Pirate's Cave", location_type="chest"),
LocationData("Wind Shrine - Wind Shrine Chest (Tent)", address = "D1323E", area = "Wind Shrine", location_type="chest"),
LocationData("Wind Shrine - Wind Shrine Chest (Leather Cap)", address = "D13242", area = "Wind Shrine", location_type="chest"),
LocationData("Wind Shrine - Wind Shrine Chest (Staff)", address = "D13246", area = "Wind Shrine", location_type="chest"),
LocationData("Tule - Tule Barrel (150)", address = "D1324A", area = "Tule", location_type="chest"),
LocationData("Tule - Tule Box (Leather Shoes)", address = "D1324E", area = "Tule", location_type="chest"),
LocationData("Tule - Tule Barrel (Potion)", address = "D13252", area = "Tule", location_type="chest"),
LocationData("Tule - Tule Box (Tent)", address = "D13256", area = "Tule", location_type="chest"),
LocationData("Tule - Tule Bush (Phoenix Down)", address = "D1325A", area = "Tule", location_type="chest"),
LocationData("Ship Graveyard - Ship Graveyard Chest (Flail)", address = "D1325E", area = "Ship Graveyard", location_type="chest"),
LocationData("Ship Graveyard - Ship Graveyard Chest (Phoenix Down (1))", address = "D13262", area = "Ship Graveyard", location_type="chest"),
LocationData("Ship Graveyard - Ship Graveyard Chest (Tent)", address = "D13266", area = "Ship Graveyard", location_type="chest"),
LocationData("Ship Graveyard - Ship Graveyard Box (990)", address = "D1326A", area = "Ship Graveyard", location_type="chest"),
LocationData("Ship Graveyard - Ship Graveyard Chest (Potion)", address = "D1326E", area = "Ship Graveyard", location_type="chest"),
LocationData("Ship Graveyard - Ship Graveyard Chest (Antidote (1))", address = "D13272", area = "Ship Graveyard", location_type="chest"),
LocationData("Ship Graveyard - Ship Graveyard Chest (Antidote (2))", address = "D13276", area = "Ship Graveyard", location_type="chest"),
LocationData("Ship Graveyard - Ship Graveyard Chest (Phoenix Down (2))", address = "D1327A", area = "Ship Graveyard", location_type="chest"),
LocationData("Carwen - Carwen Barrel (Antidote)", address = "D1327E", area = "Carwen", location_type="chest"),
LocationData("Carwen - Carwen Box (Ice Rod)", address = "D13282", area = "Carwen", location_type="chest"),
LocationData("Carwen - Carwen Pot (1000)", address = "D13286", area = "Carwen", location_type="chest"),
LocationData("North Mountain - North Mountain Chest (Soft)", address = "D1328A", area = "North Mountain", location_type="chest"),
LocationData("North Mountain - North Mountain Chest (Phoenix Down)", address = "D1328E", area = "North Mountain", location_type="chest"),
LocationData("Walse Town - Walse Town Pot (Glasses)", address = "D13292", area = "Walse Town", location_type="chest"),
LocationData("Tycoon Castle - Tycoon Castle Pot (Hi-Potion)", address = "D13296", area = "Tycoon Castle", location_type="chest"),
LocationData("Tycoon Castle - Tycoon Castle Pot (Ether (1))", address = "D1329A", area = "Tycoon Castle", location_type="chest"),
LocationData("Tycoon Castle - Tycoon Castle Barrel (Elixir)", address = "D1329E", area = "Tycoon Castle", location_type="chest"),
LocationData("Tycoon Castle - Tycoon Castle Barrel (Phoenix Down)", address = "D132A2", area = "Tycoon Castle", location_type="chest"),
LocationData("Tycoon Castle - Tycoon Castle Barrel (Cabin)", address = "D132A6", area = "Tycoon Castle", location_type="chest"),
LocationData("Tycoon Castle - Tycoon Castle Pot (Ether 2)", address = "D132AA", area = "Tycoon Castle", location_type="chest"),
LocationData("Tycoon Castle - Tycoon Castle Pot (Elixir)", address = "D132AE", area = "Tycoon Castle", location_type="chest"),
LocationData("Tycoon Castle - Tycoon Castle Pot (Phoenix Down)", address = "D132B2", area = "Tycoon Castle", location_type="chest"),
LocationData("Tycoon Castle - Tycoon Castle Pot (Maiden's Kiss)", address = "D132B6", area = "Tycoon Castle", location_type="chest"),
LocationData("Tycoon Castle - Tycoon Castle Chest (Shuriken)", address = "D132BA", area = "Tycoon Castle", location_type="chest"),
LocationData("Tycoon Castle - Tycoon Castle Chest (Giyaman)", address = "D132BE", area = "Tycoon Castle", location_type="chest"),
LocationData("Tycoon Castle - Tycoon Castle Chest (Katana)", address = "D132C2", area = "Tycoon Castle", location_type="chest"),
LocationData("Walse Castle - Walse Castle Chest (Elf Cape)", address = "D132C6", area = "Walse Castle", location_type="chest"),
LocationData("Walse Castle - Walse Castle Pot (1000 (1))", address = "D132CA", area = "Walse Castle", location_type="chest"),
LocationData("Walse Castle - Walse Castle Pot (Drag)", address = "D132CE", area = "Walse Castle", location_type="chest"),
LocationData("Walse Castle - Walse Castle Pot (1000 (2))", address = "D132D2", area = "Walse Castle", location_type="chest"),
LocationData("Walse Castle - Walse Castle Box (490)", address = "D132D6", area = "Walse Castle", location_type="chest"),
LocationData("Walse Castle - Walse Castle Barrel (Tent)", address = "D132DA", area = "Walse Castle", location_type="chest"),
LocationData("Walse Castle - Walse Castle Barrel (Phoenix Down)", address = "D132DE", area = "Walse Castle", location_type="chest"),
LocationData("Walse Tower - Walse Tower Chest (Silk robe)", address = "D132E2", area = "Walse Tower", location_type="chest"),
LocationData("Walse Tower - Walse Tower Chest (Maiden's Kiss)", address = "D132E6", area = "Walse Tower", location_type="chest"),
LocationData("Walse Tower - Walse Tower Chest (Silver Armlet)", address = "D132EA", area = "Walse Tower", location_type="chest"),
LocationData("Walse Tower - Walse Tower Chest (Ether)", address = "D132EE", area = "Walse Tower", location_type="chest"),
LocationData("Tycoon Meteor - Tycoon Meteor Chest (Phoenix Down)", address = "D132F2", area = "Tycoon Meteor", location_type="chest"),
LocationData("Karnak - Karnak Castle Chest MIB 1 (Heavy Spear)", address = "D132F6", area = "Karnak", location_type="chest"),
LocationData("Karnak - Karnak Castle Chest MIB 2 (Thunder Scroll)", address = "D132FA", area = "Karnak", location_type="chest"),
LocationData("Karnak - Karnak Castle Chest (2000 (1))", address = "D132FE", area = "Karnak", location_type="chest"),
LocationData("Karnak - Karnak Castle Chest MIB 3 (Elixir)", address = "D13302", area = "Karnak", location_type="chest"),
LocationData("Karnak - Karnak Castle Chest (Elixir (1))", address = "D13306", area = "Karnak", location_type="chest"),
LocationData("Karnak - Karnak Castle Chest (Elixir (2))", address = "D1330A", area = "Karnak", location_type="chest"),
LocationData("Karnak - Karnak Castle Chest (2000 (2))", address = "D1330E", area = "Karnak", location_type="chest"),
LocationData("Karnak - Karnak Castle Chest (Elixir (3))", address = "D13312", area = "Karnak", location_type="chest"),
LocationData("Karnak - Karnak Castle Chest (Elixir (4))", address = "D13316", area = "Karnak", location_type="chest"),
LocationData("Karnak - Karnak Castle Chest (Ribbon)", address = "D1331A", area = "Karnak", location_type="chest"),
LocationData("Karnak - Karnak Castle Chest (Shuriken)", address = "D1331E", area = "Karnak", location_type="chest"),
LocationData("Karnak - Karnak Castle Chest (2000 (3))", address = "D13322", area = "Karnak", location_type="chest"),
LocationData("Karnak - Karnak Castle Chest (Elixir (5))", address = "D13326", area = "Karnak", location_type="chest"),
LocationData("Karnak - Karnak Castle Chest (Elf Cape)", address = "D1332A", area = "Karnak", location_type="chest"),
LocationData("Karnak - Karnak Castle Chest (Guardian)", address = "D1332E", area = "Karnak", location_type="chest"),
LocationData("Karnak - Karnak Town Barrel (Fire Rod)", address = "D13332", area = "Karnak", location_type="chest"),
LocationData("Steamship - Steamship Chest (Cabin)", address = "D13336", area = "Steamship", location_type="chest"),
LocationData("Steamship - Steamship Chest (Phoenix Down)", address = "D1333A", area = "Steamship", location_type="chest"),
LocationData("Steamship - Steamship Chest (Elixir 1)", address = "D1333E", area = "Steamship", location_type="chest"),
LocationData("Steamship - Steamship Chest (GrnBeret)", address = "D13342", area = "Steamship", location_type="chest"),
LocationData("Steamship - Steamship Chest (Thief's Glove)", address = "D13346", area = "Steamship", location_type="chest"),
LocationData("Steamship - Steamship Chest (Elixir 2)", address = "D1334A", area = "Steamship", location_type="chest"),
LocationData("Ancient Library - Ancient Library Chest (Ether)", address = "D1334E", area = "Ancient Library", location_type="chest"),
LocationData("Ancient Library Lower - Ancient Library Chest (Phoenix Down)", address = "D13352", area = "Ancient Library Lower", location_type="chest"),
LocationData("Ancient Library Lower - Ancient Library Chest (Stealth Suit)", address = "D13356", area = "Ancient Library Lower", location_type="chest"),
LocationData("Jacole - Jacole Cave Chest (Shuriken)", address = "D1335A", area = "Jacole", location_type="chest"),
LocationData("Jacole - Jacole Cave Chest (Tent)", address = "D1335E", area = "Jacole", location_type="chest"),
LocationData("Ruined City - Ruined City Chest (Shuriken 1)", address = "D13362", area = "Ruined City", location_type="chest"),
LocationData("Ruined City - Ruined City Chest (Shuriken 2)", address = "D13366", area = "Ruined City", location_type="chest"),
LocationData("Ruined City - Ruined City Chest (Size)", address = "D1336A", area = "Ruined City", location_type="chest"),
LocationData("Flying Lonka Ruins - Flying Lonka Ruins Chest (Golden Armor)", address = "D1336E", area = "Flying Lonka Ruins", location_type="chest"),
LocationData("Flying Lonka Ruins - Flying Lonka Ruins Chest (Elixir)", address = "D13372", area = "Flying Lonka Ruins", location_type="chest"),
LocationData("Flying Lonka Ruins - Flying Lonka Ruins Chest (Phoenix Down)", address = "D13376", area = "Flying Lonka Ruins", location_type="chest"),
LocationData("Flying Lonka Ruins - Flying Lonka Ruins Chest (Golden Shield)", address = "D1337A", area = "Flying Lonka Ruins", location_type="chest"),
LocationData("Steamship - Steamship Chest (Mythril Glove)", address = "D1337E", area = "Steamship", location_type="chest"),
LocationData("Steamship - Steamship Chest (Elixir 3)", address = "D13382", area = "Steamship", location_type="chest"),
LocationData("Steamship - Steamship Chest (Full Moon)", address = "D13386", area = "Steamship", location_type="chest"),
LocationData("Flying Lonka Ruins - Flying Lonka Ruins Chest (Hi-Potion)", address = "D1338A", area = "Flying Lonka Ruins", location_type="chest"),
LocationData("Flying Lonka Ruins - Flying Lonka Ruins Chest (5000)", address = "D1338E", area = "Flying Lonka Ruins", location_type="chest"),
LocationData("Flying Lonka Ruins - Flying Lonka Ruins Chest (Shuriken)", address = "D13392", area = "Flying Lonka Ruins", location_type="chest"),
LocationData("Flying Lonka Ruins - Flying Lonka Ruins Chest (Ancient Sword)", address = "D13396", area = "Flying Lonka Ruins", location_type="chest"),
LocationData("Flying Lonka Ruins - Flying Lonka Ruins Chest (Full Moon)", address = "D1339A", area = "Flying Lonka Ruins", location_type="chest"),
LocationData("Flying Lonka Ruins - Flying Lonka Ruins Chest (Power Wrist)", address = "D1339E", area = "Flying Lonka Ruins", location_type="chest"),
LocationData("Flying Lonka Ruins - Flying Lonka Ruins Chest (Ether)", address = "D133A2", area = "Flying Lonka Ruins", location_type="chest"),
LocationData("Flying Lonka Ruins - Flying Lonka Ruins Chest (Cabin)", address = "D133A6", area = "Flying Lonka Ruins", location_type="chest"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (Ether 1)", address = "D133AA", area = "Exdeath's Castle", location_type="chest"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (Diamond Shield)", address = "D133AE", area = "Exdeath's Castle", location_type="chest"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (Ice Shield)", address = "D133B2", area = "Exdeath's Castle", location_type="chest"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (Ether 2)", address = "D133B6", area = "Exdeath's Castle", location_type="chest"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (Elixir 1)", address = "D133BA", area = "Exdeath's Castle", location_type="chest"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (Gale Bow)", address = "D133BE", area = "Exdeath's Castle", location_type="chest"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (IceBrand)", address = "D133C2", area = "Exdeath's Castle", location_type="chest"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (Kotetsu)", address = "D133C6", area = "Exdeath's Castle", location_type="chest"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (9900)", address = "D133CA", area = "Exdeath's Castle", location_type="chest"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (Elixir 2)", address = "D133CE", area = "Exdeath's Castle", location_type="chest"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (8000)", address = "D133D2", area = "Exdeath's Castle", location_type="chest"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (DblLance)", address = "D133D6", area = "Exdeath's Castle", location_type="chest"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (Partisan)", address = "D133DA", area = "Exdeath's Castle", location_type="chest"),
LocationData("Exdeath's Castle - Exdeath's Castle Chest (Pinwheel)", address = "D133DE", area = "Exdeath's Castle", location_type="chest"),
LocationData("Moogle Village - Moogle Cave Chest (4400)", address = "D133E2", area = "Moogle Village", location_type="chest"),
LocationData("Moogle Village - Moogle Cave Chest (Phoenix Down)", address = "D133E6", area = "Moogle Village", location_type="chest"),
LocationData("Moogle Village - Moogle Village Chest (Cabin)", address = "D133EA", area = "Moogle Village", location_type="chest"),
LocationData("Moogle Village - Moogle Village Chest (Dancing Dagger)", address = "D133EE", area = "Moogle Village", location_type="chest"),
LocationData("Moogle Village - Moogle Village Chest (1)", address = "D133F2", area = "Moogle Village", location_type="chest"),
LocationData("Moogle Village - Moogle Village Chest (10000)", address = "D133F6", area = "Moogle Village", location_type="chest"),
LocationData("Moogle Village - Moogle Village Chest (Phoenix Down)", address = "D133FA", area = "Moogle Village", location_type="chest"),
LocationData("Moogle Village - Moogle Village Chest (Ether)", address = "D133FE", area = "Moogle Village", location_type="chest"),
LocationData("Moogle Village - Moogle Village Chest (Elf Cape)", address = "D13402", area = "Moogle Village", location_type="chest"),
LocationData("Bal Castle - Bal Castle Chest (Angel Gwn)", address = "D13406", area = "Bal Castle", location_type="chest"),
LocationData("Bal Castle - Bal Castle Chest (Hero Drink)", address = "D1340A", area = "Bal Castle", location_type="chest"),
LocationData("Bal Castle - Bal Castle Chest (Exit)", address = "D1340E", area = "Bal Castle", location_type="chest"),
LocationData("Hiryuu Valley - Hiryuu Valley Skull (Bone Mail)", address = "D13412", area = "Hiryuu Valley", location_type="chest"),
LocationData("Hiryuu Valley - Hiryuu Valley Chest (5000)", address = "D13416", area = "Hiryuu Valley", location_type="chest"),
LocationData("Hiryuu Valley - Hiryuu Valley Chest (Cabin)", address = "D1341A", area = "Hiryuu Valley", location_type="chest"),
LocationData("Hiryuu Valley - Hiryuu Valley Chest (7000)", address = "D1341E", area = "Hiryuu Valley", location_type="chest"),
LocationData("Hiryuu Valley - Hiryuu Valley Chest (Hypno Helm)", address = "D13422", area = "Hiryuu Valley", location_type="chest"),
LocationData("Hiryuu Valley - Hiryuu Valley Chest (Air Blade)", address = "D13426", area = "Hiryuu Valley", location_type="chest"),
LocationData("Hiryuu Valley - Hiryuu Valley Chest (Phoenix Down)", address = "D1342A", area = "Hiryuu Valley", location_type="chest"),
LocationData("Surgate Castle - Surgate Castle Chest (5000)", address = "D1342E", area = "Surgate Castle", location_type="chest"),
LocationData("Surgate Castle - Surgate Castle Chest (Float)", address = "D13432", area = "Surgate Castle", location_type="chest"),
LocationData("Barrier Tower - Barrier Tower Chest MIB 1 (Drain Sword)", address = "D13436", area = "Barrier Tower", location_type="chest"),
LocationData("Barrier Tower - Barrier Tower Chest (9000)", address = "D1343A", area = "Barrier Tower", location_type="chest"),
LocationData("Barrier Tower - Barrier Tower Chest (18000)", address = "D1343E", area = "Barrier Tower", location_type="chest"),
LocationData("Barrier Tower - Barrier Tower Chest MIB 2 (Gold Hairpin)", address = "D13442", area = "Barrier Tower", location_type="chest"),
LocationData("Mua - Mua Town Barrel (Guardian)", address = "D13446", area = "Mua", location_type="chest"),
LocationData("Mua Forest - Mua Forest Chest (2500)", address = "D1344A", area = "Mua Forest", location_type="chest"),
LocationData("Mua Forest - Mua Forest Chest (Ether)", address = "D1344E", area = "Mua Forest", location_type="chest"),
LocationData("Mua Forest - Mua Forest Chest (4900)", address = "D13452", area = "Mua Forest", location_type="chest"),
LocationData("Mua Forest - Mua Forest Chest (Phoenix Down)", address = "D13456", area = "Mua Forest", location_type="chest"),
LocationData("Mua Forest - Mua Forest Chest (9500)", address = "D1345A", area = "Mua Forest", location_type="chest"),
LocationData("Mua Forest - Mua Forest Chest (Soot)", address = "D1345E", area = "Mua Forest", location_type="chest"),
LocationData("Mua Forest - Mua Forest Chest (Flametongue)", address = "D13462", area = "Mua Forest", location_type="chest"),
LocationData("Mua Forest - Mua Forest Chest (Cabin)", address = "D13466", area = "Mua Forest", location_type="chest"),
LocationData("Mua Forest - Mua Forest Chest (Giant Drink)", address = "D1346A", area = "Mua Forest", location_type="chest"),
LocationData("Mua Forest - Mua Forest Chest (Elixir)", address = "D1346E", area = "Mua Forest", location_type="chest"),
LocationData("Mua Forest - Mua Forest Chest (Morning Star)", address = "D13472", area = "Mua Forest", location_type="chest"),
LocationData("Solitary Island - Solitary Island Chest (Ether 1)", address = "D13476", area = "Solitary Island", location_type="chest"),
LocationData("Solitary Island - Solitary Island Chest (DragonFang)", address = "D1347A", area = "Solitary Island", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (Elixir 1)", address = "D1347E", area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (Elixir 2)", address = "D13482", area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest MIB 1 (Black Robe)", address = "D13486", area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (Thornlet)", address = "D1348A", area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest MIB 2 (DarkMatter)", address = "D1348E", area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest MIB 3 (Crystal Armor)", address = "D13492", area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (Cursed Ring)", address = "D13496", area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (Ice Shield)", address = "D1349A", area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (Flame Shield)", address = "D1349E", area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (DarkMatter 1)", address = "D134A2", area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (White Robe)", address = "D134A6", area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (DarkSuit)", address = "D134AA", area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (DarkMatter 2)", address = "D134AE", area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (DarkMatter 3)", address = "D134B2", area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (DarkMatter 4)", address = "D134B6", area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (9000)", address = "D134BA", area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (8000)", address = "D134BE", area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (Earth Hammer)", address = "D134C2", area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (10000)", address = "D134C6", area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (Cabin)", address = "D134CA", area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (Elixir 3)", address = "D134CE", area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (12000)", address = "D134D2", area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (DarkMatter 5)", address = "D134D6", area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (Elixir 4)", address = "D134DA", area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (DarkMatter 6)", address = "D134DE", area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (Guard Ring)", address = "D134E2", area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (Ribbon)", address = "D134E6", area = "Pyramid", location_type="chest"),
LocationData("Pyramid - Pyramid Chest (Gold Hairpin)", address = "D134EA", area = "Pyramid", location_type="chest"),
LocationData("Solitary Island - Solitary Island Chest (12000)", address = "D134EE", area = "Solitary Island", location_type="chest"),
LocationData("Solitary Island - Solitary Island Chest (Hi-Potion)", address = "D134F2", area = "Solitary Island", location_type="chest"),
LocationData("Solitary Island - Solitary Island Chest (Protect Drink)", address = "D134F6", area = "Solitary Island", location_type="chest"),
LocationData("Solitary Island - Solitary Island Chest (BeastKiller)", address = "D134FA", area = "Solitary Island", location_type="chest"),
LocationData("Solitary Island - Solitary Island Chest MIB 1 (RisingSun)", address = "D134FE", area = "Solitary Island", location_type="chest"),
LocationData("Solitary Island - Solitary Island Chest (Ether 2)", address = "D13502", area = "Solitary Island", location_type="chest"),
LocationData("Solitary Island - Solitary Island Chest MIB 2 (Guard Ring)", address = "D13506", area = "Solitary Island", location_type="chest"),
LocationData("Solitary Island - Solitary Island Chest (Crystal Helm)", address = "D1350A", area = "Solitary Island", location_type="chest"),
LocationData("Solitary Island - Solitary Island Chest (9000)", address = "D1350E", area = "Solitary Island", location_type="chest"),
LocationData("Solitary Island - Solitary Island Chest (Elixir)", address = "D13512", area = "Solitary Island", location_type="chest"),
LocationData("Solitary Island - Solitary Island Chest (DarkMatter)", address = "D13516", area = "Solitary Island", location_type="chest"),
LocationData("Solitary Island - Solitary Island Chest (Circlet)", address = "D1351A", area = "Solitary Island", location_type="chest"),
LocationData("Fork Tower - Fork Tower L. Chest (Ether)", address = "D1351E", area = "Fork Tower", location_type="chest"),
LocationData("Fork Tower - Fork Tower L. Chest (Wonder Wand)", address = "D13522", area = "Fork Tower", location_type="chest"),
LocationData("Fork Tower - Fork Tower R. Chest (Hi-Potion)", address = "D13526", area = "Fork Tower", location_type="chest"),
LocationData("Fork Tower - Fork Tower R. Chest (Defender Sword)", address = "D1352A", area = "Fork Tower", location_type="chest"),
LocationData("Great Trench - Great Trench Chest (Water Scroll)", address = "D1352E", area = "Great Trench", location_type="chest"),
LocationData("Great Trench - Great Trench Chest (Flame Ring)", address = "D13532", area = "Great Trench", location_type="chest"),
LocationData("Great Trench - Great Trench Chest (DragonFang)", address = "D13536", area = "Great Trench", location_type="chest"),
LocationData("Great Trench - Great Trench Chest (Ether)", address = "D1353A", area = "Great Trench", location_type="chest"),
LocationData("Great Trench - Great Trench Chest (Phoenix Down)", address = "D1353E", area = "Great Trench", location_type="chest"),
LocationData("Great Trench - Great Trench Chest (Kaiser Knuckles)", address = "D13542", area = "Great Trench", location_type="chest"),
LocationData("Istory Falls - Istory Falls Chest (Ether)", address = "D13546", area = "Istory Falls", location_type="chest"),
LocationData("Istory Falls - Istory Falls Chest (TurtleShell)", address = "D1354A", area = "Istory Falls", location_type="chest"),
LocationData("Istory Falls - Istory Falls Chest (Air Knife)", address = "D1354E", area = "Istory Falls", location_type="chest"),
LocationData("Istory Falls - Istory Falls Chest (Giant Drink)", address = "D13552", area = "Istory Falls", location_type="chest"),
LocationData("Istory Falls - Istory Falls Chest (RuneEdge)", address = "D13556", area = "Istory Falls", location_type="chest"),
LocationData("Istory Falls - Istory Falls Chest (Guard Ring)", address = "D1355A", area = "Istory Falls", location_type="chest"),
LocationData("Istory Falls - Istory Falls Chest (Wall Ring)", address = "D1355E", area = "Istory Falls", location_type="chest"),
LocationData("Istory Falls - Istory Falls Chest (Phoenix Down)", address = "D13562", area = "Istory Falls", location_type="chest"),
LocationData("Istory Falls - Istory Falls Chest (Enhancer)", address = "D13566", area = "Istory Falls", location_type="chest"),
LocationData("Istory Falls - Istory Falls Chest (12000)", address = "D1356A", area = "Istory Falls", location_type="chest"),
LocationData("Istory Falls - Istory Falls Chest (Artemis Bow)", address = "D1356E", area = "Istory Falls", location_type="chest"),
LocationData("Istory Falls - Istory Falls Chest (Pinwheel)", address = "D13572", area = "Istory Falls", location_type="chest"),
LocationData("Istory Falls - Istory Falls Chest (Aegis Shield)", address = "D13576", area = "Istory Falls", location_type="chest"),
LocationData("Istory Falls - Istory Falls Chest (Giant's Axe)", address = "D1357A", area = "Istory Falls", location_type="chest"),
LocationData("Phoenix Tower - Phoenix Tower Pot (5000)", address = "D1357E", area = "Phoenix Tower", location_type="chest"),
LocationData("Phoenix Tower - Phoenix Tower Pot (Phoenix Down 1)", address = "D13582", area = "Phoenix Tower", location_type="chest"),
LocationData("Phoenix Tower - Phoenix Tower Pot (10000)", address = "D13586", area = "Phoenix Tower", location_type="chest"),
LocationData("Phoenix Tower - Phoenix Tower Pot (Phoenix Down 2)", address = "D1358A", area = "Phoenix Tower", location_type="chest"),
LocationData("Phoenix Tower - Phoenix Tower Pot (Phoenix Down 3)", address = "D1358E", area = "Phoenix Tower", location_type="chest"),
LocationData("Phoenix Tower - Phoenix Tower Pot (15000)", address = "D13592", area = "Phoenix Tower", location_type="chest"),
LocationData("Phoenix Tower - Phoenix Tower Pot (20000)", address = "D13596", area = "Phoenix Tower", location_type="chest"),
LocationData("Phoenix Tower - Phoenix Tower Pot (Phoenix Down 4)", address = "D1359A", area = "Phoenix Tower", location_type="chest"),
LocationData("Phoenix Tower - Phoenix Tower Pot (Avis Killer)", address = "D1359E", area = "Phoenix Tower", location_type="chest"),
LocationData("Phoenix Tower - Phoenix Tower Pot (25000)", address = "D135A2", area = "Phoenix Tower", location_type="chest"),
LocationData("Mirage Village - Mirage Village Barrel (Thief Knife)", address = "D135A6", area = "Mirage Village", location_type="chest"),
LocationData("Rift (1 Tablet) - Rift (Ruins) Chest (Ether)", address = "D135AA", area = "Rift (1 Tablet)", location_type="chest"),
LocationData("Rift (1 Tablet) - Rift (Ruins) Chest (Cabin)", address = "D135AE", area = "Rift (1 Tablet)", location_type="chest"),
LocationData("Rift (1 Tablet) - Rift (Ruins) Chest (Elixir 1)", address = "D135B2", area = "Rift (1 Tablet)", location_type="chest"),
LocationData("Rift (1 Tablet) - Rift (Ruins) Chest (DarkMatter)", address = "D135B6", area = "Rift (1 Tablet)", location_type="chest"),
LocationData("Rift (1 Tablet) - Rift (Ruins) Chest (Elixir 2)", address = "D135BA", area = "Rift (1 Tablet)", location_type="chest"),
LocationData("Rift (1 Tablet) - Rift (Ruins) Chest (Drain Sword)", address = "D135BE", area = "Rift (1 Tablet)", location_type="chest"),
LocationData("Rift (1 Tablet) - Rift (Forest) Chest (DragonFang)", address = "D135C2", area = "Rift (1 Tablet)", location_type="chest"),
LocationData("Rift (1 Tablet) - Rift (Forest) Chest (Ribbon)", address = "D135C6", area = "Rift (1 Tablet)", location_type="chest"),
LocationData("Rift (1 Tablet) - Rift (Forest) Chest (Enhancer)", address = "D135CA", area = "Rift (1 Tablet)", location_type="chest"),
LocationData("Rift (1 Tablet) - Rift (Forest) Chest (Lillith Rod)", address = "D135CE", area = "Rift (1 Tablet)", location_type="chest"),
LocationData("Rift (2 Tablets) - Rift (Cave) Chest (Angel Ring)", address = "D135D2", area = "Rift (2 Tablets)", location_type="chest"),
LocationData("Rift (2 Tablets) - Rift (Cave) Chest (Coral Ring)", address = "D135D6", area = "Rift (2 Tablets)", location_type="chest"),
LocationData("Rift (3 Tablets) - Rift (Castle) Chest (Thor Hammer)", address = "D135DA", area = "Rift (3 Tablets)", location_type="chest"),
LocationData("Rift (3 Tablets) - Rift (Castle) Chest (Running Shoes)", address = "D135DE", area = "Rift (3 Tablets)", location_type="chest"),
LocationData("Rift (3 Tablets) - Rift (Castle) Chest (Red Shoes)", address = "D135E2", area = "Rift (3 Tablets)", location_type="chest"),
LocationData("Rift (3 Tablets) - Rift (Castle) Chest (Rainbow Dress)", address = "D135E6", area = "Rift (3 Tablets)", location_type="chest"),
LocationData("Rift (3 Tablets) - Rift (Castle) Chest (ManEater)", address = "D135EA", area = "Rift (3 Tablets)", location_type="chest"),
LocationData("Void - The Void Chest (Pinwheel 1)", address = "D135EE", area = "Void", location_type="chest"),
LocationData("Void - The Void Chest (Pinwheel 2)", address = "D135F2", area = "Void", location_type="chest"),
LocationData("Void - The Void Chest (Elixir)", address = "D135F6", area = "Void", location_type="chest"),
LocationData("Void - The Void Chest (Ragnarok)", address = "D135FA", area = "Void", location_type="chest"),
LocationData("Void - The Void Chest (Pinwheel 3)", address = "D135FE", area = "Void", location_type="chest"),
LocationData("Ancient Library Lower - Byblos (Boss)", address = "C0FB70", area = "Ancient Library Lower", location_type="key"),
LocationData("Wind Shrine - WingRaptor (Boss)", address = "C0FB72", area = "Wind Shrine",location_type="key"),
LocationData("Torna Canal - Karlabos (Boss)", address = "C0FB74", area = "Torna Canal",location_type="key"),
LocationData("Ship Graveyard - Siren (Boss)", address = "C0FB76", area = "Ship Graveyard",location_type="key"),
LocationData("North Mountain - Magisa & Forza (Boss)", address = "C0FB78", area = "North Mountain",location_type="key"),
LocationData("Walse Tower - Galura (Boss)", address = "C0FB7A", area = "Walse Tower",location_type="key"),
LocationData("Steamship - LiquiFlame (Boss)", address = "C0FB7C", area = "Steamship",location_type="key"),
LocationData("Karnak - Sergeant & DeathClaw (Boss)", address = "C0FB7E", area = "Karnak",location_type="key"),
LocationData("Desert of Shifting Sands - Sandworm (Boss)", address = "C0FB80", area = "Desert of Shifting Sands",location_type="key"),
LocationData("Tycoon Meteor - AdamanTiMi (Boss)", address = "C0FB82", area = "Tycoon Meteor",location_type="key"),
LocationData("Flying Lonka Ruins - Sol Cannon (Boss)", address = "C0FB84", area = "Flying Lonka Ruins",location_type="key"),
LocationData("Flying Lonka Ruins - ArchaeAvis (Boss)", address = "C0FB86", area = "Flying Lonka Ruins",location_type="key"),
LocationData("Lonka Meteor - Chim.Brain (Boss)", address = "C0FB88", area = "Lonka Meteor",location_type="key"),
LocationData("Walse Meteor - Puroboros (Boss)", address = "C0FB8A", area = "Walse Meteor",location_type="key"),
LocationData("Karnak Meteor - Titan (Boss)", address = "C0FB8C", area = "Karnak Meteor",location_type="key"),
LocationData("Ancient Library - Ifrit (Boss)", address = "C0FBB6", area = "Ancient Library",location_type="key"),
LocationData("Walse Castle - Shiva (Boss)", address = "C0FBB8", area = "Walse Castle",location_type="key"),
LocationData("Catapult - Crayclaw (Boss)", address = "C0FBBA", area = "Catapult",location_type="key"),
LocationData("Exdeath's Castle Lower - Gilgamesh 1 (Boss)", address = "C0FB8E", area = "Exdeath's Castle Lower",location_type="key"),
LocationData("Big Bridge - Gilgamesh 2 (Boss)", address = "C0FB90", area = "Big Bridge",location_type="key"),
LocationData("Moogle Waterway - Tyrasaurus (Boss)", address = "C0FB92", area = "Moogle Waterway",location_type="key"),
LocationData("Bal Castle - Abductor (Boss)", address = "C0FB94", area = "Bal Castle",location_type="key"),
LocationData("Hiryuu Valley - HiryuuPlant (Boss)", address = "C0FB96", area = "Hiryuu Valley",location_type="key"),
LocationData("Zeza Fleet - Gilgamesh 3 & Enkidou (Boss)", address = "C0FB98", area = "Zeza Fleet",location_type="key"),
LocationData("Barrier Tower - Atmos (Boss)", address = "C0FB9A", area = "Barrier Tower",location_type="key"),
LocationData("Mua Forest - Guardians (Boss)", address = "C0FB9C", area = "Mua Forest",location_type="key"),
LocationData("Exdeath's Castle - Carbunkle (Boss)", address = "C0FB9E", area = "Exdeath's Castle",location_type="key"),
LocationData("Exdeath's Castle - Gilgamesh 4 (Boss)", address = "C0FBA0", area = "Exdeath's Castle",location_type="key"),
LocationData("Tule Pass - Antlion (Boss)", address = "C0FBA2", area = "Tule Pass",location_type="key"),
LocationData("Pyramid - Merugene (Boss)", address = "C0FBA4", area = "Pyramid",location_type="key"),
LocationData("Bal Castle Lower - Odin (Boss)", address = "C0FBA6", area = "Bal Castle Lower",location_type="key"),
LocationData("Great Trench - Triton, Neregeid & Phobos (Boss)", address = "C0FBA8", area = "Great Trench",location_type="key"),
LocationData("Fork Tower - Omniscient (Boss)", address = "C0FBAA", area = "Fork Tower",location_type="key"),
LocationData("Fork Tower - Minotauros (Boss)", address = "C0FBAC", area = "Fork Tower",location_type="key"),
LocationData("Istory Falls - Leviathan (Boss)", address = "C0FBAE", area = "Istory Falls",location_type="key"),
LocationData("Solitary Island - Stalker (Boss)", address = "C0FBB0", area = "Solitary Island",location_type="key"),
LocationData("Walse Tower Sunken - GoGo (Boss)", address = "C0FBB2", area = "Walse Tower Sunken",location_type="key"),
LocationData("North Mountain (World 3) - Bahamut (Boss)", address = "C0FBB4", area = "North Mountain (World 3)", location_type="key"),
LocationData("ExDeath", address = "C0FFFF", area = "Void", location_type="key"),
]