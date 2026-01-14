# key_emitter.py
from pynput.keyboard import Controller, Key


class VirtualKeyboardEmitter:
    def __init__(self):
        self.keyboard = Controller()
        self.final_text = ""

    def emit(self, key_text: str):
        """
        key_text: 버튼에 적힌 문자열 (예: 'A', 'BS', ';' 등)
        """
        if key_text == "BS":
            self.keyboard.press(Key.backspace)
            self.keyboard.release(Key.backspace)
            self.final_text = self.final_text[:-1]
        else:
            # 일반 문자 키
            self.keyboard.press(key_text)
            self.keyboard.release(key_text)
            self.final_text += key_text
