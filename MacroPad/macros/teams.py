# MACROPAD Hotkeys example: Teams

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                       # REQUIRED dict, must be named 'app'
    'name' : 'Teams', # Application name
    'macros' : [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),
        # 2nd row ----------
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),
        # 3rd row ----------
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),
        # 4th row ----------
        (0x000000, '', []),
        (0x400000, 'Mute', [Keycode.CONTROL, Keycode.SHIFT, Keycode.M,
                            -Keycode.CONTROL, -Keycode.SHIFT, -Keycode.M]),
        (0x000000, '', []),
        # Encoder button ---
        (0x000000, '', [Keycode.WINDOWS, 'l']) # Lock Computer
    ]
}
