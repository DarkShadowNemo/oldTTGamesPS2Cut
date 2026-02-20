from struct import unpack, pack, error
import bpy
import os
import mathutils
import math

def cut_importV2_parser(f):
    global Version
    global EntrySize1
    global id1
    global EntrySize2
    global id2
    global FloatCount
    global unk01
    global EntrySize3
    global id3
    global EntrySize4
    global id4
    global EntrySize5
    global id5
    global EntrySize6
    global id6
    global EntrySize7
    global id7
    global EntrySize8
    global id8
    global EntrySize9
    global id9
    global EntrySize10
    global id10
    global EntrySize11
    global id11
    global EntrySize12
    global id12
    global EntrySize13
    global id13
    global EntrySize14
    global id14
    global EntrySize15
    global id15
    global EntrySize16
    global id16
    global EntrySize17
    global id17
    global cameraCount
    global cameraCount2

    ob = bpy.context.object

    idx=0
    Version = unpack("<I", f.read(4))[0]
    if Version == 1:
        EntrySize1 = unpack("<H", f.read(2))[0]
        id1 = unpack("<H", f.read(2))[0]
        FloatCount = unpack("<f", f.read(4))[0]
        unk01 = unpack("<I", f.read(4))[0]
        EntrySize2 = unpack("<H", f.read(2))[0]
        id2 = unpack("<H", f.read(2))[0]
        EntrySize3 = unpack("<H", f.read(2))[0]
        id3 = unpack("<H", f.read(2))[0]
        EntrySize4 = unpack("<H", f.read(2))[0]
        id4= unpack("<H", f.read(2))[0]
        EntrySize5 = unpack("<H", f.read(2))[0]
        id5= unpack("<H", f.read(2))[0]
        cameraCount = unpack("<I", f.read(4))[0]
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
        unk01 = unpack("<I", f.read(4))[0]
        EntrySize2 = unpack("<H", f.read(2))[0]
        id2 = unpack("<H", f.read(2))[0]
        EntrySize3 = unpack("<H", f.read(2))[0]
        id3 = unpack("<H", f.read(2))[0]
        EntrySize4 = unpack("<H", f.read(2))[0]
        id4= unpack("<H", f.read(2))[0]
        EntrySize5 = unpack("<H", f.read(2))[0]
        id5= unpack("<H", f.read(2))[0]
        EntrySize6 = unpack("<H", f.read(2))[0]
        id6= unpack("<H", f.read(2))[0]
        EntrySize7 = unpack("<H", f.read(2))[0]
        id7= unpack("<H", f.read(2))[0]
        EntrySize8 = unpack("<H", f.read(2))[0]
        id8= unpack("<H", f.read(2))[0]
        EntrySize9 = unpack("<H", f.read(2))[0]
        id9= unpack("<H", f.read(2))[0]
        EntrySize10 = unpack("<H", f.read(2))[0]
        id10= unpack("<H", f.read(2))[0]
        EntrySize11 = unpack("<H", f.read(2))[0]
        id11= unpack("<H", f.read(2))[0]
        EntrySize12 = unpack("<H", f.read(2))[0]
        id12= unpack("<H", f.read(2))[0]
        EntrySize13 = unpack("<H", f.read(2))[0]
        id13= unpack("<H", f.read(2))[0]
        EntrySize14 = unpack("<H", f.read(2))[0]
        id14= unpack("<H", f.read(2))[0]
        EntrySize15 = unpack("<H", f.read(2))[0]
        id15= unpack("<H", f.read(2))[0]
        EntrySize16 = unpack("<H", f.read(2))[0]
        id16= unpack("<H", f.read(2))[0]
        EntrySize17 = unpack("<H", f.read(2))[0]
        id17= unpack("<H", f.read(2))[0]
        cameraCount2 = unpack("<I", f.read(4))[0]

        bpy.context.scene.render.fps = 30
        bpy.context.scene.render.fps_base = 1
        bpy.context.scene.unit_settings.system_rotation = "RADIANS"

        for pbone in ob.pose.bones:
            pbone.rotation_mode = "XYZ"

        bpy.context.scene.frame_end = int(FloatCount)
        bpy.context.scene.frame_current = 1
        bpy.context.scene.frame_start = 1

        ob.shape_key_add(name = 'BlendShape Base')
        blendshape = ob.shape_key_add(name = "CUT BlendShape Key")

def cut_exportV2_parser(f):
    
    ob = bpy.context.object

    idx=0
    if Version == 1:
        f.write(pack("<I", Version-Version+1))
        f.write(pack("<H", EntrySize1-EntrySize1+32))
        f.write(pack("<H", id1-id1))
        f.write(pack("<f", FloatCount-FloatCount+bpy.context.scene.frame_end))
        f.write(pack("<I", unk01))
        f.write(pack("<H", EntrySize2-EntrySize2+80))
        f.write(pack("<H", id2-id2))
        f.write(pack("<H", EntrySize3))
        f.write(pack("<H", id3-id3))
        f.write(pack("<H", EntrySize4))
        f.write(pack("<H", id4-id4))
        f.write(pack("<H", EntrySize5))
        f.write(pack("<H", id5-id5))
        f.write(pack("<I", cameraCount-cameraCount+len(bpy.data.cameras)))
        
    elif Version == 2:
        f.write(pack("<I", Version-Version+2))
        f.write(pack("<H", EntrySize1-EntrySize1+32))
        f.write(pack("<H", id1-id1))
        f.write(pack("<f", FloatCount-FloatCount+bpy.context.scene.frame_end))
        f.write(pack("<I", unk01))
        f.write(pack("<H", EntrySize2-EntrySize2+112))
        f.write(pack("<H", id2-id2))
        f.write(pack("<H", EntrySize3))
        f.write(pack("<H", id3-id3))
        f.write(pack("<H", EntrySize4))
        f.write(pack("<H", id4-id4))
        f.write(pack("<H", EntrySize5))
        f.write(pack("<H", id5-id5))
        f.write(pack("<H", EntrySize6))
        f.write(pack("<H", id6-id6))
        f.write(pack("<H", EntrySize7))
        f.write(pack("<H", id7-id7))
        f.write(pack("<H", EntrySize8))
        f.write(pack("<H", id8-id8))
        f.write(pack("<H", EntrySize9))
        f.write(pack("<H", id9-id9))
        f.write(pack("<H", EntrySize10))
        f.write(pack("<H", id10-id10))
        f.write(pack("<H", EntrySize11))
        f.write(pack("<H", id11-id11))
        f.write(pack("<H", EntrySize12))
        f.write(pack("<H", id12-id12))
        f.write(pack("<H", EntrySize13))
        f.write(pack("<H", id13-id13))
        f.write(pack("<H", EntrySize14))
        f.write(pack("<H", id14-id14))
        f.write(pack("<H", EntrySize15))
        f.write(pack("<H", id15-id15))
        f.write(pack("<H", EntrySize16))
        f.write(pack("<H", id16-id16))
        f.write(pack("<H", EntrySize17))
        f.write(pack("<H", id17-id17))
        f.write(pack("<I", cameraCount2-cameraCount2+len(bpy.data.cameras)))
        
