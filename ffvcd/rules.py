from worlds.generic.Rules import add_rule, set_rule, forbid_item

def set_rules(ffvcdworld):
    multiworld = ffvcdworld.multiworld
    player = ffvcdworld.player
    
    if ffvcdworld.options.goal.value == 1:
        multiworld.completion_condition[player] = \
            lambda state: state.has("ExDeath World 2", player)
			
    elif ffvcdworld.options.goal.value == 2:
        piano_events = (
            "Piano (Tule)",
            "Piano (Carwen)",
            "Piano (Karnak)",
            "Piano (Jacole)",
            "Piano (Crescent)",
            "Piano (Mua)",
            "Piano (Rugor)",
            "Piano (Mirage)",
        )
        multiworld.completion_condition[player] = \
            lambda state: all(state.has(piano, player) for piano in piano_events)
			
    else:
        multiworld.completion_condition[player] = lambda state: state.has("Victory", player)
    
    # set_rule(multiworld.get_location("Kelb - CornaJar at Kelb (CornaJar)", ffvcdworld.player),
    #       lambda state: state.has("Catch Ability", ffvcdworld.player) or
    #                     state.has("Trainer Crystal", ffvcdworld.player))
    
