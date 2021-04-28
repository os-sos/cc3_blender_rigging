

if "bpy" in locals():
    import importlib
    importlib.reload(rigify)
    importlib.reload(utils)
    importlib.reload(geom)

import bpy
import os
from . import rigify
from . import utils
from . import geom

bl_info = {
    "name": "CC3 Rigging",
    "author": "Victor Soupday",
    "version": (0, 1, 1),
    "blender": (2, 80, 0),
    "category": "Rigging",
    "location": "3D View > Properties> CC3 Rigging",
    "description": "Rigging and stuff.",
}

CLASSES = (rigify.CC3Rigifier, rigify.CC3RigifyPanel)

def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls)
    #bpy.types.Scene.CC3RiggingProps = bpy.props.PointerProperty(type=CC3RiggingProps)

def unregister():
    for cls in CLASSES:
        bpy.utils.unregister_class(cls)
    #del(bpy.types.Scene.CC3RiggingProps)