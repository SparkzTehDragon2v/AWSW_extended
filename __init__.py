
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
        from modloader.modgame import base, AWSWHomeHook

        home_hook = AWSWHomeHook(base)        
        home_hook1 = ml.get_home_hook()

        KvScene = modast.find_label("chapter1charsmodded")
        KvScene_initialize = modast.find_label("KevinExtended")
##        hook = modast.find_menu("Meet with Sebastian.")
        home_hook.hook_chapter_1(KvScene_initialize)
##        home_hook.add_route("Meet with Kevin", KvScene, "MeetKevin == 1 and kvextpoints < 3") ## "(not sebastianunplayed) and kevin1ext is None"
##        print KvScene
##        print hook        
##        modast.add_menu_option(hook, "Take a walk.", KvScene)
##        home_hook.add_route("Take a walk.", modast.find_label("chapter1charsmodded"), "MeetKevin == 0 and kvextpoints == 0")
        menu = modast.get_slscreen("main_menu")
        addition = modast.get_slscreen("KevinExtended_main_menu")
##        menu.children.append(addition.children[0])

    def mod_complete(self):
        pass
