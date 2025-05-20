# Entry point: runs the app
from utils.video_utils import get_video_capture
from utils.mediapipe_utils import initialize_face_mesh, detect_face_landmarks, draw_landmarks
from utils.blink_detector import BlinkDetector
from utils.head_pose import HeadPoseEstimator
from alarms.alarm import start_alarm, stop_alarm    
import cv2

def main():
    cap = cv2.VideoCapture(0)

    blink_counter = 0
    nod_counter = 0

    BLINK_THRESHOLD = 15  # tweak this
    NOD_THRESHOLD = 15    # tweak this

    face_mesh = initialize_face_mesh()
    blink_detector = BlinkDetector()
    


    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Cannot read from webcam.")
            return

        head_pose_estimator = HeadPoseEstimator(frame.shape)

         # Get results and RGB frame from detection
        results, frame_rgb = detect_face_landmarks(frame, face_mesh)

        if results.multi_face_landmarks:
            # This is the actual list of landmarks
            draw_landmarks(frame, results.multi_face_landmarks)

            # 👁 Blink Detection
            for face_landmarks in results.multi_face_landmarks:
                ear, is_drowsy = blink_detector.detect_blink(face_landmarks, frame.shape)

                # Visual feedback
                cv2.putText(frame, f"EAR: {ear:.2f}", (30, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                if is_drowsy:
                    blink_counter += 1
                    cv2.putText(frame, "DROWSY: Eyes Closed", (30, 60),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
                else:
                    blink_counter = max(blink_counter - 1, 0)  # decay counter gradually

            # Nodding Detection
            # Estimate head pose
            pose = head_pose_estimator.get_head_pose(face_landmarks.landmark, frame.shape)
            if pose:
                pitch, yaw, roll = pose
                cv2.putText(frame, f"Pitch: {pitch:.2f}", (30, 90),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)

                # Simple drowsiness rule: if pitch is nodding down too much
                if pitch > 15:  # adjust this threshold after testing
                    nod_counter += 1
                    cv2.putText(frame, "DROWSY: Nodding", (30, 120),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)

            if blink_counter >= BLINK_THRESHOLD or nod_counter >= NOD_THRESHOLD:
                print("[ALERT] Drowsiness Detected!")
                start_alarm()
            else:
                stop_alarm()


        cv2.imshow("Drowsiness Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    face_mesh.close()

if __name__ == "__main__":
    main()
