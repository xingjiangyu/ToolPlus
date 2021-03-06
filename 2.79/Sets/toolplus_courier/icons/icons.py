import os
import bpy
import bpy.utils.previews

toolplus_icon_collections = {}
toolplus_icons_loaded = False

def load_icons():
    global toolplus_icon_collections
    global toolplus_icons_loaded

    if toolplus_icons_loaded: return toolplus_icon_collections["main"]

    mkb_icons = bpy.utils.previews.new()

    icons_dir = os.path.join(os.path.dirname(__file__))

    #--------------------------------------------

    mkb_icons.load("icon_fun", os.path.join(icons_dir, "fun.png"), 'IMAGE')
    mkb_icons.load("icon_run", os.path.join(icons_dir, "run.png"), 'IMAGE')
    mkb_icons.load("icon_options", os.path.join(icons_dir, "options.png"), 'IMAGE')
    mkb_icons.load("icon_shadow", os.path.join(icons_dir, "shadow.png"), 'IMAGE')
    mkb_icons.load("icon_restart", os.path.join(icons_dir, "restart.png"), 'IMAGE')

    #--------------------------------------------

    toolplus_icon_collections["main"] = mkb_icons
    toolplus_icons_loaded = True

    return toolplus_icon_collections["main"]

def clear_icons():
    global toolplus_icons_loaded
    for icon in toolplus_icon_collections.values():
        bpy.utils.previews.remove(icon)
    toolplus_icon_collections.clear()
    toolplus_icons_loaded = False