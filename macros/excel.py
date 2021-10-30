# MACROPAD Hotkeys example: Excel

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                       # REQUIRED dict, must be named 'app'
    'name' : 'Excel', # Application name
    'macros' : [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x400000, 'ClrFtr', [Keycode.ALT, -Keycode.ALT, 0.5, 'h', 0.5, 's', 0.5, 'c', 0.5, Keycode.ENTER, -Keycode.ENTER]),
        (0x000000, '', ['rick.tompkins', Keycode.TAB,
                           'Rct.031293\n']),
        (0x000000, '', ['rick.tompkins', Keycode.TAB,
                           'Rct.031293\n']),
        # 2nd row ----------
        (0x000000, '', ['e400646']),
        (0x000000, '', ['rick.tompkins']),
        (0x000000, '', ['rick.tompkins']),
        # 3rd row ----------
        (0x000000, '', ['XSW@3edcvb\n']),
        (0x000000, '', ['Rct.031293\n']),
        (0x000000, '', ['Rct.031293\n']),
        # 4th row ----------
        (0x202000, '<Sheet', [Keycode.CONTROL, Keycode.PAGE_UP]),
        (0x000000, '', [Keycode.ALT, -Keycode.ALT, Keycode.RIGHT_ARROW, -Keycode.RIGHT_ARROW, Keycode.RIGHT_ARROW, -Keycode.RIGHT_ARROW, Keycode.DOWN_ARROW, -Keycode.DOWN_ARROW, Keycode.DOWN_ARROW, -Keycode.DOWN_ARROW, Keycode.DOWN_ARROW, -Keycode.DOWN_ARROW, Keycode.ENTER]),
        (0x202000, 'Sheet>', [Keycode.CONTROL, Keycode.PAGE_DOWN]),
        # Encoder button ---
        (0x000000, '', [Keycode.WINDOWS, 'l']) # Lock Computer
    ]
}
