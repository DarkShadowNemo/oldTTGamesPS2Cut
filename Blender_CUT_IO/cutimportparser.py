from struct import unpack, pack, error
import bpy
import os
import mathutils
import math

def cut_importV2_parser(f):
    global Version
    global EntrySize1
    global id1
    global FloatCount

    ob = bpy.context.object

    idx=0
    Version = unpack("<I", f.read(4))[0]
    if Version == 1:
        EntrySize1 = unpack("<H", f.read(2))[0]
        id1 = unpack("<H", f.read(2))[0]
        FloatCount = unpack("<f", f.read(4))[0]
        
        bpy.context.scene.render.fps = 30
        bpy.context.scene.render.fps_base = 1
        bpy.context.scene.unit_settings.system_rotation = "RADIANS"

        for pbone in ob.pose.bones:
            pbone.rotation_mode = "XYZ"

        bpy.context.scene.frame_end = int(FloatCount)
        bpy.context.scene.frame_current = 1
        bpy.context.scene.frame_start = 1
        
    elif Version == 2:
        EntrySize1 = unpack("<H", f.read(2))[0]
        id1 = unpack("<H", f.read(2))[0]
        FloatCount = unpack("<f", f.read(4))[0]

        bpy.context.scene.render.fps = 30
        bpy.context.scene.render.fps_base = 1
        bpy.context.scene.unit_settings.system_rotation = "RADIANS"

        for pbone in ob.pose.bones:
            pbone.rotation_mode = "XYZ"

        bpy.context.scene.frame_end = int(FloatCount)
        bpy.context.scene.frame_current = 1
        bpy.context.scene.frame_start = 1

def cut_exportV2_parser(f):
    
    ob = bpy.context.object

    idx=0
    if Version == 1:
        f.write(pack("<I", Version-Version+1))
        f.write(pack("<H", EntrySize1-EntrySize1+32))
        f.write(pack("<H", id1-id1))
        f.write(pack("<f", FloatCount-FloatCount+bpy.context.scene.frame_end))
        
    elif Version == 2:
        f.write(pack("<I", Version-Version+2))
        f.write(pack("<H", EntrySize1-EntrySize1+32))
        f.write(pack("<H", id1-id1))
        f.write(pack("<f", FloatCount-FloatCount+bpy.context.scene.frame_end))
        
