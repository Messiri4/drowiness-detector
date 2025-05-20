# Face mesh & landmark detection
import mediapipe as mp
import cv2

mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
mp_style = mp.solutions.drawing_styles

def initialize_face_mesh():
    return mp_face_mesh.FaceMesh(
        max_num_faces=1,
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    )

def detect_face_landmarks(frame, face_mesh):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(frame_rgb)
    return results, frame_rgb

def draw_landmarks(frame, landmarks):
    for face_landmarks in landmarks:
        mp_drawing.draw_landmarks(
            image=frame,
            landmark_list=face_landmarks,
            connections=mp_face_mesh.FACEMESH_TESSELATION,
            landmark_drawing_spec=None,
            connection_drawing_spec=mp_style.get_default_face_mesh_tesselation_style()
        )
