# Head pose & nodding detection
import cv2
import numpy as np

class HeadPoseEstimator:
    def __init__(self, frame_shape):
        self.size = frame_shape  # (height, width, channels)

        # 3D model points of a generic face (nose, eyes, mouth, etc.)
        self.model_points = np.array([
            (0.0, 0.0, 0.0),             # Nose tip
            (0.0, -330.0, -65.0),        # Chin
            (-225.0, 170.0, -135.0),     # Left eye left corner
            (225.0, 170.0, -135.0),      # Right eye right corner
            (-150.0, -150.0, -125.0),    # Left mouth corner
            (150.0, -150.0, -125.0)      # Right mouth corner
        ], dtype=np.float64)

    def get_head_pose(self, landmarks, image_shape):
        h, w, _ = image_shape

        # Get 2D image points from 468 landmark array
        image_points = np.array([
            [landmarks[1].x * w, landmarks[1].y * h],    # Nose tip
            [landmarks[152].x * w, landmarks[152].y * h],# Chin
            [landmarks[263].x * w, landmarks[263].y * h],# Left eye
            [landmarks[33].x * w, landmarks[33].y * h],  # Right eye
            [landmarks[287].x * w, landmarks[287].y * h],# Left mouth corner
            [landmarks[57].x * w, landmarks[57].y * h]   # Right mouth corner
        ], dtype=np.float64)

        focal_length = w
        center = (w / 2, h / 2)
        camera_matrix = np.array([
            [focal_length, 0, center[0]],
            [0, focal_length, center[1]],
            [0, 0, 1]
        ], dtype=np.float64)

        dist_coeffs = np.zeros((4, 1))  # Assume no lens distortion

        # SolvePnP
        success, rotation_vector, translation_vector = cv2.solvePnP(
            self.model_points, image_points, camera_matrix, dist_coeffs, flags=cv2.SOLVEPNP_ITERATIVE
        )

        if not success:
            return None

        # Convert rotation vector to Euler angles
        rmat, _ = cv2.Rodrigues(rotation_vector)
        angles, _, _, _, _, _ = cv2.RQDecomp3x3(rmat)
        pitch, yaw, roll = angles  # These are in degrees

        return pitch, yaw, roll
