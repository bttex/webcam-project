import math


class GestureClassifier:
    def is_pinch(self, fingers, landmarks):

        thumb = landmarks[4]
        index = landmarks[8]

        dist = math.sqrt((thumb.x - index.x) ** 2 + (thumb.y - index.y) ** 2)

        if fingers[1] == 1 and dist < 0.05:
            return True

        return False

    def classify(self, fingers, landmarks):

        if self.is_pinch(fingers, landmarks):
            return "PINCH"

        if fingers == [0, 0, 0, 0, 0]:
            return "FIST"

        if fingers == [1, 0, 0, 0, 0]:
            return "THUMBS_UP"

        if fingers == [1, 1, 0, 0, 0]:
            return "GUN"

        if fingers == [0, 1, 1, 0, 0]:
            return "PEACE"

        if fingers == [0, 1, 0, 0, 1]:
            return "ROCK"

        if fingers == [1, 1, 1, 1, 1]:
            return "OPEN_HAND"

        if fingers == [0, 0, 1, 0, 0]:
            return "MIDDLE_FINGER"

        if fingers == [1, 0, 0, 0, 1]:
            return "HANG_LOOSE"

        return "UNKNOWN"
