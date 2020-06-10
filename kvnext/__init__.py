
import renpy
import renpy.sl2.slast as slast
import renpy.parser as parser
import renpy.ast as ast
import sys

from modloader import modinfo, modast
from modloader.modgame import sprnt
from modloader.modgame import base as ml
from modloader.modclass import Mod, loadable_mod

@loadable_mod
class AWSWMod(Mod):
    """Adds a follow-up encounter with Kevin"""
    def mod_info(self):
        return ("KevinExtended", "v0.1", "SparkzTehDragon")

    def mod_load(self):
        
        label2 = modast.find_label("chapter1chars")
        menu2 = modast.find_menu("Meet with Sebastian.")[0]

        print label2
        print menu2


        modast.add_menu_option(menu2, "Take a walk.", label2)

        menu = modast.get_slscreen("main_menu")
        addition = modast.get_slscreen("KevinExtended_main_menu")


        
        menu.children.append(addition.children[0])

    def mod_complete(self):
        pass
