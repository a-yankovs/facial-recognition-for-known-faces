import cv2
import face_recognition
from camera import camera_init, capture_frame
from face_recognition_model import load_known_faces_from_folder, detect_faces, recognise_faces

recognized_faces = []

def run_facial_recognition():
    cam = camera_init()
    known_faces, known_face_names = load_known_faces_from_folder("known_faces")

    while True:
        frame = capture_frame(cam)
        if frame is None:
            break

        # Detect face locations using face_recognition
        face_locations = face_recognition.face_locations(frame)
        
        # Recognize faces based on known faces
        names = recognise_faces(frame, known_faces, face_locations, known_face_names)

        for (top, right, bottom, left), name in zip(face_locations, names):
            # Draw bounding box around face and add the label
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.putText(frame, name, (right - 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        cv2.imshow('Face Recognition', frame)

        # Exit when the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_facial_recognition()  # Call the correct function to start facial recognition
