README for PTZ Controller Macro for Streamdeck Devices

by Doc McDowell
written originally in Python

Usage:

    Connect the Lumens PTZ Camera:
        Plug the Lumens PTZ camera into your Windows 11 machine via USB.

    Run the Script:
        The script will automatically discover the PTZ camera’s IP address via SSDP. The camera will register on the network once it is connected.
        The StreamDeck buttons will be configured to control the camera.

    Control the Camera:
        Use the StreamDeck to control the camera, starting with power on/off. Additional controls (like pan, tilt, zoom) can be configured by extending the command API.

Updates Log:
May 2024 - Project Initialization:

    Initial setup for integrating StreamDeck with PTZ cameras.
    Basic functionality for detecting StreamDeck and mapping buttons was established.
    SSDP-based network discovery was initially implemented but did not yet integrate with Lumens PTZ-specific commands.

June 2024 - July 2024:

    Worked on improving SSDP discovery and ensuring PTZ cameras were detectable over the network.
    Added placeholder functions for power on/off commands.
    Initial tests with StreamDeck buttons to send basic HTTP requests to the discovered IP addresses.

August 29th, 2024 - Milestone Completion:

    StreamDeck integration fully functional.
        Buttons were successfully mapped to PTZ cameras using their discovered IP addresses.
    Added more robust SSDP-based device filtering to ensure only relevant PTZ devices were targeted.
    Basic control features (power on/off) completed and tested.

October 21st, 2024 - Automatic Detection and Plug-and-Play Update:

    New Features:
        Added automatic USB detection for Lumens PTZ cameras, eliminating the need for manual user input.
        The system now continuously scans for the PTZ device and discovers its IP address without needing to point to any specific paths.
    StreamDeck now supports plug-and-play behavior, automatically updating controls when a PTZ camera is connected to the system.
    Error handling improvements for detecting when the PTZ device is not connected or if the network discovery fails.

Future Enhancements:

    Advanced PTZ Control:
        Add support for panning, tilting, and zooming via StreamDeck buttons using specific API calls from the Lumens PTZ camera.

    Multi-Device Support:
        Expand functionality to control multiple PTZ cameras simultaneously via StreamDeck.

    GUI for Manual Control:
        Develop a simple GUI for users to manually select and control PTZ cameras if necessary, providing flexibility alongside automatic detection.

Troubleshooting:

    No PTZ Device Found:
        Ensure the Lumens PTZ camera is properly plugged in via USB and that it is registering on the network.
        Check the SSDP logs to ensure the device is being discovered.

    StreamDeck Not Found:
        Make sure the StreamDeck device is plugged in and recognized by the system.
        Try resetting the StreamDeck by unplugging and replugging it.

    Commands Not Working:
        Verify that the PTZ control API URL is correct and that the PTZ camera is reachable over the network. You can test this by sending HTTP requests manually via a tool like curl or Postman.

Contact:

For any issues or further improvements, please open a ticket on the GitHub repository or contact the project maintainer at [Your Email].
License:

This project is licensed under the MIT License. See the LICENSE file for more details.