from struct import unpack, pack, error
import bpy
import os
import mathutils
import math

def cut_importV2_parser(f):
    global Version

    idx=0
    version = unpack("<I", f.read(4))[0]
    if Version == 1:
        pass
    elif Version == 2:
        pass
