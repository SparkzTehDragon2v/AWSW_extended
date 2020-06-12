
import renpy
import renpy.ast as ast
import renpy.parser as parser
import renpy.sl2.slast as slast
import sys
from modloader import modinfo, modast
from modloader.modgame import sprnt
from modloader.modgame import base as ml
from modloader.modclass import Mod, loadable_mod
##from modloader.modinfo import get_mods

@loadable_mod
class AWSWMod(Mod):
    """Adds a follow-up encounter with Kevin"""
    def mod_info(self):
        return ("KevinExtended", "v0.1", "SparkzTehDragon")

    def mod_load(self):
#        ml.search_peak_if(modast.find_say("Hello there!", ast.Scene, 0)
        KvSource = modast.find_label("chapter1charsmodded")
        hook = modast.find_menu("Meet with Sebastian.")[0]
        print KvSource
        print hook


        modast.add_menu_option(hook, "Take a walk.", KvSource)

        menu = modast.get_slscreen("main_menu")
        addition = modast.get_slscreen("KevinExtended_main_menu")



        menu.children.append(addition.children[0])

    def mod_complete(self):
        pass
