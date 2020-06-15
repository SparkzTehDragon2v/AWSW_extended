
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

# note: 
#   label chapter2chars | a jumping point to the label and then the menu names which those menu Starts and Labels are
# label chap2altmenua1
# label of chapter2chars



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
        # KvScene2 = modast.find_label("chapter2charsmodded")
        # Kv_c2 = modast.find_label("k2chap2")
        # Sb_initialize = modast.find_label("")
        # Sb_date = modast.find_label("sebastian2")
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


# Possible Jumping Points through labels
# label chapter1chars, (with menu search "Meet with the store clerk.", "Meet with Zhong.", "Meet with Emera.", "" | Locals "chapter2csplayed" & "chapter2scplayed" but == 1 not 0. ) chap2altmanua1 ("Meet with Bryce"), chap2altmenua2 ("Meet with Emera"), chap2altmenub1 ("[[Show more options.]"), chap2altmenub2 ("Meet with the store clerk."). 