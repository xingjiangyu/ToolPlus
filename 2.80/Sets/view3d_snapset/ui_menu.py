# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *
from . icons.icons import load_icons  



def draw_snapset_menu_ui(self, context, layout):

    icons = load_icons()   

    layout.operator_context = 'INVOKE_REGION_WIN' 

    addon_prefs = context.preferences.addons[__package__].preferences

    layout.scale_y = addon_prefs.ui_scale_y

    if addon_prefs.tpc_use_grid == True:
        if addon_prefs.use_internal_icon_bta == True:  
            layout.operator("tpc_ot.snapset_button_a", text=addon_prefs.name_bta, icon=addon_prefs.icon_bta)
        else:
            button_snap_grid = icons.get("icon_snap_grid")
            layout.operator("tpc_ot.snapset_button_a", text=addon_prefs.name_bta, icon_value=button_snap_grid.icon_id)
 
    if addon_prefs.tpc_use_grid_modal == True:
        button_snap_grid = icons.get("icon_snap_grid")
        layout.operator("tpc_ot.snapset_modal", text="GridM", icon_value=button_snap_grid.icon_id).mode = "GRID"
                
    if context.mode == 'OBJECT':

        if addon_prefs.tpc_use_place == True:
            if addon_prefs.use_internal_icon_btb == True:   
                layout.operator("tpc_ot.snapset_button_b", text=addon_prefs.name_btb, icon=addon_prefs.icon_btb)
            else:
                button_snap_place = icons.get("icon_snap_place")
                layout.operator("tpc_ot.snapset_button_b", text=addon_prefs.name_btb, icon_value=button_snap_place.icon_id)
        
        if addon_prefs.tpc_use_place_modal == True:
            button_snap_place = icons.get("icon_snap_place")
            layout.operator("tpc_ot.snapset_modal", text="PlaceM", icon_value=button_snap_place.icon_id).mode = "PLACE"

    else:
        if addon_prefs.tpc_use_retopo == True:
            if addon_prefs.use_internal_icon_btf == True:   
                layout.operator("tpc_ot.snapset_button_f", text=addon_prefs.name_btf, icon=addon_prefs.icon_btf)    
            else:
                button_snap_retopo = icons.get("icon_snap_retopo")
                layout.operator("tpc_ot.snapset_button_f", text=addon_prefs.name_btf, icon_value=button_snap_retopo.icon_id)    
       
        if addon_prefs.tpc_use_retopo_modal == True:              
            button_snap_retopo = icons.get("icon_snap_retopo")
            layout.operator("tpc_ot.snapset_modal", text="RetopoM", icon_value=button_snap_retopo.icon_id).mode = "RETOPO"   
      
    if addon_prefs.tpc_use_cursor == True:
        if addon_prefs.use_internal_icon_btc == True:     
            layout.operator("tpc_ot.snapset_button_c", text=addon_prefs.name_btc, icon=addon_prefs.icon_btc) 
        else:       
            button_snap_cursor = icons.get("icon_snap_cursor")           
            layout.operator("tpc_ot.snapset_button_c", text=addon_prefs.name_btc, icon_value=button_snap_cursor.icon_id) 

    if addon_prefs.tpc_use_closest == True:
        if addon_prefs.use_internal_icon_bte == True:
            layout.operator("tpc_ot.snapset_button_e", text=addon_prefs.name_bte, icon=addon_prefs.icon_bte)
        else:           
            button_snap_closest = icons.get("icon_snap_closest")
            layout.operator("tpc_ot.snapset_button_e", text=addon_prefs.name_bte, icon_value=button_snap_closest.icon_id)
            

    if addon_prefs.tpc_use_active == True: 
        if addon_prefs.use_internal_icon_btd == True:
            layout.operator("tpc_ot.snapset_button_d", text=addon_prefs.name_btd, icon=addon_prefs.icon_btd) 
        else:
            button_snap_active = icons.get("icon_snap_active")            
            layout.operator("tpc_ot.snapset_button_d", text=addon_prefs.name_btd, icon_value=button_snap_active.icon_id) 

    #layout.popover(panel="VIEW3D_PT_SnapSet_Header_Panel", text=" SnapSet")            




# UI: HOTKEY MENU # 
class VIEW3D_MT_SnapSet_Menu(bpy.types.Menu):
    bl_label = "SnapSet"
    bl_idname = "VIEW3D_MT_SnapSet_Menu"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN' 
        
        draw_snapset_menu_ui(self, context, layout)



# UI: HOTKEY MENU # 
class VIEW3D_MT_SnapSet_Menu_Special(bpy.types.Menu):
    bl_label = "SnapSet"
    bl_idname = "VIEW3D_MT_SnapSet_Menu_Special"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN' 
        
        draw_snapset_menu_ui(self, context, layout)

