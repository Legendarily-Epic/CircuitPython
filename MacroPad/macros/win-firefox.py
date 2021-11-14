# MACROPAD Hotkeys example: Firefox web browser for Windows

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                       # REQUIRED dict, must be named 'app'
    'name' : 'Windows Firefox', # Application name
    'macros' : [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, '< Back', [Keycode.ALT, Keycode.LEFT_ARROW]),
        (0x004000, 'Fwd >', [Keycode.ALT, Keycode.RIGHT_ARROW]),
        (0x400000, 'Up', [Keycode.SHIFT, ' ']),      # Scroll up
        # 2nd row ----------
        (0x202000, '< Tab', [Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB]),
        (0x202000, 'Tab >', [Keycode.CONTROL, Keycode.TAB]),
        (0x400000, 'Down', ' '),                     # Scroll down
        # 3rd row ----------
        (0x000040, 'Reload', [Keycode.CONTROL, 'r']),
        (0x000040, 'Home', [Keycode.ALT, Keycode.HOME]),
        (0x000040, 'Private', [Keycode.CONTROL, Keycode.SHIFT, 'p']),
        # 4th row ----------
        (0x101010, 'Ada', [Keycode.CONTROL, 't', -Keycode.CONTROL,
                           'www.adafruit.com\n']), # adafruit.com in a new tab
        (0x000040, 'Dev Mode', [Keycode.F12]),     # dev mode
        (0x101010, 'Digi', [Keycode.CONTROL, 't', -Keycode.CONTROL,
                            'digikey.com\n']),     # digikey in a new tab
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w']) # Close window/tab
    ]
}