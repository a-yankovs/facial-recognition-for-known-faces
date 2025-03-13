import cv2
import face_recognition
from camera import camera_init, capture_frame
from face_recognition_model import load_known_faces_from_folder, detect_faces, recognise_faces, save_new_face
import time 
# import threading

recognized_faces = []

def run_facial_recognition():
    cam = camera_init()
    known_faces, known_face_names = load_known_faces_from_folder("known_faces")

    while True:
        frame = capture_frame(cam)
        if frame is None:
            break
        #find where each face is in the frame (find its coordinates)
        face_locations = face_recognition.face_locations(frame) 
        #  use the known faces to find known faces in the frame  
        names = recognise_faces(frame, known_faces, face_locations, known_face_names)
        # draw bounding rectangle around each face detected in the video 
        for (top, right, bottom, left), name in zip(face_locations, names):
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.putText(frame, name, (right - 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            if name == "Unknown": 
                print("Uh-oh! Unknown face detected!\n")
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                save_new_face(frame, (top, right, bottom, left), timestamp, directory_path = "known_faces")
                known_faces, known_face_names = load_known_faces_from_folder("known_faces")
                print("No worries, though! We saved the new face as time that it was first detected!")
    # Multi-threading: doesn't work YET!
            # if name == "Unknown":
            #     print("Unknown face detected! Press 's' to save or any other key to continue.")
            #     key = input()
            #     if key == ord('s'):
            #        thread2 = threading.Thread(target=prompt_and_save_face, args=(frame.copy(), (top, right, bottom, left)), daemon=True)
            #        thread2.start()
            #        known_faces, known_face_names = load_known_faces_from_folder("known_faces")

        cv2.imshow('Face Recognition', frame)

        # if the "q" key is pressed, exit the program 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
# Multi-threading: function to save new face and prompt user for a name for the face 
# def prompt_and_save_face(frame, face_location):
#     new_name = input("Enter name for the new face: ").strip()
#     save_new_face(frame, face_location, new_name)
#     global known_faces, known_face_names
#     known_faces, known_face_names = load_known_faces_from_folder("known_faces")

if __name__ == "__main__":
    run_facial_recognition()
