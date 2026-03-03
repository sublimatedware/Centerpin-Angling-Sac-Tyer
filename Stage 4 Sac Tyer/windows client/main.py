import dearpygui.dearpygui as dpg
import os
import sys
import time
import serial
import serial.tools.list_ports
import threading

def refresh_ports():
    global ports
    ports = serial.tools.list_ports.comports(include_links=False)
    dpg.configure_item("serial_listbox", items=ports)
    if ports:
        dpg.set_value("serial_listbox", ports[0])
    else:
        dpg.set_value("serial_listbox", "")

def Serial_Connect_CallBack():
    truncatedPorts = []
    for port in ports:
        truncatedPorts.append(str(port))
    truncatedPorts.index(dpg.get_value("serial_listbox"))
    try:
        global ser
        ser = serial.Serial(ports[truncatedPorts.index(dpg.get_value("serial_listbox"))][0], baudrate=230400)
        ser.write(b'ayy')
        time.sleep(0.01)
        serialIn = ser.read(4)
        print(serialIn)
        if serialIn == b'lmao':
            dpg.configure_item("Refresh", enabled = False)
            dpg.configure_item("Connect Serial", enabled = False)
            dpg.configure_item("Compress Sack", enabled = True)
            dpg.configure_item("Expand Sack", enabled = True)
            dpg.configure_item("Twist Sack", enabled = True)
            dpg.configure_item("UnTwist Sack", enabled = True)
            dpg.configure_item("Set CW", enabled = True)
            dpg.configure_item("Set CCW", enabled = True)
            dpg.configure_item("Set Speed", enabled = True)
            dpg.configure_item("Speed Bax", enabled = True)
            dpg.configure_item("Set Steps", enabled = True)
            dpg.configure_item("Step Bax", enabled = True)
            ser.write(b'okk')
            threading.Thread(target=serialDoShit).start()
        else:
            raise Exception("The device did not respond to the request to connect. Maybe the device is not the Tight-Sac O-Matic 69000")
  
    except Exception as e:
        dpg.configure_item("modal_id", show=True)
        dpg.set_value("error text", e)

def Compress_Sack_CallBack():
    ser.write(b'aaa')                   #compress sack  direction change, pin pb6 high

def Expand_Sack_CallBack():
    ser.write(b'aab')                   #expand sack  direction change, pin pb6 low

def Twist_Sack_CallBack():
    ser.write(b'aac')                   #this is going to be the twist machine

def UnTwist_Sack_CallBack():
    ser.write(b'aad')                   #twist machine
    print("hungry for juicy pussy, utterly deprived, desperate")

def Set_CW_CallBack():
    ser.write(b'aae')                   #Set CW rotation

def Set_CCW_CallBack():
    ser.write(b'aaf')                   #Set CCW rotation

def sac_open_key():
    ser.write(b'aab')                   #expand sack  direction change, pin pb6 low

def sac_close_key():
    ser.write(b'aaa')                   #compress sack  direction change, pin pb6 high

def Set_Speed_Callback():
    char2 = int(dpg.get_value("Speed Bax")) & 0x00ff
    char1 = int(dpg.get_value("Speed Bax")) >> 8


    #ser.write(int('b')+ (char1) + char2)
    ser.write((b'b') + char1.to_bytes() + char2.to_bytes())
    #print(int('b')+ (char1) + char2)

def Set_Steps_Callback():
    char2 = int(dpg.get_value("Step Bax")) & 0x00ff
    char1 = int(dpg.get_value("Step Bax")) >> 8
    ser.write((b'c') + char1.to_bytes() + char2.to_bytes())

def Gay_Button_Callback():
    #put some useful shit here
    print("Gay")

def serialDoShit():
    while True:
        print(ser.readline())
        if ser.readline() == b'butt\n':
            dpg.configure_item("LED", fill=(255,0,0,255))
            ser.reset_input_buffer()
        else:
            dpg.configure_item("LED", fill=(0,0,0,255))


dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

with dpg.handler_registry():
    dpg.add_key_press_handler(key=dpg.mvKey_NumPad8, callback=sac_open_key)
    dpg.add_key_press_handler(key=dpg.mvKey_NumPad2, callback=sac_close_key)

with dpg.theme() as disabled_theme:
    with dpg.theme_component(dpg.mvButton, enabled_state=False):
        dpg.add_theme_color(dpg.mvThemeCol_Text, (150, 150, 150))
        dpg.add_theme_color(dpg.mvThemeCol_Button, (100, 100, 100))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (100, 100, 100))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (100, 100, 100))

dpg.bind_theme(disabled_theme)

with dpg.window(label="Tight-Sac O-Matic 69000"):
    dpg.add_text("Serial Device List")
    dpg.add_listbox(tag="serial_listbox",items=[],width = 300)
    dpg.add_button(label="Refresh Devices", tag="Refresh", callback=refresh_ports)
    dpg.add_button(label="Establish Serial Connection", tag="Connect Serial", callback=Serial_Connect_CallBack)
    dpg.add_button(label="Compress Sack", tag="Compress Sack", callback=Compress_Sack_CallBack, enabled=False)
    dpg.add_button(label="Expand Sack", tag="Expand Sack", callback=Expand_Sack_CallBack, enabled=False)
    dpg.add_button(label="Twist Sack", tag="Twist Sack", callback=Twist_Sack_CallBack, enabled=False)
    dpg.add_button(label="UnTwist Sack", tag="UnTwist Sack", callback=UnTwist_Sack_CallBack, enabled=False)
    dpg.add_button(label="Set Clockwise", tag="Set CW", callback=Set_CW_CallBack, enabled=False)
    dpg.add_button(label="Set Counter Clockwise", tag="Set CCW", callback=Set_CCW_CallBack, enabled=False)
    with dpg.group(horizontal=True):
        dpg.add_input_text(width=100, tag="Speed Bax",enabled=False)
        dpg.add_button(label="Set Counter Period", tag="Set Speed", callback=Set_Speed_Callback, enabled=False)
    dpg.add_button(label="Gay Button", tag="Gay Button", callback=Gay_Button_Callback, enabled=True)
    with dpg.group(horizontal=True):
        dpg.add_input_text(width=100, tag="Step Bax",enabled=False)
        dpg.add_button(label="Set Steps", tag="Set Steps", callback=Set_Steps_Callback, enabled=False)
    dpg.draw_rectangle      (   pmin=(202, 113),
                                pmax=(217, 128),
                                color=(51,51,55,255),
                                label = "LED",
                                tag = "LED",
                                fill=(0,0,0,255)
                            )

with dpg.window(label="Error", modal=True, show=False, tag="modal_id", width=300):
    dpg.set_item_pos("modal_id",(200,200))
    #dpg.add_text("The specified serial device was not connected successfully. Please try reinserting the device, and ensuring the device labelled 'USB Serial Device' is selected. Thanks Dawg.",wrap=0, tag="error text")
    dpg.add_text("Super fucked up error just occured. Thanks Dawg.",wrap=0, tag="error text")
    dpg.add_separator()
    with dpg.group(horizontal=True):
        dpg.add_button(label="OK", width=75, callback=lambda: dpg.configure_item("modal_id", show=False))

refresh_ports()


dpg.show_viewport()
print("im gay")

dpg.start_dearpygui()
print("im not gay")
dpg.destroy_context()
