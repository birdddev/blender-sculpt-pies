bl_info = {
    "name": "Sculpt Pie Menus",
    "description": "Adds pie menus that groups certain sculpt tools together",
    "author": "bird_d",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "Sculpt Mode",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "support": 'COMMUNITY',
    "category": "Sculpting"
}

##TODO: Make the addon handle temporarily overwrite default keymaps instead of making user make their own/overwrite it themselves

import bpy
import rna_keymap_ui
from bpy.types import Menu

#region /Brushes/
blue = [
    "Draw",
    "Clay",
    "Clay Strips",
    "Layer",
    "Blob",
    "Crease"
]

red = [
    "Smooth",
    "Flatten",
    "Fill",
    "Scrape",
    "Pinch"
]

yellow = [
    "Grab",
    "Snake Hook",
    "Thumb",
    "Nudge",
    "Rotate"
]

white = [
    "Simplify",
    "Mask",
    "Box Mask",
    "Box Hide"
]
#endregion /Brushes/

# addon_keymaps = []

# class SculptPiePreferences(bpy.types.AddonPreferences):
#     bl_idname = __name__

#     def draw(self, context):
#         layout=self.layout
#         box = layout.box()

#         wm = bpy.context.window_manager
#         # kc = wm.keyconfigs.addon
#         kc = wm.keyconfigs.user

#         #from . keys import keys

#         split = box.split()

#         b = split.box()
#         b.label(text="Keymaps")
#         col = b.column()

#         for km, kmi in addon_keymaps:
#             km.active()
#             col.context_pointer_set("keymap", km)
#             rna_keymap_ui.draw_kmi(["ADDON", "USER", "DEFAULT"], kc, km, kmi, col, 0)

def master_poll(context):
    if context.object is None:
        return False
    if context.object.mode != "SCULPT":
        return False
    return True

def build_brush_pie_menu(pie, brushes):
    for b in brushes:
        op = pie.operator("wm.tool_set_by_id", text=b)
        op.name = "builtin_brush.%s" % b

class BRDD_MT_blue(Menu):
    bl_label = "Blue Pies"

    @classmethod
    def poll(self, context):
        return master_poll(context)

    def draw(self, context):
        layout = self.layout
        p = layout.menu_pie()
        build_brush_pie_menu(p, blue)

class BRDD_MT_red(Menu):
    bl_label = "Red Pies"

    @classmethod
    def poll(self, context):
        return master_poll(context)

    def draw(self, context):
        layout = self.layout
        p = layout.menu_pie()
        build_brush_pie_menu(p, red)

class BRDD_MT_yellow(Menu):
    bl_label = "Yellow Pies"

    @classmethod
    def poll(self, context):
        return master_poll(context)

    def draw(self, context):
        layout = self.layout
        p = layout.menu_pie()
        build_brush_pie_menu(p, yellow)

class BRDD_MT_white(Menu):
    bl_label = "White Pies"

    @classmethod
    def poll(self, context):
        return master_poll(context)

    def draw(self, context):
        layout = self.layout
        p = layout.menu_pie()
        build_brush_pie_menu(p, white)

classes = [
    #SculptPiePreferences,
    BRDD_MT_blue,
    BRDD_MT_red,
    BRDD_MT_yellow,
    BRDD_MT_white
]

def register():
    print("Registering Sculpt-Pie-Menus")

    for c in classes:
        bpy.utils.register_class(c)

    ##Register keymaps
    # Keymapping

    # wm = bpy.context.window_manager
    # kc = wm.keyconfigs.addon
    # km = kc.keymaps.new(name="3D View", space_type='VIEW_3D')
    # kmi = km.keymap_items.new("wm.call_menu_pie", 'C', 'PRESS')
    # kmi.properties.name = "BRDD_MT_BLUE_TEMPLATE"
    # kmi.active = True
    # addon_keymaps.append((km, kmi))

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)

    # for km, kmi in addon_keymaps:
    #     km.keymap_items.remove(kmi)
    # addon_keymaps.clear()
        