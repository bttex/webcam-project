import cv2
import time

from camera import start_camera
from hand_detector import HandDetector
from gesture_detector import GestureDetector
from gesture_classifier import GestureClassifier
from gesture_stabilizer import GestureStabilizer
from gesture_controller import GestureController


cap = start_camera()

hand_detector = HandDetector("hand_landmarker.task")
gesture_detector = GestureDetector()

gesture_classifier = GestureClassifier()
gesture_stabilizer = GestureStabilizer(window_size=5)
gesture_controller = GestureController()


while True:
    ret, frame = cap.read()

    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    timestamp = int(time.time() * 1000)

    result = hand_detector.detect(rgb, timestamp)

    if result.hand_landmarks:
        for hand_landmarks in result.hand_landmarks:
            # estados dos dedos
            fingers = gesture_detector.get_finger_states(hand_landmarks)

            # classifica gesto
            gesture = gesture_classifier.classify(fingers, hand_landmarks)

            # estabiliza
            stable_gesture = gesture_stabilizer.update(gesture)

            if stable_gesture:
                # executa ação
                action = gesture_controller.handle(stable_gesture)
                if action == "EXIT":
                    break

                # mostra na tela
                cv2.putText(
                    frame,
                    stable_gesture,
                    (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2,
                )

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == 27:
        break


cap.release()
cv2.destroyAllWindows()
