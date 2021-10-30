# MACROPAD Hotkeys example: Honeywell

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                       # REQUIRED dict, must be named 'app'
    'name' : 'Honeywell', # Application name
    'macros' : [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x400000, 'LDAP', [Keycode.DOWN_ARROW, -Keycode.DOWN_ARROW, 0.5, Keycode.ENTER, -Keycode.ENTER, 0.5, 'XSW@3edcvb\n']),
        (0x000040, 'Oracle', ['rick.tompkins', Keycode.TAB,
                           'Rct.031293\n']),
        (0x101010, 'Kronos', ['rick.tompkins', Keycode.TAB,
                           'Rct.031293\n']),
        # 2nd row ----------
        (0x400000, 'ID', ['e400646']),
        (0x000040, 'ID', ['rick.tompkins']),
        (0x101010, 'ID', ['rick.tompkins']),
        # 3rd row ----------
        (0x400000, 'Pass', ['XSW@3edcvb\n']),
        (0x000040, 'Pass', ['Rct.031293\n']),
        (0x101010, 'Pass', ['Rct.031293\n']),
        # 4th row ----------
        (0x400000, 'Lock', [Keycode.DOWN_ARROW, -Keycode.DOWN_ARROW, 0.5, 'XSW@3edcvb\n']),
        (0x002000, 'Find', [Keycode.ALT, -Keycode.ALT, Keycode.RIGHT_ARROW, -Keycode.RIGHT_ARROW, Keycode.RIGHT_ARROW, -Keycode.RIGHT_ARROW, Keycode.DOWN_ARROW, -Keycode.DOWN_ARROW, Keycode.DOWN_ARROW, -Keycode.DOWN_ARROW, Keycode.DOWN_ARROW, -Keycode.DOWN_ARROW, Keycode.ENTER]),
        (0x202000, 'VPN', ['Rct.3045', Keycode.ENTER]),
        # Encoder button ---
        (0x000000, '', [Keycode.WINDOWS, 'l']) # Lock Computer
    ]
}