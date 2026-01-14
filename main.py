# main.py
import cv2
from cvzone.HandTrackingModule import HandDetector

from core.keyboard_ui import build_button_list, draw_all, DEFAULT_KEYS
from core.gesture_logic import update_hover_and_click, GestureConfig
from core.key_emitter import VirtualKeyboardEmitter


def main():
    # Camera setup
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)

    detector = HandDetector(detectionCon=0.8)

    # UI layout
    button_list = build_button_list(DEFAULT_KEYS)

    # Gesture config (감도 조절은 여기서)
    gesture_cfg = GestureConfig(
        click_distance_thresh=30,  # 기존 코드의 l < 30
        debounce_sec=0.15          # 기존 sleep(0.15)
    )

    # Key event emitterZVVVVBNNNNNNHHHHHH
    emitter = VirtualKeyboardEmitter()

    while True:
        success, img = cap.read()
        if not success:
            continue

        hands, img = detector.findHands(img)
        lm_list = None
        if hands:
            lm_list = hands[0]["lmList"]  # 21 landmarks

        # Draw UI
        img = draw_all(img, button_list)

        # Hover/Click update
        hovered_btn, clicked_btn = update_hover_and_click(
            img=img,
            lm_list=lm_list,
            button_list=button_list,
            detector=detector,
            cfg=gesture_cfg
        )

        # TODO: Emit key event when clicked

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
