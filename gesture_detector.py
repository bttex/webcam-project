class GestureDetector:
    def get_finger_states(self, landmarks):

        fingers = []

        # polegar
        fingers.append(1 if landmarks[4].x > landmarks[3].x else 0)

        # indicador
        fingers.append(1 if landmarks[8].y < landmarks[6].y else 0)

        # médio
        fingers.append(1 if landmarks[12].y < landmarks[10].y else 0)

        # anelar
        fingers.append(1 if landmarks[16].y < landmarks[14].y else 0)

        # mindinho
        fingers.append(1 if landmarks[20].y < landmarks[18].y else 0)

        return fingers
