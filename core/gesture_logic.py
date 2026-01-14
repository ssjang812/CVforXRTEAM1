# gesture_logic.py
from dataclasses import dataclass
import time
import cv2


class GestureState:
    def __init__(self):
        self.last_click_time = 0.0


_state = GestureState()


def _point_in_button(px, py, button):
    x, y = button.pos
    w, h = button.size
    return (x < px < x + w) and (y < py < y + h)


def update_hover_and_click(img, lm_list, button_list, detector):
    """
    returns: (hovered_button, clicked_button)
    """
    hovered = None
    clicked = None

    if not lm_list:
        return hovered, clicked

    # fingertip indices: index=8, middle=12
    ix, iy = lm_list[8][0], lm_list[8][1]

    for button in button_list:
        if _point_in_button(ix, iy, button):
            hovered = button

            # Hover highlight
            x, y = button.pos
            w, h = button.size
            cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5),
                          (175, 0, 175), cv2.FILLED)
            cv2.putText(img, button.text, (x + 10, y + 45),
                        cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)

            # Click detection by distance between tips (8 and 12)
            dist, _, _ = detector.findDistance(lm_list[8][0:2], lm_list[12][0:2])

            now = time.time()
            can_click = (now - _state.last_click_time) >= 0.15

            if can_click and dist < 30:
                clicked = button
                _state.last_click_time = now

                # Click highlight
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, button.text, (x + 10, y + 45),
                            cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)

            break  # 한 프레임에 하나의 버튼만 처리

    return hovered, clicked
