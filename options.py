from Options import Toggle, Choice, Range, NamedRange, TextChoice, DeathLink

class WorldLock(Choice):
    """
    Which world lock to use
    1: Access locked to world 1 to start
    2: Access locked to worlds 1 & 2 to start
    3: All worlds accessible from start
    """
    display_name = "World Lock"
    option_world_1 = 0
    option_world_2 = 1
    option_world_3 = 2
    default = 0


ffvcd_options = {
    "world_lock": WorldLock,
    }