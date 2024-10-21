import ssdp
import requests
import socket
import time
from StreamDeck.DeviceManager import DeviceManager

# Placeholder URL suffix for PTZ camera control (replace with actual control API if available)
CONTROL_SUFFIX = "/control?power="

LUMENS_DEVICE_TYPE = "ptz"  # Placeholder; this could be specific to the Lumens device if it uses specific identifiers.

def discover_ptz_devices():
    """
    Discover PTZ devices using SSDP on the local network.
    This will return the IP addresses of devices that respond with appropriate control endpoints.
    """
    print("Discovering PTZ devices on the local network via SSDP...")
    devices = ssdp.discover("ssdp:all")
    
    # Filter discovered devices based on 'ptz' keyword or specific device type in their description
    ptz_devices = [device.location for device in devices if LUMENS_DEVICE_TYPE in device.server.lower()]
    
    if ptz_devices:
        print(f"PTZ devices found: {ptz_devices}")
    else:
        print("No PTZ devices found on the network.")
    
    return ptz_devices

def send_power_command(ip, power_state):
    """
    Send a power on/off command to the PTZ device.
    """
    try:
        url = f"http://{ip}{CONTROL_SUFFIX}{power_state}"
        response = requests.get(url)
        print(f"Command sent to {ip}, response: {response.status_code}")
    except Exception as e:
        print(f"Error sending command to {ip}: {str(e)}")

def setup_streamdeck(devices):
    """
    Sets up the Stream Deck with buttons to control PTZ devices.
    """
    decks = DeviceManager().enumerate()
    if not decks:
        print("No Stream Deck found.")
        return

    deck = decks[0]
    deck.open()
    deck.reset()

    # Setup a button for each PTZ device found
    for i, ip in enumerate(devices[:deck.key_count()]):  # Limit to the number of keys available on the deck
        # Toggle on/off with each button press
        deck.set_key_callback(i, lambda deck, key, state, ip=ip: send_power_command(ip, 'toggle') if state else None)
        deck.set_key_image(i, "path/to/your/image.png")  # Assumes you have an image for the button

    print("Stream Deck is ready. Press buttons to control PTZ devices.")

def wait_for_ptz_connection():
    """
    Continuously wait for PTZ device to connect via USB, and then discover its IP via SSDP.
    This simulates the PTZ camera being plugged into the network and registering.
    """
    while True:
        ptz_devices = discover_ptz_devices()
        if ptz_devices:
            print(f"PTZ devices discovered: {ptz_devices}")
            return ptz_devices
        else:
            print("Waiting for PTZ device to connect...")
            time.sleep(5)  # Wait before trying again

def main():
    print("Waiting for PTZ camera to be plugged in and registered on the network...")
    ptz_devices = wait_for_ptz_connection()  # Wait for the PTZ to be discovered via network
    if ptz_devices:
        print(f"PTZ devices ready for control: {ptz_devices}")
        setup_streamdeck(ptz_devices)
    else:
        print("No PTZ devices found to control.")

if __name__ == "__main__":
    main()
 