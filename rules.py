from typing import TYPE_CHECKING

from worlds.generic.Rules import add_rule



def set_rules(ffvcdworld):
    world = ffvcdworld.multiworld
    player = ffvcdworld.player

        
    world.completion_condition[player] = lambda state: state.has("Victory", player)
    
    