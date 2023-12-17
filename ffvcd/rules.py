from typing import TYPE_CHECKING

from worlds.generic.Rules import add_rule


def set_rules(ffvcdworld):
    world = ffvcdworld.multiworld
    player = ffvcdworld.player

    # bal_locations = [i for i in world.get_locations() if "Bal" in i.name]
    # for loc1 in bal_locations:
    #     add_rule(loc1, lambda state: state.has("Adamantite", player))

    # moogle_locations = [i for i in world.get_locations() if "Moogle" in i.name]
    # for loc1 in moogle_locations:
    #     add_rule(loc1, lambda state: state.has("SandwormBait", player))

    # locations = [i for i in world.get_locations() if "North Mountain" in i.name]
    # for loc1 in locations:
    #     add_rule(loc1, lambda state: state.has("Falls Page", player))

    # locations = [i for i in world.get_locations() if "Istory Falls" in i.name]
    # for loc1 in locations:
    #     add_rule(loc1, lambda state: state.has("Pyramid Page", player))

    # locations = [i for i in world.get_locations() if "Wind Shrine" in i.name]
    # for loc1 in locations:
    #     add_rule(loc1, lambda state: state.has("Shrine Page", player))


    # locations = [i for i in world.get_locations() if "Mua" in i.name]
    # for loc1 in locations:
    #     add_rule(loc1, lambda state: state.has("Bracelet", player))



    exdeath = world.get_location("ExDeath", player)
    exdeath.place_locked_item(world.worlds[player].create_event("Victory"))
    add_rule(exdeath, lambda state: state.has("1st Tablet", player) and state.has("2nd Tablet", player) \
             and state.has("3rd Tablet", player) and state.has("4th Tablet", player))
    world.completion_condition[player] = lambda state: state.has("Victory", player)