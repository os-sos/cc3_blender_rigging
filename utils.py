import bpy


def log_info(msg, self = None):
    """Log an info message to console."""
    print(msg)
    if self:
        self.report({'INFO'}, msg)


def log_warn(msg, self = None):
    """Log a warning message to console."""
    print("Warning: " + msg)
    if self:
        self.report({'WARNING'}, msg)


def log_error(msg, self = None):
    """Log an error message to console and raise an exception."""
    print("Error: " + msg)
    if self:
        self.report({'ERROR'}, msg)


def get_active_object():
    return bpy.context.view_layer.objects.active


def set_active_object(obj):
    bpy.context.view_layer.objects.active = obj
    return bpy.context.active_object == obj


def set_mode(mode):
    if bpy.context.object == None:
        if mode != "OBJECT":
            log_error("No context object, unable to set any mode but OBJECT!")
            return False
        return True
    else:
        bpy.ops.object.mode_set(mode=mode)
        if bpy.context.object.mode != mode:
            log_error("Unable to set " + mode + " on object: " + bpy.context.object.name)
            return False
        return True


def edit_mode_to(obj):
    if set_mode("OBJECT") and set_active_object(obj) and set_mode("EDIT"):
        return True
    return False


def find_cc3_rig(objects):
    for obj in objects:
        if obj.type == "ARMATURE":
            if "Base_Spine01" in obj.pose.bones or "CC_Base_Spine01" in obj.pose.bones:
                return obj
    return None


def rest_pose(rig):
    if rig is not None and rig.type == "ARMATURE":
        rig.data.pose_position = 'REST'
        return True
    return False