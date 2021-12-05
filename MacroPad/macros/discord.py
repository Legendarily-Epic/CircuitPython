# MACROPAD Hotkeys example: Discord

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                       # REQUIRED dict, must be named 'app'
    'name' : 'Discord', # Application name
    'macros' : [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'Reply', [Keycode.R]),
        (0x000040, '<<SERV', [Keycode.COMMAND, Keycode.OPTION, Keycode.UP_ARROW]),
        (0x000040, 'SERV>>', [Keycode.COMMAND, Keycode.OPTION, Keycode.DOWN_ARROW]),
        # 2nd row ----------
        (0x004000, 'React', [Keycode.KEYPAD_PLUS]),
        (0x202000, '<<CHAN', [Keycode.OPTION, Keycode.UP_ARROW]),
        (0x202000, 'CHAN>>', [Keycode.OPTION, Keycode.DOWN_ARROW]),
        # 3rd row ----------
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),
        # 4th row ----------
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),
        # Encoder button ---
        (0x000000, '', [])
    ]
}
