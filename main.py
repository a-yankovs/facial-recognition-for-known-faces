# Main file of this project - runs the face detector program. 
import cv2
import face_recognition
from camera import camera_init, capture_frame 
from face_recognition_model import load_known_faces_from_folder, detect_faces, recognise_faces, save_new_face
import time 
# import threading

recognized_faces = []

# Function which runs facial recognition, using methods from camera and face_recognition_model.
# Initialize the camera, load known faces, detect faces in each frame,
# and update the known face database if unknown individuals are detected. 
def run_facial_recognition():
    cam = camera_init()
    known_faces, known_face_names = load_known_faces_from_folder("known_faces")

    while True:
        frame = capture_frame(cam)
        if frame is None:
            break
            
        # Find where each face is in the frame (find its coordinates). 
        face_locations = face_recognition.face_locations(frame) 
        
        #  Use the known faces to find known faces in the frame.   
        names = recognise_faces(frame, known_faces, face_locations, known_face_names)
        
        # Draw bounding rectangle around each face detected in the video. 
        for (top, right, bottom, left), name in zip(face_locations, names):
            if name not in recognized_faces: 
                print(name + " recognised! \n" )
                recognized_faces.append(name)
                
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.putText(frame, name, (right - 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

            # Handle unknown faces by saving them with timestamps. 
            if name == "Unknown": 
                print("Uh-oh! Unknown face detected!\n")
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                save_new_face(frame, (top, right, bottom, left), timestamp, directory_path = "known_faces")
                known_faces, known_face_names = load_known_faces_from_folder("known_faces")
                print("No worries, though! We saved the new face as time that it was first detected!")
        
        cv2.imshow('Face Recognition', frame)

        # If the "q" key is pressed, exit the program.  
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_facial_recognition()
