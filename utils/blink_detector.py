# EAR calculation, blink logic
import numpy as np
from config import LEFT_EYE_LANDMARKS, RIGHT_EYE_LANDMARKS, EAR_THRESHOLD, EAR_CONSEC_FRAMES

class BlinkDetector:
    def __init__(self):
        self.frame_counter = 0
        self.drowsy = False

    def calculate_ear(self, eye_landmarks):
        A = np.linalg.norm(eye_landmarks[1] - eye_landmarks[5])
        B = np.linalg.norm(eye_landmarks[2] - eye_landmarks[4])
        C = np.linalg.norm(eye_landmarks[0] - eye_landmarks[3])
        ear = (A + B) / (2.0 * C)
        return ear

    def extract_eye_landmarks(self, face_landmarks, image_shape):
        h, w, _ = image_shape
        left_eye = np.array([
            [face_landmarks.landmark[i].x * w, face_landmarks.landmark[i].y * h]
            for i in LEFT_EYE_LANDMARKS
        ])
        right_eye = np.array([
            [face_landmarks.landmark[i].x * w, face_landmarks.landmark[i].y * h]
            for i in RIGHT_EYE_LANDMARKS
        ])
        return left_eye, right_eye

    def detect_blink(self, face_landmarks, image_shape):
        left_eye, right_eye = self.extract_eye_landmarks(face_landmarks, image_shape)
        left_ear = self.calculate_ear(left_eye)
        right_ear = self.calculate_ear(right_eye)
        avg_ear = (left_ear + right_ear) / 2.0

        if avg_ear < EAR_THRESHOLD:
            self.frame_counter += 1
        else:
            self.frame_counter = 0
            self.drowsy = False

        if self.frame_counter >= EAR_CONSEC_FRAMES:
            self.drowsy = True

        return avg_ear, self.drowsy
