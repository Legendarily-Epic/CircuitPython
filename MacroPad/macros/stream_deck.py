# MACROPAD Hotkeys example: Stream Deck

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                       # REQUIRED dict, must be named 'app'
    'name' : 'Stream Deck', # Application name
    'macros' : [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x400000, 'Front', [Keycode.ALT,'1',-Keycode.ALT]),
        (0x000040, 'Top', [Keycode.ALT,'2',-Keycode.ALT]),
        (0x101010, 'Side', [Keycode.ALT,'3',-Keycode.ALT]),
        # 2nd row ----------
        (0x400000, 'Desktop', [Keycode.ALT,'d',-Keycode.ALT]),
        (0x000040, '', [Keycode.ALT,'2',-Keycode.ALT]),
        (0x101010, '', [Keycode.ALT,'3',-Keycode.ALT]),
        # 3rd row ----------
        (0x400000, 'Intro', [Keycode.ALT,'7',-Keycode.ALT]),
        (0x000040, 'BRB', [Keycode.ALT,'9',-Keycode.ALT]),
        (0x101010, 'Outro', [Keycode.ALT,'8',-Keycode.ALT]),
        # 4th row ----------
        (0x400000, 'Start', [Keycode.ALT,'r',-Keycode.ALT]),
        (0x002000, 'Stop', [Keycode.ALT,'s',-Keycode.ALT]),
        (0x202000, 'Mute', [Keycode.ALT,'m',-Keycode.ALT]),
        # Encoder button ---
        (0x000000, '', [])
    ]
}