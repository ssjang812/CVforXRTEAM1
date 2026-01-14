# keyboard_ui.py
import cv2
import cvzone


DEFAULT_KEYS = [
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', 'BS'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', "'"],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/']
]


class Button:
    def __init__(self, pos, text, size=(60, 60)):
        self.pos = pos          # [x, y]
        self.size = size        # (w, h)
        self.text = text


def build_button_list(keys_layout, start=(50, 50), gap=70):
    """
    keys_layout: 2D list of key labels
    start: top-left offset (x0, y0)
    gap: spacing between keys
    """
    button_list = []
    x0, y0 = start

    for row_i in range(len(keys_layout)):
        for col_i, key in enumerate(keys_layout[row_i]):
            x = gap * col_i + x0
            y = gap * row_i + y0
            button_list.append(Button([x, y], key))
    return button_list

