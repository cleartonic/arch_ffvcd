from Options import Toggle, DefaultOnToggle, Range


class JobPalettes(Toggle):
    """
    When enabled, randomizes palettes for each characters' jobs
    """
    display_name = "Randomize Job Palettes"
class FourJob(Toggle):
    """
    When enabled, enables four job mode. No crystals are placed in the world, and the player starts with 4 crystals.
    Players are disallowed from leaving the menu if every character doesnt have a unique job
    """
    display_name = "Enable Four Job Mode"

class RemoveFlashes(DefaultOnToggle):
    """
    When enabled, optional patches for removing flashes (notably Neo ExDeath) are applied
    """
    display_name = "Apply flash removal"

class WorldLock(Range):
    """Determines how many worlds are available from the start.
    1: The first world is available. Adamantite unlocks World 2. Defeating Exdeath in World 2 unlocks World 3 via Anti Barrier and Bracelet.
    2: Worlds 1 and 2 are available. Defeating Exdeath in World 2 unlocks World 3 via Anti Barrier and Bracelet.
    3: All worlds are available immediately.    
    """
    display_name = "World Lock"
    range_start = 1
    range_end = 3
    default = 3


ffvcd_options = {
    "job_palettes": JobPalettes,
    "four_job": FourJob,
    "remove_flashes" : RemoveFlashes,
    "world_lock" : WorldLock
    }
