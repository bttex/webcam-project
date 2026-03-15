import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


class HandDetector:
    def __init__(self, model_path):

        BaseOptions = python.BaseOptions
        HandLandmarker = vision.HandLandmarker
        HandLandmarkerOptions = vision.HandLandmarkerOptions
        VisionRunningMode = vision.RunningMode

        options = HandLandmarkerOptions(
            base_options=BaseOptions(model_asset_path=model_path),
            running_mode=VisionRunningMode.VIDEO,
            num_hands=1,
        )

        self.detector = HandLandmarker.create_from_options(options)

    def detect(self, frame, timestamp):

        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)

        result = self.detector.detect_for_video(mp_image, timestamp)

        return result
