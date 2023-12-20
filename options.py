from Options import Toggle, DefaultOnToggle


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

# class LennaName(FreeText):
#     """
#     Set Lenna's name
#     """
#     display_name = "Lenna's name"
#     default = "Lenna"
# class GalufName(FreeText):
#     """
#     Set Galuf's name
#     """
#     display_name = "Galuf's name"
#     default = "Galuf"
# class FarisName(FreeText):
#     """
#     Set Faris' name
#     """
#     display_name = "Faris' name"
#     default = "Faris"
# class KrileName(FreeText):
#     """
#     Set Krile's name
#     """
#     display_name = "Krile's name"
#     default = "Krile"


ffvcd_options = {
    "job_palettes": JobPalettes,
    "four_job": FourJob,
    "extra_patches" : ExtraPatches,
    "remove_flashes" : RemoveFlashes
    }