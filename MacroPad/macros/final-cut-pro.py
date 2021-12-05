# MACROPAD Hotkeys example: Final Cut Pro for Mac

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                       # REQUIRED dict, must be named 'app'
    'name' : 'Final Cut Pro', # Application name
    'macros' : [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'Import', [Keycode.COMMAND, 'i']),
        (0x202000, 'Mk_Srt', 'i'),
        (0x202000, 'Mk_End', 'o'),   # Cycle brush modes
        # 2nd row ----------
        (0x000040, 'X_Fade', [Keycode.OPTION, 't']),
        (0x004000, 'Vol Up', [Keycode.CONTROL, '=']),
        (0x400000, 'Vol Dn', [Keycode.CONTROL, '-']),
        # 3rd row ----------
        (0x400000, 'Blade', [Keycode.COMMAND, 'b']),
        (0x400000, 'T_Srt', [Keycode.OPTION, '[']),
        (0x400000, 'T_End', [Keycode.OPTION, ']']),
        # 4th row ----------
        (0x000000, '', 'I'),
        (0x000040, 'Z_In', [Keycode.COMMAND, '=']),
        (0x000040, 'Z_Out', [Keycode.COMMAND, '-']),
        # Encoder button ---
        (0x000000, '', [Keycode.COMMAND, 'S'])
    ]
}
