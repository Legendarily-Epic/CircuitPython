# MACROPAD Hotkeys example: Logins

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                       # REQUIRED dict, must be named 'app'
    'name' : 'Logins', # Application name
    'macros' : [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x400000, 'LDAP', [Keycode.DOWN_ARROW, -Keycode.DOWN_ARROW, 0.5, Keycode.ENTER, -Keycode.ENTER, 0.5, 'LDAPpass\n']),
        (0x000040, 'Oracle', ['OracleID', Keycode.TAB,
                           'OraclePASS\n']),
        (0x101010, 'Kronos', ['KronosID', Keycode.TAB,
                           'KronosPASS\n']),
        # 2nd row ----------
        (0x400000, 'ID', ['EID']),
        (0x000040, 'ID', ['OracleID']),
        (0x101010, 'ID', ['KronosID']),
        # 3rd row ----------
        (0x400000, 'Pass', ['LDAPpass']),
        (0x000040, 'Pass', ['OraclePASS\n']),
        (0x101010, 'Pass', ['KronosPASS\n']),
        # 4th row ----------
        (0x400000, 'Lock', [Keycode.DOWN_ARROW, -Keycode.DOWN_ARROW, 0.5, 'LDAPpass\n']),
        (0x002000, 'Find', [Keycode.ALT, -Keycode.ALT, Keycode.RIGHT_ARROW, -Keycode.RIGHT_ARROW, Keycode.RIGHT_ARROW, -Keycode.RIGHT_ARROW, Keycode.DOWN_ARROW, -Keycode.DOWN_ARROW, Keycode.DOWN_ARROW, -Keycode.DOWN_ARROW, Keycode.DOWN_ARROW, -Keycode.DOWN_ARROW, Keycode.ENTER]),
        (0x202000, 'VPN', ['VPNpass', Keycode.ENTER]),
        # Encoder button ---
        (0x000000, '', [Keycode.WINDOWS, 'l']) # Lock Computer
    ]
}
