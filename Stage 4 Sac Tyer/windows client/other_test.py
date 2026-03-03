# import dearpygui.dearpygui as dpg

# dpg.create_context()
# dpg.create_viewport()
# dpg.setup_dearpygui()

# with dpg.theme() as disabled_theme:
#     with dpg.theme_component(dpg.mvInputFloat, enabled_state=False):
#         dpg.add_theme_color(dpg.mvThemeCol_Text, [255, 0, 0])
#         dpg.add_theme_color(dpg.mvThemeCol_Button, [255, 0, 0])

#     with dpg.theme_component(dpg.mvInputInt, enabled_state=False):
#         dpg.add_theme_color(dpg.mvThemeCol_Text, [255, 0, 0])
#         dpg.add_theme_color(dpg.mvThemeCol_Button, [255, 0, 0])

# dpg.bind_theme(disabled_theme)

# with dpg.window(label="tutorial"):
#     dpg.add_input_float(label="Input float", enabled=True)
#     dpg.add_input_int(label="Input int", enabled=False)

# dpg.show_viewport()
# dpg.start_dearpygui()
# dpg.destroy_context()


#####################################################################
# import dearpygui.dearpygui as dpg

# dpg.create_context()
# dpg.create_viewport()
# dpg.setup_dearpygui()

# with dpg.theme() as global_theme:

#     with dpg.theme_component(dpg.mvInputFloat, enabled_state=True):
#         dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 0, 0), category=dpg.mvThemeCat_Core)


# dpg.bind_theme(global_theme)

# with dpg.window(label="tutorial"):
#     dpg.add_input_float(label="Input float", enabled=False)
#     dpg.add_input_int(label="Input int", enabled=False)

# dpg.show_viewport()
# dpg.start_dearpygui()
# dpg.destroy_context()

##########################################################################################################

import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.window(label="Error", modal=True, show=False, tag="modal_id", width=300):
    dpg.set_item_pos("modal_id",(200,200))
    dpg.add_text("The specified serial device was not connected successfully. Please try reinserting the device, and ensuring the device labelled 'USB Serial Device' is selected. Thanks Dawg.",wrap=0)
    dpg.add_separator()
    with dpg.group(horizontal=True):
        dpg.add_button(label="OK", width=75, callback=lambda: dpg.configure_item("modal_id", show=False))

with dpg.window(label="Tutorial"):
    dpg.add_button(label="Open Dialog", callback=lambda: dpg.configure_item("modal_id", show=True))

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

################################################################################

