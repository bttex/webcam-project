import cv2


def start_camera(index=0):
    cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)

    if not cap.isOpened():
        raise RuntimeError("Não foi possível acessar a webcam")

    return cap
