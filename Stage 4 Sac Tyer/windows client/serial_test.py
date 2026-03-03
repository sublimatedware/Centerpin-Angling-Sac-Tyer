import dearpygui.dearpygui as dpg
import serial
import serial.tools.list_ports

SERIAL_BAUDRATE = 9600
SERIAL_TIMEOUT = 1

serial_connection = None


def get_serial_ports():
    """Return a list of serial port device names."""
    ports = serial.tools.list_ports.comports()
    return [port.device for port in ports]


def refresh_ports():
    ports = serial.tools.list_ports.comports()
    dpg.configure_item("serial_listbox", items=ports)

    if ports:
        dpg.set_value("serial_listbox", ports[0])
    else:
        dpg.set_value("serial_listbox", "")


def send_data():
    global serial_connection

    port = dpg.get_value("serial_listbox")
    if not port:
        print("No serial port selected")
        return

    try:
        if serial_connection is None or serial_connection.port != port:
            if serial_connection:
                serial_connection.close()

            serial_connection = serial.Serial(
                port=port,
                baudrate=SERIAL_BAUDRATE,
                timeout=SERIAL_TIMEOUT
            )

        data = b"Hello from Dear PyGui!\n"
        serial_connection.write(data)
        print(f"Sent data to {port}")

    except serial.SerialException as e:
        print(f"Serial error: {e}")


dpg.create_context()

with dpg.window(label="Serial Device Sender", width=400, height=200):
    dpg.add_text("Connected Serial Devices")

    dpg.add_listbox(
        tag="serial_listbox",
        items=[],
        width=300,
        num_items=5
    )

    dpg.add_spacer(height=5)

    dpg.add_button(label="Refresh Devices", callback=refresh_ports)
    dpg.add_button(label="Send Data", callback=send_data)

refresh_ports()

dpg.create_viewport(title="Serial GUI", width=420, height=250)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()