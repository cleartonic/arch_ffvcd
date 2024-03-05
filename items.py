import os, sys
from BaseClasses import ItemClassification, Item
arch_item_offset = 352000000



EXDEATH_ITEM_ID = 1200
WORLD2_ACCESS_ITEM_ID = 1201
WORLD3_ACCESS_ITEM_ID = 1202

class ItemData:
    def __init__(self, item_id, classification, groups):
        self.groups = groups
        self.classification = classification
        self.id = None if item_id is None else item_id + arch_item_offset


def create_item(name: str, classification, item_data_id, player, groups) -> Item:
    return FFVCDItem(name, classification, item_data_id, player, groups)



def create_world_items(world):
    
    # add victory first, manually update location and item table
    exdeath = world.multiworld.get_location("ExDeath", world.player)    
    new_item = create_item("Victory",  
                                ItemClassification.progression, 
                                EXDEATH_ITEM_ID + arch_item_offset, 
                                world.player, ['Victory'])
    exdeath.place_locked_item(new_item)
    
    ##################    
    # add progression items
    ##################
    placed_items = []
    for key_item_name in [i for i in item_table if "Key Items" in item_table[i].groups]:
        item_data = item_table[key_item_name]
        if item_data.classification == ItemClassification.progression:
            new_item = create_item(key_item_name, item_data.classification, item_data.id, \
                                   world.player, item_data.groups)
            placed_items.append(new_item)


            
    ###############
    # FOUR JOB ENABLED
    # do not add abilities/crystals to pool if four job enabled
    ###############
    if world.multiworld.four_job[world.player]:
        starting_crystals = world.multiworld.random.sample([i for i in item_table \
                                                            if "Crystals" in item_table[i].groups],4)       
        for item_name in [i for i in item_table\
                              if "Magic" in item_table[i].groups or "Gil" in item_table[i].groups]:
            
            if item_name not in starting_crystals:
                
                item_data = item_table[item_name]
                new_item = create_item(item_name, item_data.classification, item_data.id, \
                                       world.player, item_data.groups)
                placed_items.append(new_item)



    ###############
    # FOUR JOB DISABLED
    # add crystals only if four job not enabled
    ###############
    else:
        
        # first choose starting crystal
        starting_crystals = [world.multiworld.random.choice([i for i in item_table \
                                                             if "Crystals" in item_table[i].groups])]

        for item_name in [i for i in item_table if "Crystals" in item_table[i].groups or \
                              "Abilities" in item_table[i].groups or "Magic" in item_table[i].groups\
                                  or "Gil" in item_table[i].groups]:
            if item_name not in starting_crystals:
                item_data = item_table[item_name]
                new_item = create_item(item_name, item_data.classification, item_data.id, \
                                       world.player, item_data.groups)
                placed_items.append(new_item)

        


    
    # then calculate remaining    
    locations_this_world = [i for i in world.multiworld.get_locations(world.player)]
    # this has a minus 1 at the end to accommodate special locations like "ExDeath" at the end
    
    item_count_to_place = len(locations_this_world) - len(placed_items) - 1
    for item_name in world.multiworld.random.sample([i for i in item_table if "Fungible" in \
                                                     item_table[i].groups], item_count_to_place):
        item_data = item_table[item_name]
        new_item = create_item(item_name, item_data.classification, item_data.id, \
                                                   world.player, item_data.groups)
            
        placed_items.append(new_item)

    world.random.shuffle(placed_items)
    # add remaining to itempool
    for new_item in placed_items:
        world.multiworld.itempool.append(new_item)
        
        
    return starting_crystals

item_table = {
    "Knight Crystal" : ItemData(100, ItemClassification.useful, ["Unique", "Crystals"]),
    "Monk Crystal" : ItemData(101, ItemClassification.useful, ["Unique", "Crystals"]),
    "Thief Crystal" : ItemData(102, ItemClassification.useful, ["Unique", "Crystals"]),
    "Dragoon Crystal" : ItemData(103, ItemClassification.useful, ["Unique", "Crystals"]),
    "Ninja Crystal" : ItemData(104, ItemClassification.useful, ["Unique", "Crystals"]),
    "Samurai Crystal" : ItemData(105, ItemClassification.useful, ["Unique", "Crystals"]),
    "Berserker Crystal" : ItemData(106, ItemClassification.useful, ["Unique", "Crystals"]),
    "Hunter Crystal" : ItemData(107, ItemClassification.useful, ["Unique", "Crystals"]),
    "MysticKnight Crystal" : ItemData(108, ItemClassification.useful, ["Unique", "Crystals"]),
    "WhiteMage Crystal" : ItemData(109, ItemClassification.useful, ["Unique", "Crystals"]),
    "BlackMage Crystal" : ItemData(110, ItemClassification.useful, ["Unique", "Crystals"]),
    "TimeMage Crystal" : ItemData(111, ItemClassification.useful, ["Unique", "Crystals"]),
    "Summoner Crystal" : ItemData(112, ItemClassification.useful, ["Unique", "Crystals"]),
    "BlueMage Crystal" : ItemData(113, ItemClassification.useful, ["Unique", "Crystals"]),
    "RedMage Crystal" : ItemData(114, ItemClassification.useful, ["Unique", "Crystals"]),
    "Trainer Crystal" : ItemData(115, ItemClassification.useful, ["Unique", "Crystals"]),
    "Chemist Crystal" : ItemData(116, ItemClassification.useful, ["Unique", "Crystals"]),
    "Geomancer Crystal" : ItemData(117, ItemClassification.useful, ["Unique", "Crystals"]),
    "Bard Crystal" : ItemData(118, ItemClassification.useful, ["Unique", "Crystals"]),
    "Dancer Crystal" : ItemData(119, ItemClassification.useful, ["Unique", "Crystals"]),
    "Mimic Crystal" : ItemData(120, ItemClassification.useful, ["Unique", "Crystals"]),
    "Freelancer Crystal" : ItemData(121, ItemClassification.useful, ["Unique", "Crystals"]),
        
    "Ice Sword Magic" : ItemData(201, ItemClassification.useful, ["Unique","Magic"]),
    "Bolt Sword Magic" : ItemData(202, ItemClassification.useful, ["Unique","Magic"]),
    "Venom Sword Magic" : ItemData(203, ItemClassification.useful, ["Unique","Magic"]),
    "Mute Sword Magic" : ItemData(204, ItemClassification.useful, ["Unique","Magic"]),
    "Sleep Sword Magic" : ItemData(205, ItemClassification.useful, ["Unique","Magic"]),
    "Fire2 Sword Magic" : ItemData(206, ItemClassification.useful, ["Unique","Magic"]),
    "Ice2 Sword Magic" : ItemData(207, ItemClassification.useful, ["Unique","Magic"]),
    "Bolt2 Sword Magic" : ItemData(208, ItemClassification.useful, ["Unique","Magic"]),
    "Drain Sword Magic" : ItemData(209, ItemClassification.useful, ["Unique","Magic"]),
    "Break Sword Magic" : ItemData(210, ItemClassification.useful, ["Unique","Magic"]),
    "Bio Sword Magic" : ItemData(211, ItemClassification.useful, ["Unique","Magic"]),
    "Fire3 Sword Magic" : ItemData(212, ItemClassification.useful, ["Unique","Magic"]),
    "Ice3 Sword Magic" : ItemData(213, ItemClassification.useful, ["Unique","Magic"]),
    "Bolt3 Sword Magic" : ItemData(214, ItemClassification.useful, ["Unique","Magic"]),
    "Holy Sword Magic" : ItemData(215, ItemClassification.useful, ["Unique","Magic"]),
    "Flare Sword Magic" : ItemData(216, ItemClassification.useful, ["Unique","Magic"]),
    "Psych Sword Magic" : ItemData(217, ItemClassification.useful, ["Unique","Magic"]),
    "Cure White Magic" : ItemData(218, ItemClassification.useful, ["Unique","Magic"]),
    "Scan White Magic" : ItemData(219, ItemClassification.useful, ["Unique","Magic"]),
    "Antdt White Magic" : ItemData(220, ItemClassification.useful, ["Unique","Magic"]),
    "Mute White Magic" : ItemData(221, ItemClassification.useful, ["Unique","Magic"]),
    "Armor White Magic" : ItemData(222, ItemClassification.useful, ["Unique","Magic"]),
    "Size White Magic" : ItemData(223, ItemClassification.useful, ["Unique","Magic"]),
    "Cure2 White Magic" : ItemData(224, ItemClassification.useful, ["Unique","Magic"]),
    "Life White Magic" : ItemData(225, ItemClassification.useful, ["Unique","Magic"]),
    "Charm White Magic" : ItemData(226, ItemClassification.useful, ["Unique","Magic"]),
    "Image White Magic" : ItemData(227, ItemClassification.useful, ["Unique","Magic"]),
    "Shell White Magic" : ItemData(228, ItemClassification.useful, ["Unique","Magic"]),
    "Heal White Magic" : ItemData(229, ItemClassification.useful, ["Unique","Magic"]),
    "Cure3 White Magic" : ItemData(230, ItemClassification.useful, ["Unique","Magic"]),
    "Wall White Magic" : ItemData(231, ItemClassification.useful, ["Unique","Magic"]),
    "Bersk White Magic" : ItemData(232, ItemClassification.useful, ["Unique","Magic"]),
    "Life2 White Magic" : ItemData(233, ItemClassification.useful, ["Unique","Magic"]),
    "Holy White Magic" : ItemData(234, ItemClassification.useful, ["Unique","Magic"]),
    "Dispel White Magic" : ItemData(235, ItemClassification.useful, ["Unique","Magic"]),
    "Fire Black Magic" : ItemData(236, ItemClassification.useful, ["Unique","Magic"]),
    "Ice Black Magic" : ItemData(237, ItemClassification.useful, ["Unique","Magic"]),
    "Bolt Black Magic" : ItemData(238, ItemClassification.useful, ["Unique","Magic"]),
    "Venom Black Magic" : ItemData(239, ItemClassification.useful, ["Unique","Magic"]),
    "Sleep Black Magic" : ItemData(240, ItemClassification.useful, ["Unique","Magic"]),
    "Toad Black Magic" : ItemData(241, ItemClassification.useful, ["Unique","Magic"]),
    "Fire2 Black Magic" : ItemData(242, ItemClassification.useful, ["Unique","Magic"]),
    "Ice2 Black Magic" : ItemData(243, ItemClassification.useful, ["Unique","Magic"]),
    "Bolt2 Black Magic" : ItemData(244, ItemClassification.useful, ["Unique","Magic"]),
    "Drain Black Magic" : ItemData(245, ItemClassification.useful, ["Unique","Magic"]),
    "Break Black Magic" : ItemData(246, ItemClassification.useful, ["Unique","Magic"]),
    "Bio Black Magic" : ItemData(247, ItemClassification.useful, ["Unique","Magic"]),
    "Fire3 Black Magic" : ItemData(248, ItemClassification.useful, ["Unique","Magic"]),
    "Ice3 Black Magic" : ItemData(249, ItemClassification.useful, ["Unique","Magic"]),
    "Bolt3 Black Magic" : ItemData(250, ItemClassification.useful, ["Unique","Magic"]),
    "Flare Black Magic" : ItemData(251, ItemClassification.useful, ["Unique","Magic"]),
    "Doom Black Magic" : ItemData(252, ItemClassification.useful, ["Unique","Magic"]),
    "Psych Black Magic" : ItemData(253, ItemClassification.useful, ["Unique","Magic"]),
    "Slow Time Magic" : ItemData(255, ItemClassification.useful, ["Unique","Magic"]),
    "Regen Time Magic" : ItemData(256, ItemClassification.useful, ["Unique","Magic"]),
    "Void Time Magic" : ItemData(257, ItemClassification.useful, ["Unique","Magic"]),
    "Haste Time Magic" : ItemData(258, ItemClassification.useful, ["Unique","Magic"]),
    "Float Time Magic" : ItemData(259, ItemClassification.useful, ["Unique","Magic"]),
    "Demi Time Magic" : ItemData(260, ItemClassification.useful, ["Unique","Magic"]),
    "Stop Time Magic" : ItemData(261, ItemClassification.useful, ["Unique","Magic"]),
    "Comet Time Magic" : ItemData(263, ItemClassification.useful, ["Unique","Magic"]),
    "Slow2 Time Magic" : ItemData(264, ItemClassification.useful, ["Unique","Magic"]),
    "Reset Time Magic" : ItemData(265, ItemClassification.useful, ["Unique","Magic"]),
    "Qrter Time Magic" : ItemData(266, ItemClassification.useful, ["Unique","Magic"]),
    "Hast2 Time Magic" : ItemData(267, ItemClassification.useful, ["Unique","Magic"]),
    "Old Time Magic" : ItemData(268, ItemClassification.useful, ["Unique","Magic"]),
    "Meteo Time Magic" : ItemData(269, ItemClassification.useful, ["Unique","Magic"]),
    "Quick Time Magic" : ItemData(270, ItemClassification.useful, ["Unique","Magic"]),
    "Xzone Time Magic" : ItemData(271, ItemClassification.useful, ["Unique","Magic"]),
    "Chocob Esper Magic" : ItemData(272, ItemClassification.useful, ["Unique","Magic"]),
    "Sylph Esper Magic" : ItemData(273, ItemClassification.useful, ["Unique","Magic"]),
    "Remora Esper Magic" : ItemData(274, ItemClassification.useful, ["Unique","Magic"]),
    "Shiva Esper Magic" : ItemData(275, ItemClassification.useful, ["Unique","Magic"]),
    "Ramuh Esper Magic" : ItemData(276, ItemClassification.useful, ["Unique","Magic"]),
    "Ifrit Esper Magic" : ItemData(277, ItemClassification.useful, ["Unique","Magic"]),
    "Titan Esper Magic" : ItemData(278, ItemClassification.useful, ["Unique","Magic"]),
    "Golem Esper Magic" : ItemData(279, ItemClassification.useful, ["Unique","Magic"]),
    "Shoat Esper Magic" : ItemData(280, ItemClassification.useful, ["Unique","Magic"]),
    "Crbnkl Esper Magic" : ItemData(281, ItemClassification.useful, ["Unique","Magic"]),
    "Syldra Esper Magic" : ItemData(282, ItemClassification.useful, ["Unique","Magic"]),
    "Odin Esper Magic" : ItemData(283, ItemClassification.useful, ["Unique","Magic"]),
    "Phenix Esper Magic" : ItemData(284, ItemClassification.useful, ["Unique","Magic"]),
    "Levia Esper Magic" : ItemData(285, ItemClassification.useful, ["Unique","Magic"]),
    "Bahmut Esper Magic" : ItemData(286, ItemClassification.useful, ["Unique","Magic"]),
    "Power Song Magic" : ItemData(287, ItemClassification.useful, ["Unique","Magic"]),
    "Speed Song Magic" : ItemData(288, ItemClassification.useful, ["Unique","Magic"]),
    "Vitality Song Magic" : ItemData(289, ItemClassification.useful, ["Unique","Magic"]),
    "Magic Song Magic" : ItemData(290, ItemClassification.useful, ["Unique","Magic"]),
    "Hero Song Magic" : ItemData(291, ItemClassification.useful, ["Unique","Magic"]),
    "Requiem Song Magic" : ItemData(292, ItemClassification.useful, ["Unique","Magic"]),
    "Love Song Magic" : ItemData(293, ItemClassification.useful, ["Unique","Magic"]),
    "Charm Song Magic" : ItemData(294, ItemClassification.useful, ["Unique","Magic"]),
    "Condemn Blue Magic" : ItemData(295, ItemClassification.useful, ["Unique","Magic"]),
    "Roulette Blue Magic" : ItemData(296, ItemClassification.useful, ["Unique","Magic"]),
    "AquaRake Blue Magic" : ItemData(297, ItemClassification.useful, ["Unique","Magic"]),
    "L5 Doom Blue Magic" : ItemData(298, ItemClassification.useful, ["Unique","Magic"]),
    "L4 Qrter Blue Magic" : ItemData(299, ItemClassification.useful, ["Unique","Magic"]),
    "L2 Old Blue Magic" : ItemData(300, ItemClassification.useful, ["Unique","Magic"]),
    "L3 Flare Blue Magic" : ItemData(301, ItemClassification.useful, ["Unique","Magic"]),
    "FrogSong Blue Magic" : ItemData(302, ItemClassification.useful, ["Unique","Magic"]),
    "TinySong Blue Magic" : ItemData(303, ItemClassification.useful, ["Unique","Magic"]),
    "Flash Blue Magic" : ItemData(304, ItemClassification.useful, ["Unique","Magic"]),
    "Time Slip Blue Magic" : ItemData(305, ItemClassification.useful, ["Unique","Magic"]),
    "MoonFlut Blue Magic" : ItemData(306, ItemClassification.useful, ["Unique","Magic"]),
    "DethClaw Blue Magic" : ItemData(307, ItemClassification.useful, ["Unique","Magic"]),
    "Aero Blue Magic" : ItemData(308, ItemClassification.useful, ["Unique","Magic"]),
    "Aero 2 Blue Magic" : ItemData(309, ItemClassification.useful, ["Unique","Magic"]),
    "Aero 3 Blue Magic" : ItemData(310, ItemClassification.useful, ["Unique","Magic"]),
    "Emission Blue Magic" : ItemData(311, ItemClassification.useful, ["Unique","Magic"]),
    "GblinPnch Blue Magic" : ItemData(312, ItemClassification.useful, ["Unique","Magic"]),
    "DrkShock Blue Magic" : ItemData(313, ItemClassification.useful, ["Unique","Magic"]),
    "GuardOff Blue Magic" : ItemData(314, ItemClassification.useful, ["Unique","Magic"]),
    "Fusion Blue Magic" : ItemData(315, ItemClassification.useful, ["Unique","Magic"]),
    "MindBlst Blue Magic" : ItemData(316, ItemClassification.useful, ["Unique","Magic"]),
    "Vampire Blue Magic" : ItemData(317, ItemClassification.useful, ["Unique","Magic"]),
    "Hammer Blue Magic" : ItemData(318, ItemClassification.useful, ["Unique","Magic"]),
    "BigGuard Blue Magic" : ItemData(319, ItemClassification.useful, ["Unique","Magic"]),
    "Exploder Blue Magic" : ItemData(320, ItemClassification.useful, ["Unique","Magic"]),
    "???? Blue Magic" : ItemData(321, ItemClassification.useful, ["Unique","Magic"]),
    "Blowfish Blue Magic" : ItemData(322, ItemClassification.useful, ["Unique","Magic"]),
    "WhiteWind Blue Magic" : ItemData(323, ItemClassification.useful, ["Unique","Magic"]),
    "Missile Blue Magic" : ItemData(324, ItemClassification.useful, ["Unique","Magic"]),
        
    "Kick Ability" : ItemData(400, ItemClassification.useful, ["Unique","Abilities"]),
    "BuildUp Ability" : ItemData(401, ItemClassification.useful, ["Unique","Abilities"]),
    "Mantra Ability" : ItemData(402, ItemClassification.useful, ["Unique","Abilities"]),
    "Escape Ability" : ItemData(403, ItemClassification.useful, ["Unique","Abilities"]),
    "Steal Ability" : ItemData(404, ItemClassification.useful, ["Unique","Abilities"]),
    "Mug Ability" : ItemData(405, ItemClassification.useful, ["Unique","Abilities"]),
    "Jump Ability" : ItemData(406, ItemClassification.useful, ["Unique","Abilities"]),
    "DrgnSwd Ability" : ItemData(407, ItemClassification.useful, ["Unique","Abilities"]),
    "Smoke Ability" : ItemData(408, ItemClassification.useful, ["Unique","Abilities"]),
    "Image Ability" : ItemData(409, ItemClassification.useful, ["Unique","Abilities"]),
    "Throw Ability" : ItemData(410, ItemClassification.useful, ["Unique","Abilities"]),
    "SwdSlap Ability" : ItemData(411, ItemClassification.useful, ["Unique","Abilities"]),
    "GilToss Ability" : ItemData(412, ItemClassification.useful, ["Unique","Abilities"]),
    "Slash Ability" : ItemData(413, ItemClassification.useful, ["Unique","Abilities"]),
    "Animals Ability" : ItemData(414, ItemClassification.useful, ["Unique","Abilities"]),
    "Aim Ability" : ItemData(415, ItemClassification.useful, ["Unique","Abilities"]),
    "X-Fight Ability" : ItemData(416, ItemClassification.useful, ["Unique","Abilities"]),
    "Conjure Ability" : ItemData(417, ItemClassification.useful, ["Unique","Abilities"]),
    "Observe Ability" : ItemData(418, ItemClassification.useful, ["Unique","Abilities"]),
    "Analyze Ability" : ItemData(419, ItemClassification.useful, ["Unique","Abilities"]),
    "Tame Ability" : ItemData(420, ItemClassification.useful, ["Unique","Abilities"]),
    "Control Ability" : ItemData(421, ItemClassification.useful, ["Unique","Abilities"]),
    "Catch Ability" : ItemData(422, ItemClassification.useful, ["Unique","Abilities"]),
    "Mix Ability" : ItemData(423, ItemClassification.useful, ["Unique","Abilities"]),
    "Drink Ability" : ItemData(424, ItemClassification.useful, ["Unique","Abilities"]),
    "Pray Ability" : ItemData(425, ItemClassification.useful, ["Unique","Abilities"]),
    "Revive Ability" : ItemData(426, ItemClassification.useful, ["Unique","Abilities"]),
    "Terrain Ability" : ItemData(427, ItemClassification.useful, ["Unique","Abilities"]),
    "Hide Ability" : ItemData(428, ItemClassification.useful, ["Unique","Abilities"]),
    "Sing Ability" : ItemData(429, ItemClassification.useful, ["Unique","Abilities"]),
    "Flirt Ability" : ItemData(430, ItemClassification.useful, ["Unique","Abilities"]),
    "Dance Ability" : ItemData(431, ItemClassification.useful, ["Unique","Abilities"]),
    "Mimic Ability" : ItemData(432, ItemClassification.useful, ["Unique","Abilities"]),
    "MgcSwrd Lv.1 Ability" : ItemData(433, ItemClassification.useful, ["Unique","Abilities"]),
    "MgcSwrd Lv.2 Ability" : ItemData(434, ItemClassification.useful, ["Unique","Abilities"]),
    "MgcSwrd Lv.3 Ability" : ItemData(435, ItemClassification.useful, ["Unique","Abilities"]),
    "MgcSwrd Lv.4 Ability" : ItemData(436, ItemClassification.useful, ["Unique","Abilities"]),
    "MgcSwrd Lv.5 Ability" : ItemData(437, ItemClassification.useful, ["Unique","Abilities"]),
    "MgcSwrd Lv.6 Ability" : ItemData(438, ItemClassification.useful, ["Unique","Abilities"]),
    "White Lv.1 Ability" : ItemData(439, ItemClassification.useful, ["Unique","Abilities"]),
    "White Lv.2 Ability" : ItemData(440, ItemClassification.useful, ["Unique","Abilities"]),
    "White Lv.3 Ability" : ItemData(441, ItemClassification.useful, ["Unique","Abilities"]),
    "White Lv.4 Ability" : ItemData(442, ItemClassification.useful, ["Unique","Abilities"]),
    "White Lv.5 Ability" : ItemData(443, ItemClassification.useful, ["Unique","Abilities"]),
    "White Lv.6 Ability" : ItemData(444, ItemClassification.useful, ["Unique","Abilities"]),
    "Black Lv.1 Ability" : ItemData(445, ItemClassification.useful, ["Unique","Abilities"]),
    "Black Lv.2 Ability" : ItemData(446, ItemClassification.useful, ["Unique","Abilities"]),
    "Black Lv.3 Ability" : ItemData(447, ItemClassification.useful, ["Unique","Abilities"]),
    "Black Lv.4 Ability" : ItemData(448, ItemClassification.useful, ["Unique","Abilities"]),
    "Black Lv.5 Ability" : ItemData(449, ItemClassification.useful, ["Unique","Abilities"]),
    "Black Lv.6 Ability" : ItemData(450, ItemClassification.useful, ["Unique","Abilities"]),
    "Time Lv.1 Ability" : ItemData(451, ItemClassification.useful, ["Unique","Abilities"]),
    "Time Lv.2 Ability" : ItemData(452, ItemClassification.useful, ["Unique","Abilities"]),
    "Time Lv.3 Ability" : ItemData(453, ItemClassification.useful, ["Unique","Abilities"]),
    "Time Lv.4 Ability" : ItemData(454, ItemClassification.useful, ["Unique","Abilities"]),
    "Time Lv.5 Ability" : ItemData(455, ItemClassification.useful, ["Unique","Abilities"]),
    "Time Lv.6 Ability" : ItemData(456, ItemClassification.useful, ["Unique","Abilities"]),
    "Summon Lv.1 Ability" : ItemData(457, ItemClassification.useful, ["Unique","Abilities"]),
    "Summon Lv.2 Ability" : ItemData(458, ItemClassification.useful, ["Unique","Abilities"]),
    "Summon Lv.3 Ability" : ItemData(459, ItemClassification.useful, ["Unique","Abilities"]),
    "Summon Lv.4 Ability" : ItemData(460, ItemClassification.useful, ["Unique","Abilities"]),
    "Summon Lv.5 Ability" : ItemData(461, ItemClassification.useful, ["Unique","Abilities"]),
    "Red Lv.1 Ability" : ItemData(462, ItemClassification.useful, ["Unique","Abilities"]),
    "Red Lv.2 Ability" : ItemData(463, ItemClassification.useful, ["Unique","Abilities"]),
    "Red Lv.3 Ability" : ItemData(464, ItemClassification.useful, ["Unique","Abilities"]),
    "X-Magic Ability" : ItemData(465, ItemClassification.useful, ["Unique","Abilities"]),
    "Blue Ability" : ItemData(466, ItemClassification.useful, ["Unique","Abilities"]),
    "Equip Shield Ability" : ItemData(467, ItemClassification.useful, ["Unique","Abilities"]),
    "Equip Armors Ability" : ItemData(468, ItemClassification.useful, ["Unique","Abilities"]),
    "Equip Ribbon Ability" : ItemData(469, ItemClassification.useful, ["Unique","Abilities"]),
    "Equip Swords Ability" : ItemData(470, ItemClassification.useful, ["Unique","Abilities"]),
    "Equip Spears Ability" : ItemData(471, ItemClassification.useful, ["Unique","Abilities"]),
    "Equip Katana Ability" : ItemData(472, ItemClassification.useful, ["Unique","Abilities"]),
    "Equip Axes Ability" : ItemData(473, ItemClassification.useful, ["Unique","Abilities"]),
    "Equip Bows Ability" : ItemData(474, ItemClassification.useful, ["Unique","Abilities"]),
    "Equip Whips Ability" : ItemData(475, ItemClassification.useful, ["Unique","Abilities"]),
    "Equip Harps Ability" : ItemData(476, ItemClassification.useful, ["Unique","Abilities"]),
    "Agility Ability" : ItemData(477, ItemClassification.useful, ["Unique","Abilities"]),
    "HP +10% Ability" : ItemData(478, ItemClassification.useful, ["Unique","Abilities"]),
    "HP +20% Ability" : ItemData(479, ItemClassification.useful, ["Unique","Abilities"]),
    "HP +30% Ability" : ItemData(480, ItemClassification.useful, ["Unique","Abilities"]),
    "MP +10% Ability" : ItemData(481, ItemClassification.useful, ["Unique","Abilities"]),
    "MP +30% Ability" : ItemData(482, ItemClassification.useful, ["Unique","Abilities"]),
    "Brawl Ability" : ItemData(483, ItemClassification.useful, ["Unique","Abilities"]),
    "Dbl Grip Ability" : ItemData(484, ItemClassification.useful, ["Unique","Abilities"]),
    "2-Wield Ability" : ItemData(485, ItemClassification.useful, ["Unique","Abilities"]),
    "Medicine Ability" : ItemData(486, ItemClassification.useful, ["Unique","Abilities"]),
    "Cover Ability" : ItemData(487, ItemClassification.useful, ["Unique","Abilities"]),
    "Counter Ability" : ItemData(488, ItemClassification.useful, ["Unique","Abilities"]),
    "Evade Ability" : ItemData(489, ItemClassification.useful, ["Unique","Abilities"]),
    "Barrier Ability" : ItemData(490, ItemClassification.useful, ["Unique","Abilities"]),
    "Berserk Ability" : ItemData(491, ItemClassification.useful, ["Unique","Abilities"]),
    "Caution Ability" : ItemData(492, ItemClassification.useful, ["Unique","Abilities"]),
    "Preemptive Ability" : ItemData(493, ItemClassification.useful, ["Unique","Abilities"]),
    "DmgFloor Ability" : ItemData(494, ItemClassification.useful, ["Unique","Abilities"]),
    "Equip Rods Ability" : ItemData(495, ItemClassification.useful, ["Unique","Abilities"]),
    
        
    "Knife Item" : ItemData(600, ItemClassification.useful, ["Fungible", "Item"]),
    "Dagger Item" : ItemData(601, ItemClassification.useful, ["Fungible", "Item"]),
    "Mythril Knife Item" : ItemData(602, ItemClassification.useful, ["Fungible", "Item"]),
    "Kunai Item" : ItemData(603, ItemClassification.useful, ["Fungible", "Item"]),
    "Mage Masher Item" : ItemData(604, ItemClassification.useful, ["Fungible", "Item"]),
    "Guardian Item" : ItemData(605, ItemClassification.useful, ["Fungible", "Item"]),
    "Kodachi Item" : ItemData(606, ItemClassification.useful, ["Fungible", "Item"]),
    "Orialcon Item" : ItemData(607, ItemClassification.useful, ["Fungible", "Item"]),
    "Air Knife Item" : ItemData(608, ItemClassification.useful, ["Fungible", "Item"]),
    "Assassin Item" : ItemData(609, ItemClassification.useful, ["Fungible", "Item"]),
    "Hardened Dagger Item" : ItemData(610, ItemClassification.useful, ["Fungible", "Item"]),
    "Broadsword Item" : ItemData(611, ItemClassification.useful, ["Fungible", "Item"]),
    "RegalCut Item" : ItemData(612, ItemClassification.useful, ["Fungible", "Item"]),
    "Mythril Sword Item" : ItemData(613, ItemClassification.useful, ["Fungible", "Item"]),
    "Coral Sword Item" : ItemData(614, ItemClassification.useful, ["Fungible", "Item"]),
    "Ancient Sword Item" : ItemData(615, ItemClassification.useful, ["Fungible", "Item"]),
    "Epee Sword Item" : ItemData(616, ItemClassification.useful, ["Fungible", "Item"]),
    "Slumber Sword Item" : ItemData(617, ItemClassification.useful, ["Fungible", "Item"]),
    "Defender Sword Item" : ItemData(618, ItemClassification.useful, ["Fungible", "Item"]),
    "Excalibur Item" : ItemData(619, ItemClassification.useful, ["Fungible", "Item"]),
    "Ragnarok Item" : ItemData(620, ItemClassification.useful, ["Fungible", "Item"]),
    "Javelin Item" : ItemData(621, ItemClassification.useful, ["Fungible", "Item"]),
    "Spear Item" : ItemData(622, ItemClassification.useful, ["Fungible", "Item"]),
    "Mythril Spear Item" : ItemData(623, ItemClassification.useful, ["Fungible", "Item"]),
    "Trident Item" : ItemData(624, ItemClassification.useful, ["Fungible", "Item"]),
    "Wind Spear Item" : ItemData(625, ItemClassification.useful, ["Fungible", "Item"]),
    "Partisan Item" : ItemData(626, ItemClassification.useful, ["Fungible", "Item"]),
    "Heavy Spear Item" : ItemData(627, ItemClassification.useful, ["Fungible", "Item"]),
    "DblLance Item" : ItemData(628, ItemClassification.useful, ["Fungible", "Item"]),
    "Holy Lance Item" : ItemData(629, ItemClassification.useful, ["Fungible", "Item"]),
    "Dragoon Lance Item" : ItemData(630, ItemClassification.useful, ["Fungible", "Item"]),
    "Battle Axe Item" : ItemData(631, ItemClassification.useful, ["Fungible", "Item"]),
    "Mythril Hammer Item" : ItemData(632, ItemClassification.useful, ["Fungible", "Item"]),
    "Ogre Killer Item" : ItemData(633, ItemClassification.useful, ["Fungible", "Item"]),
    "War Hammer Item" : ItemData(634, ItemClassification.useful, ["Fungible", "Item"]),
    "Venom Axe Item" : ItemData(635, ItemClassification.useful, ["Fungible", "Item"]),
    "Earth Hammer Item" : ItemData(636, ItemClassification.useful, ["Fungible", "Item"]),
    "Rune Axe Item" : ItemData(637, ItemClassification.useful, ["Fungible", "Item"]),
    "Thor Hammer Item" : ItemData(638, ItemClassification.useful, ["Fungible", "Item"]),
    "Katana Item" : ItemData(639, ItemClassification.useful, ["Fungible", "Item"]),
    "Air Blade Item" : ItemData(640, ItemClassification.useful, ["Fungible", "Item"]),
    "Kotetsu Item" : ItemData(641, ItemClassification.useful, ["Fungible", "Item"]),
    "Bizen Item" : ItemData(642, ItemClassification.useful, ["Fungible", "Item"]),
    "Forged Item" : ItemData(643, ItemClassification.useful, ["Fungible", "Item"]),
    "Murasume Item" : ItemData(644, ItemClassification.useful, ["Fungible", "Item"]),
    "Masamune Item" : ItemData(645, ItemClassification.useful, ["Fungible", "Item"]),
    "Tempest Item" : ItemData(646, ItemClassification.useful, ["Fungible", "Item"]),
    "Rod Item" : ItemData(647, ItemClassification.useful, ["Fungible", "Item"]),
    "Fire Rod Item" : ItemData(648, ItemClassification.useful, ["Fungible", "Item"]),
    "Ice Rod Item" : ItemData(649, ItemClassification.useful, ["Fungible", "Item"]),
    "Thunder Rod Item" : ItemData(650, ItemClassification.useful, ["Fungible", "Item"]),
    "Venom Rod Item" : ItemData(651, ItemClassification.useful, ["Fungible", "Item"]),
    "Lillith Rod Item" : ItemData(652, ItemClassification.useful, ["Fungible", "Item"]),
    "Wizard Rod Item" : ItemData(653, ItemClassification.useful, ["Fungible", "Item"]),
    "Staff Item" : ItemData(654, ItemClassification.useful, ["Fungible", "Item"]),
    "Mythril Staff Item" : ItemData(655, ItemClassification.useful, ["Fungible", "Item"]),
    "Power Staff Item" : ItemData(656, ItemClassification.useful, ["Fungible", "Item"]),
    "Healing Staff Item" : ItemData(657, ItemClassification.useful, ["Fungible", "Item"]),
    "Staff of Light Item" : ItemData(658, ItemClassification.useful, ["Fungible", "Item"]),
    "Sage's Staff Item" : ItemData(659, ItemClassification.useful, ["Fungible", "Item"]),
    "Judgement Staff Item" : ItemData(660, ItemClassification.useful, ["Fungible", "Item"]),
    "Fire Bow Item" : ItemData(661, ItemClassification.useful, ["Fungible", "Item"]),
    "Ice Bow Item" : ItemData(662, ItemClassification.useful, ["Fungible", "Item"]),
    "Thunder Bow Item" : ItemData(663, ItemClassification.useful, ["Fungible", "Item"]),
    "Darkness Bow Item" : ItemData(664, ItemClassification.useful, ["Fungible", "Item"]),
    "Killer Bow Item" : ItemData(665, ItemClassification.useful, ["Fungible", "Item"]),
    "Elven Bow Item" : ItemData(666, ItemClassification.useful, ["Fungible", "Item"]),
    "Yoichi Bow Item" : ItemData(667, ItemClassification.useful, ["Fungible", "Item"]),
    "Artemis Bow Item" : ItemData(668, ItemClassification.useful, ["Fungible", "Item"]),
    "Silver Harp Item" : ItemData(669, ItemClassification.useful, ["Fungible", "Item"]),
    "Dream Harp Item" : ItemData(670, ItemClassification.useful, ["Fungible", "Item"]),
    "Lamia's Harp Item" : ItemData(671, ItemClassification.useful, ["Fungible", "Item"]),
    "Apollo's Harp Item" : ItemData(672, ItemClassification.useful, ["Fungible", "Item"]),
    "Whip Item" : ItemData(673, ItemClassification.useful, ["Fungible", "Item"]),
    "Chain Whip Item" : ItemData(674, ItemClassification.useful, ["Fungible", "Item"]),
    "Thunder Whip Item" : ItemData(675, ItemClassification.useful, ["Fungible", "Item"]),
    "Flame Whip Item" : ItemData(676, ItemClassification.useful, ["Fungible", "Item"]),
    "Dragon's Whisker Item" : ItemData(677, ItemClassification.useful, ["Fungible", "Item"]),
    "Giyaman Item" : ItemData(678, ItemClassification.useful, ["Fungible", "Item"]),
    "Earth Bell Item" : ItemData(679, ItemClassification.useful, ["Fungible", "Item"]),
    "Rune Chime Item" : ItemData(680, ItemClassification.useful, ["Fungible", "Item"]),
    "Tinkerbell Item" : ItemData(681, ItemClassification.useful, ["Fungible", "Item"]),
    "Drain Sword Item" : ItemData(682, ItemClassification.useful, ["Fungible", "Item"]),
    "RuneEdge Item" : ItemData(683, ItemClassification.useful, ["Fungible", "Item"]),
    "Flametongue Item" : ItemData(684, ItemClassification.useful, ["Fungible", "Item"]),
    "IceBrand Item" : ItemData(685, ItemClassification.useful, ["Fungible", "Item"]),
    "Full Moon Item" : ItemData(686, ItemClassification.useful, ["Fungible", "Item"]),
    "Shuriken Item" : ItemData(687, ItemClassification.useful, ["Fungible", "Item"]),
    "Pinwheel Item" : ItemData(688, ItemClassification.useful, ["Fungible", "Item"]),
    "Excailbur Item" : ItemData(689, ItemClassification.useful, ["Fungible", "Item"]),
    "BeastKiller Item" : ItemData(690, ItemClassification.useful, ["Fungible", "Item"]),
    "Flail Item" : ItemData(691, ItemClassification.useful, ["Fungible", "Item"]),
    "Morning Star Item" : ItemData(692, ItemClassification.useful, ["Fungible", "Item"]),
    "Wonder Wand Item" : ItemData(693, ItemClassification.useful, ["Fungible", "Item"]),
    "Brave Blade Item" : ItemData(694, ItemClassification.useful, ["Fungible", "Item"]),
    "Soot Item" : ItemData(695, ItemClassification.useful, ["Fungible", "Item"]),
    "Chicken Knife Item" : ItemData(696, ItemClassification.useful, ["Fungible", "Item"]),
    "RisingSun Item" : ItemData(697, ItemClassification.useful, ["Fungible", "Item"]),
    "Silver Bow Item" : ItemData(698, ItemClassification.useful, ["Fungible", "Item"]),
    "Gale Bow Item" : ItemData(699, ItemClassification.useful, ["Fungible", "Item"]),
    "AntiMagic Bow Item" : ItemData(700, ItemClassification.useful, ["Fungible", "Item"]),
    "Avis Killer Item" : ItemData(701, ItemClassification.useful, ["Fungible", "Item"]),
    "DoomCut Item" : ItemData(702, ItemClassification.useful, ["Fungible", "Item"]),
    "Giant's Axe Item" : ItemData(703, ItemClassification.useful, ["Fungible", "Item"]),
    "ManEater Item" : ItemData(704, ItemClassification.useful, ["Fungible", "Item"]),
    "Thief Knife Item" : ItemData(705, ItemClassification.useful, ["Fungible", "Item"]),
    "Dancing Dagger Item" : ItemData(706, ItemClassification.useful, ["Fungible", "Item"]),
    "Enhancer Item" : ItemData(707, ItemClassification.useful, ["Fungible", "Item"]),
    "Leather Shield Item" : ItemData(708, ItemClassification.useful, ["Fungible", "Item"]),
    "Bronze Shield Item" : ItemData(709, ItemClassification.useful, ["Fungible", "Item"]),
    "Iron Shield Item" : ItemData(710, ItemClassification.useful, ["Fungible", "Item"]),
    "Mythril Shield Item" : ItemData(711, ItemClassification.useful, ["Fungible", "Item"]),
    "Golden Shield Item" : ItemData(712, ItemClassification.useful, ["Fungible", "Item"]),
    "Aegis Shield Item" : ItemData(713, ItemClassification.useful, ["Fungible", "Item"]),
    "Diamond Shield Item" : ItemData(714, ItemClassification.useful, ["Fungible", "Item"]),
    "Crystal Shield Item" : ItemData(715, ItemClassification.useful, ["Fungible", "Item"]),
    "Leather Cap Item" : ItemData(716, ItemClassification.useful, ["Fungible", "Item"]),
    "Bronze Helm Item" : ItemData(717, ItemClassification.useful, ["Fungible", "Item"]),
    "Iron Helm Item" : ItemData(718, ItemClassification.useful, ["Fungible", "Item"]),
    "Mythril Helm Item" : ItemData(719, ItemClassification.useful, ["Fungible", "Item"]),
    "Golden Helm Item" : ItemData(720, ItemClassification.useful, ["Fungible", "Item"]),
    "Diamond Helm Item" : ItemData(721, ItemClassification.useful, ["Fungible", "Item"]),
    "Crystal Helm Item" : ItemData(722, ItemClassification.useful, ["Fungible", "Item"]),
    "Plumed Hat Item" : ItemData(723, ItemClassification.useful, ["Fungible", "Item"]),
    "Tricorn Hat Item" : ItemData(724, ItemClassification.useful, ["Fungible", "Item"]),
    "Magus Item" : ItemData(725, ItemClassification.useful, ["Fungible", "Item"]),
    "Circlet Item" : ItemData(726, ItemClassification.useful, ["Fungible", "Item"]),
    "Gold Hairpin Item" : ItemData(727, ItemClassification.useful, ["Fungible", "Item"]),
    "Ribbon Item" : ItemData(728, ItemClassification.useful, ["Fungible", "Item"]),
    "Bandana Item" : ItemData(729, ItemClassification.useful, ["Fungible", "Item"]),
    "GrnBeret Item" : ItemData(730, ItemClassification.useful, ["Fungible", "Item"]),
    "DarkHood Item" : ItemData(731, ItemClassification.useful, ["Fungible", "Item"]),
    "Lamia's Tiara Item" : ItemData(732, ItemClassification.useful, ["Fungible", "Item"]),
    "Leather Armor Item" : ItemData(733, ItemClassification.useful, ["Fungible", "Item"]),
    "Bronze Armor Item" : ItemData(734, ItemClassification.useful, ["Fungible", "Item"]),
    "Iron Armor Item" : ItemData(735, ItemClassification.useful, ["Fungible", "Item"]),
    "Mythril Armor Item" : ItemData(736, ItemClassification.useful, ["Fungible", "Item"]),
    "Golden Armor Item" : ItemData(737, ItemClassification.useful, ["Fungible", "Item"]),
    "Diamond Armor Item" : ItemData(738, ItemClassification.useful, ["Fungible", "Item"]),
    "Crystal Armor Item" : ItemData(739, ItemClassification.useful, ["Fungible", "Item"]),
    "CopperPlt Item" : ItemData(740, ItemClassification.useful, ["Fungible", "Item"]),
    "Training Suit Item" : ItemData(741, ItemClassification.useful, ["Fungible", "Item"]),
    "Silver Plate Item" : ItemData(742, ItemClassification.useful, ["Fungible", "Item"]),
    "Stealth Suit Item" : ItemData(743, ItemClassification.useful, ["Fungible", "Item"]),
    "DiamndPlt Item" : ItemData(744, ItemClassification.useful, ["Fungible", "Item"]),
    "DarkSuit Item" : ItemData(745, ItemClassification.useful, ["Fungible", "Item"]),
    "Cotton Robe Item" : ItemData(746, ItemClassification.useful, ["Fungible", "Item"]),
    "Silk robe Item" : ItemData(747, ItemClassification.useful, ["Fungible", "Item"]),
    "Gaia Gear Item" : ItemData(748, ItemClassification.useful, ["Fungible", "Item"]),
    "Bard's Surplice Item" : ItemData(749, ItemClassification.useful, ["Fungible", "Item"]),
    "Lumina Robe Item" : ItemData(750, ItemClassification.useful, ["Fungible", "Item"]),
    "Black Robe Item" : ItemData(751, ItemClassification.useful, ["Fungible", "Item"]),
    "White Robe Item" : ItemData(752, ItemClassification.useful, ["Fungible", "Item"]),
    "Mirage Vest Item" : ItemData(753, ItemClassification.useful, ["Fungible", "Item"]),
    "Guard Ring Item" : ItemData(754, ItemClassification.useful, ["Fungible", "Item"]),
    "Thief's Glove Item" : ItemData(755, ItemClassification.useful, ["Fungible", "Item"]),
    "Giant's Gloves Item" : ItemData(756, ItemClassification.useful, ["Fungible", "Item"]),
    "Elf Cape Item" : ItemData(757, ItemClassification.useful, ["Fungible", "Item"]),
    "Cursed Ring Item" : ItemData(758, ItemClassification.useful, ["Fungible", "Item"]),
    "Glasses Item" : ItemData(759, ItemClassification.useful, ["Fungible", "Item"]),
    "Running Shoes Item" : ItemData(760, ItemClassification.useful, ["Fungible", "Item"]),
    "Mythril Glove Item" : ItemData(761, ItemClassification.useful, ["Fungible", "Item"]),
    "Silver Armlet Item" : ItemData(762, ItemClassification.useful, ["Fungible", "Item"]),
    "Diamond Armlet Item" : ItemData(763, ItemClassification.useful, ["Fungible", "Item"]),
    "Strength Item" : ItemData(764, ItemClassification.useful, ["Fungible", "Item"]),
    "Power Wrist Item" : ItemData(765, ItemClassification.useful, ["Fungible", "Item"]),
    "Angel Gwn Item" : ItemData(766, ItemClassification.useful, ["Fungible", "Item"]),
    "Angel Ring Item" : ItemData(767, ItemClassification.useful, ["Fungible", "Item"]),
    "Flame Ring Item" : ItemData(768, ItemClassification.useful, ["Fungible", "Item"]),
    "Coral Ring Item" : ItemData(769, ItemClassification.useful, ["Fungible", "Item"]),
    "Bone Mail Item" : ItemData(770, ItemClassification.useful, ["Fungible", "Item"]),
    "Leather Shoes Item" : ItemData(771, ItemClassification.useful, ["Fungible", "Item"]),
    "Kaiser Knuckles Item" : ItemData(772, ItemClassification.useful, ["Fungible", "Item"]),
    "Gauntlets Item" : ItemData(773, ItemClassification.useful, ["Fungible", "Item"]),
    "Tiger Mask Item" : ItemData(774, ItemClassification.useful, ["Fungible", "Item"]),
    "Flame Shield Item" : ItemData(775, ItemClassification.useful, ["Fungible", "Item"]),
    "CornaJar Item" : ItemData(776, ItemClassification.useful, ["Fungible", "Item"]),
    "Genji Shield Item" : ItemData(777, ItemClassification.useful, ["Fungible", "Item"]),
    "Genji Helm Item" : ItemData(778, ItemClassification.useful, ["Fungible", "Item"]),
    "Genji Armor Item" : ItemData(779, ItemClassification.useful, ["Fungible", "Item"]),
    "Genji Gloves Item" : ItemData(780, ItemClassification.useful, ["Fungible", "Item"]),
    "Wall Ring Item" : ItemData(781, ItemClassification.useful, ["Fungible", "Item"]),
    "Hypno Helm Item" : ItemData(782, ItemClassification.useful, ["Fungible", "Item"]),
    "Thornlet Item" : ItemData(783, ItemClassification.useful, ["Fungible", "Item"]),
    "Ice Shield Item" : ItemData(784, ItemClassification.useful, ["Fungible", "Item"]),
    "Cursed Shield Item" : ItemData(785, ItemClassification.useful, ["Fungible", "Item"]),
    "Rainbow Dress Item" : ItemData(786, ItemClassification.useful, ["Fungible", "Item"]),
    "Red Shoes Item" : ItemData(787, ItemClassification.useful, ["Fungible", "Item"]),
    "Potion Item" : ItemData(788, ItemClassification.useful, ["Fungible", "Item"]),
    "HiPotion Item" : ItemData(789, ItemClassification.useful, ["Fungible", "Item"]),
    "Ether Item" : ItemData(790, ItemClassification.useful, ["Fungible", "Item"]),
    "Elixir Item" : ItemData(791, ItemClassification.useful, ["Fungible", "Item"]),
    "Phoenix Down Item" : ItemData(792, ItemClassification.useful, ["Fungible", "Item"]),
    "Maiden's Kiss Item" : ItemData(793, ItemClassification.useful, ["Fungible", "Item"]),
    "Revivify Item" : ItemData(794, ItemClassification.useful, ["Fungible", "Item"]),
    "TurtleShell Item" : ItemData(795, ItemClassification.useful, ["Fungible", "Item"]),
    "Antidote Item" : ItemData(796, ItemClassification.useful, ["Fungible", "Item"]),
    "Eyedrop Item" : ItemData(797, ItemClassification.useful, ["Fungible", "Item"]),
    "DragonFang Item" : ItemData(798, ItemClassification.useful, ["Fungible", "Item"]),
    "DarkMatter Item" : ItemData(799, ItemClassification.useful, ["Fungible", "Item"]),
    "Soft Item" : ItemData(800, ItemClassification.useful, ["Fungible", "Item"]),
    "LuckMallet Item" : ItemData(801, ItemClassification.useful, ["Fungible", "Item"]),
    "Magic Lamp Item" : ItemData(802, ItemClassification.useful, ["Fungible", "Item"]),
    "Tent Item" : ItemData(803, ItemClassification.useful, ["Fungible", "Item"]),
    "Cabin Item" : ItemData(804, ItemClassification.useful, ["Fungible", "Item"]),
    "Giant Drink Item" : ItemData(805, ItemClassification.useful, ["Fungible", "Item"]),
    "Power Drink Item" : ItemData(806, ItemClassification.useful, ["Fungible", "Item"]),
    "Speed Drink Item" : ItemData(807, ItemClassification.useful, ["Fungible", "Item"]),
    "Protect Drink Item" : ItemData(808, ItemClassification.useful, ["Fungible", "Item"]),
    "Hero Drink Item" : ItemData(809, ItemClassification.useful, ["Fungible", "Item"]),
    "Ramuh Item" : ItemData(810, ItemClassification.useful, ["Fungible", "Item"]),
    "Shoat Item" : ItemData(811, ItemClassification.useful, ["Fungible", "Item"]),
    "Golem Item" : ItemData(812, ItemClassification.useful, ["Fungible", "Item"]),
    "Flame Scroll Item" : ItemData(813, ItemClassification.useful, ["Fungible", "Item"]),
    "Water Scroll Item" : ItemData(814, ItemClassification.useful, ["Fungible", "Item"]),
    "Thunder Scroll Item" : ItemData(815, ItemClassification.useful, ["Fungible", "Item"]),
    
    "100 Gil" : ItemData(900, ItemClassification.useful, ["Gil", "Item"]),
    "300 Gil" : ItemData(901, ItemClassification.useful, ["Gil", "Item"]),
    "1000 Gil" : ItemData(902, ItemClassification.useful, ["Gil", "Item"]),
    "5000 Gil (#1)" : ItemData(903, ItemClassification.useful, ["Gil", "Item"]),
    "9900 Gil" : ItemData(904, ItemClassification.useful, ["Gil", "Item"]),
    "8000 Gil (#1)" : ItemData(905, ItemClassification.useful, ["Gil", "Item"]),
    "4400 Gil" : ItemData(906, ItemClassification.useful, ["Gil", "Item"]),
    "10000 Gil (#1)" : ItemData(907, ItemClassification.useful, ["Gil", "Item"]),
    "5000 Gil (#2)" : ItemData(908, ItemClassification.useful, ["Gil", "Item"]),
    "8000 Gil (#2)" : ItemData(909, ItemClassification.useful, ["Gil", "Item"]),
    "5000 Gil (#3)" : ItemData(910, ItemClassification.useful, ["Gil", "Item"]),
    "9000 Gil (#1)" : ItemData(911, ItemClassification.useful, ["Gil", "Item"]),
    "18000 Gil" : ItemData(912, ItemClassification.useful, ["Gil", "Item"]),
    "2500 Gil" : ItemData(913, ItemClassification.useful, ["Gil", "Item"]),
    "4900 Gil" : ItemData(914, ItemClassification.useful, ["Gil", "Item"]),
    "9500 Gil" : ItemData(915, ItemClassification.useful, ["Gil", "Item"]),
    "9000 Gil (#2)" : ItemData(916, ItemClassification.useful, ["Gil", "Item"]),
    "8000 Gil (#3)" : ItemData(917, ItemClassification.useful, ["Gil", "Item"]),
    "10000 Gil (#2)" : ItemData(918, ItemClassification.useful, ["Gil", "Item"]),
    "12000 Gil (#1)" : ItemData(919, ItemClassification.useful, ["Gil", "Item"]),
    "12000 Gil (#2)" : ItemData(920, ItemClassification.useful, ["Gil", "Item"]),
    "9000 Gil (#3)" : ItemData(921, ItemClassification.useful, ["Gil", "Item"]),
    "12000 Gil (#3)" : ItemData(922, ItemClassification.useful, ["Gil", "Item"]),
    "5000 Gil (#4)" : ItemData(923, ItemClassification.useful, ["Gil", "Item"]),
    "15000 Gil" : ItemData(924, ItemClassification.useful, ["Gil", "Item"]),
    "20000 Gil" : ItemData(925, ItemClassification.useful, ["Gil", "Item"]),
    "25000 Gil" : ItemData(926, ItemClassification.useful, ["Gil", "Item"]),


    "Walse Tower Key" : ItemData(1000, ItemClassification.progression, ["Unique", "Key Items"]),
    "Steamship Key" : ItemData(1001, ItemClassification.progression, ["Unique", "Key Items"]),
    "Ifrit's Fire" : ItemData(1002, ItemClassification.progression, ["Unique", "Key Items"]),
    "SandwormBait" : ItemData(1003, ItemClassification.progression, ["Unique", "Key Items"]),
    "Big Bridge Key" : ItemData(1004, ItemClassification.progression, ["Unique", "Key Items"]),
    "Hiryuu Call" : ItemData(1005, ItemClassification.progression, ["Unique", "Key Items"]),
    "Submarine Key" : ItemData(1006, ItemClassification.progression, ["Unique", "Key Items"]),
    "Anti Barrier" : ItemData(1007, ItemClassification.progression, ["Unique", "Key Items"]),
    "Bracelet" : ItemData(1008, ItemClassification.progression, ["Unique", "Key Items"]),
    "Pyramid Page" : ItemData(1009, ItemClassification.progression, ["Unique", "Key Items"]),
    "Shrine Page" : ItemData(1010, ItemClassification.progression, ["Unique", "Key Items"]),
    "Trench Page" : ItemData(1011, ItemClassification.progression, ["Unique", "Key Items"]),
    "Falls Page" : ItemData(1012, ItemClassification.progression, ["Unique", "Key Items"]),
    "Mirage Radar" : ItemData(1013, ItemClassification.progression, ["Unique", "Key Items"]),
    "Adamantite" : ItemData(1014, ItemClassification.progression, ["Unique", "Key Items"]),
    "Moogle Suit" : ItemData(1015, ItemClassification.progression, ["Unique", "Key Items"]),
    "Elder Branch" : ItemData(1016, ItemClassification.progression, ["Unique", "Key Items"]),
    "1st Tablet" : ItemData(1017, ItemClassification.progression, ["Unique", "Key Items"]),
    "2nd Tablet" : ItemData(1018, ItemClassification.progression, ["Unique", "Key Items"]),
    "3rd Tablet" : ItemData(1019, ItemClassification.progression, ["Unique", "Key Items"]),
    "4th Tablet" : ItemData(1020, ItemClassification.progression, ["Unique", "Key Items"]),

    "Victory" : ItemData(1200, ItemClassification.progression, ["Victory"]),

}

item_groups = {}
for item, data in item_table.items():
    for group in data.groups:
        item_groups[group] = item_groups.get(group, []) + [item]


class FFVCDItem(Item):
    game = "ffvcd"
    def __init__(self, name, classification, item_data_id, player, groups):
        super().__init__(name, classification, item_data_id, player)
        self.groups = groups

