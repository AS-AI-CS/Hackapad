import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC

keyboard = KMKKeyboard()

keyboard.row_pins = (board.D2, board.D3, board.D4, board.D6)
keyboard.col_pins = ()
keyboard.diode_orientation = DiodeOrientation.COL2ROW


keyboard.keymap = [
    [
        KC.LCTL(KC.LGUI(KC.Q)),
        KC.LGUI(KC.LSFT(KC.Q)), 
        KC.LGUI(KC.C),
        KC.LGUI(KC.V),
    ]
]

if __name__ == '__main__':
    keyboard.go()
