# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
#


# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *

import bmesh
from mathutils import Vector   
  
 
class VIEWD_TP_Selected_to_Selection(bpy.types.Operator):
    bl_idname = "object.to_selection"
    bl_label = "To selection"
 
    def execute(self, context):
        
        obj_list = []
        bpy.ops.object.mode_set(mode='OBJECT')
        ref_obj = bpy.context.active_object

        obj1, obj2 = context.selected_objects
        second_obj = obj1 if obj2 == ref_obj else obj2                                 
        
        obj_list.append(second_obj.name)
        bpy.data.objects[second_obj.name].select = False 
        bpy.ops.object.duplicate_move()
        bpy.context.active_object.name = "Dummy"
        obj = context.active_object
        bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')    
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
        
        
        copy_cursor = bpy.context.scene.cursor_location.copy()     
 
        bm = bmesh.new()
        bm.from_mesh(obj.data)
 
 
        selected_faces = [f for f in bm.faces if f.select]
 
        for face in selected_faces:
 
            face_location = face.calc_center_median()
 
            loc_world_space = obj.matrix_world * Vector(face_location)
 
            z = Vector((0,0,1))
 
            angle = face.normal.angle(z)
 
            axis = z.cross(face.normal)
            bpy.ops.object.select_all(action='DESELECT')
            bpy.context.scene.objects.active = bpy.data.objects[second_obj.name]
            bpy.data.objects[second_obj.name].select=True
            bpy.ops.object.duplicate()
            bpy.context.scene.cursor_location = loc_world_space
            bpy.ops.view3d.snap_selected_to_cursor()
 
            bpy.ops.transform.rotate(value=angle, axis=axis)
            obj_list.append(context.object.name)
 
        bm.to_mesh(obj.data)
 
        bm.free()
 
        bpy.context.scene.cursor_location = copy_cursor
        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.scene.objects.active = bpy.data.objects["Dummy"]         
        bpy.data.objects["Dummy"].select = True
        bpy.ops.object.delete(use_global=False)
        
        bpy.context.scene.objects.active = bpy.data.objects[obj_list[0]]
         
        for obj in obj_list:
            bpy.data.objects[obj].select=True
            bpy.ops.make.link()  # custom link called from operators module
         
        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.scene.objects.active = bpy.data.objects[ref_obj.name]
        bpy.data.objects[second_obj.name].select=True
        bpy.data.objects[ref_obj.name].select=True
         
        bpy.ops.object.mode_set(mode='EDIT')        
        del(obj_list[:])
        
 
        return {'FINISHED'}


