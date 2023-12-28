from Options import Toggle, DefaultOnToggle, OptionSet


class JobPalettes(Toggle):
    """
    When enabled, randomizes palettes for each characters' jobs
    """
    display_name = "Randomize Job Palettes"
class FourJob(Toggle):
    """
    When enabled, enables four job mode. No crystals are placed in the world, and the player starts with 4 crystals
    """
    display_name = "Enable Four Job Mode"

class ExtraPatches(DefaultOnToggle):
    """
    When enabled, optional patches for L/R functionality in menus and enhanced optimize are applied
    """
    display_name = "Apply optional patches"

class RemoveFlashes(DefaultOnToggle):
    """
    When enabled, optional patches for removing flashes (notably Neo ExDeath) are applied
    """
    display_name = "Apply flash removal"

class WorldLock(OptionSet):
    """Determines how many worlds are available from the start.
    1: The first world is available. Adamantite unlocks World 2. Defeating Exdeath in World 2 unlocks World 3 via Anti Barrier and Bracelet.
    2: Worlds 1 and 2 are available. Defeating Exdeath in World 2 unlocks World 3 via Anti Barrier and Bracelet.
    3: All worlds are available immediately.    
    """
    display_name = "World Lock"
    valid_keys = {
        "1",
        "2",
        "3",
    }


ffvcd_options = {
    "job_palettes": JobPalettes,
    "four_job": FourJob,
    "extra_patches" : ExtraPatches,
    "remove_flashes" : RemoveFlashes,
    "world_lock" : WorldLock
    }