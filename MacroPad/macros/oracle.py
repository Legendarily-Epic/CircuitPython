# MACROPAD Hotkeys example: Oracle

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                       # REQUIRED dict, must be named 'app'
    'name' : 'Oracle', # Application name
    'macros' : [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x400000, 'Login', ['oracleID', Keycode.TAB, 'oraclePass\n']),
        (0x400000, 'Re-Log', ['oraclePass\n', 1.0, Keycode.ALT, Keycode.TAB, -Keycode.ALT, -Keycode.TAB,
                            0.5, Keycode.ENTER, -Keycode.ENTER]),
        (0x400000, 'Pass', ['oraclePass\n']),
        # 2nd row ----------
        (0x000040, 'OnHand',[Keycode.TAB, -Keycode.TAB, Keycode.TAB, -Keycode.TAB, Keycode.TAB,
                            -Keycode.TAB, Keycode.TAB, -Keycode.TAB, Keycode.TAB, -Keycode.TAB,
                            '1', Keycode.TAB, -Keycode.TAB, '999999\n', 5.0, Keycode.ALT, -Keycode.ALT,
                            Keycode.DOWN_ARROW, -Keycode.DOWN_ARROW, Keycode.DOWN_ARROW, -Keycode.DOWN_ARROW,
                            Keycode.DOWN_ARROW, -Keycode.DOWN_ARROW, Keycode.DOWN_ARROW, -Keycode.DOWN_ARROW,
                            Keycode.DOWN_ARROW, -Keycode.DOWN_ARROW, Keycode.DOWN_ARROW, -Keycode.DOWN_ARROW,
                            Keycode.ENTER, -Keycode.ENTER, 8.0, Keycode.TAB, -Keycode.TAB, Keycode.TAB,
                            -Keycode.TAB, 0.5, Keycode.ENTER]),
        (0x002000, 'Qry', [Keycode.F11, -Keycode.F11]),
        (0x002000, 'X_Qry', [Keycode.CONTROL, Keycode.F11, -Keycode.CONTROL, -Keycode.F11]),
        # 3rd row ----------
        (0x000000, '', []),
        (0x002000, 'V_Req', [Keycode.ALT, -Keycode.ALT, Keycode.RIGHT_ARROW,
                            -Keycode.RIGHT_ARROW, Keycode.RIGHT_ARROW, -Keycode.RIGHT_ARROW,
                            Keycode.DOWN_ARROW, -Keycode.DOWN_ARROW, Keycode.DOWN_ARROW,
                            -Keycode.DOWN_ARROW, Keycode.DOWN_ARROW, -Keycode.DOWN_ARROW,
                            Keycode.DOWN_ARROW, -Keycode.DOWN_ARROW, Keycode.DOWN_ARROW,
                            -Keycode.DOWN_ARROW, Keycode.DOWN_ARROW, -Keycode.DOWN_ARROW,
                            Keycode.DOWN_ARROW, -Keycode.DOWN_ARROW, Keycode.DOWN_ARROW,
                            -Keycode.DOWN_ARROW, Keycode.DOWN_ARROW, -Keycode.DOWN_ARROW,
                            Keycode.DOWN_ARROW, -Keycode.DOWN_ARROW, Keycode.ENTER, -Keycode.ENTER,
                            3.0, Keycode.TAB, -Keycode.TAB, Keycode.TAB, -Keycode.TAB, Keycode.TAB,
                            -Keycode.TAB, '1', Keycode.TAB, -Keycode.TAB, Keycode.TAB,
                            -Keycode.TAB, Keycode.TAB, -Keycode.TAB, Keycode.TAB, -Keycode.TAB, Keycode.ENTER,
                            -Keycode.ENTER]),
        (0x002000, 'FIND', [Keycode.ALT, -Keycode.ALT, Keycode.RIGHT_ARROW, -Keycode.RIGHT_ARROW,
                            Keycode.RIGHT_ARROW, -Keycode.RIGHT_ARROW, Keycode.DOWN_ARROW,
                            -Keycode.DOWN_ARROW, Keycode.DOWN_ARROW, -Keycode.DOWN_ARROW,
                            Keycode.DOWN_ARROW, -Keycode.DOWN_ARROW, Keycode.ENTER]),
        # 4th row ----------
        (0x202000, 'SHPPRT', ['INT_PHX_SHIPPING3', Keycode.TAB, -Keycode.TAB]),
        (0x202000, 'CNTPRT', ['AZ0Z CONTAINER 4', Keycode.TAB, -Keycode.TAB]),
        (0x202000, 'LBLPRT', ['AZ0Z LABEL 8', Keycode.TAB, -Keycode.TAB]),
        # Encoder button ---
        (0x000000, '', [Keycode.WINDOWS, 'l']) # Lock Computer
    ]
}
