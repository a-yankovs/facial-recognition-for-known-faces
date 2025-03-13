import cv2
import face_recognition
import os 

def load_known_faces_from_folder(directory_path = "known_faces_folder"):
    known_faces = []
    known_face_names = []

    for filename in os.listdir(directory_path):
        if filename.endswith(".jpg"): 
            image_path = os.path.join(directory_path, filename)
            known_face = face_recognition.load_image_file(image_path)
            # 128D feature vector extracted from the face 
            known_encoding = face_recognition.face_encodings(known_face)
        
            if known_encoding:  # If faces are found in the image
                known_faces.append(known_encoding[0])
                 # Use the filename as the name to store in 
                known_face_names.append(filename.split(".")[0]) 

    return known_faces, known_face_names


def detect_faces(frame): 
    # converts to grayscale - easier to process for Haar Cascades 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # load the pre-trained model 
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # faces: contained the boundign boxes for each face 
    # scaleFactor: scales the image so that image that might be smaller or bigger bc of distance and resolution 
    # tries dteetcing the face at different scales. used 1.2 because it's faster, but scales images by a larger percentage at each scale  
    # minNeighbors: the minimum number of chose 7 as it reduces the number of false positives - accuracy is important 
    # minSize: smallest face size that is detected in pixels - helps reduce noise - helps improve speed of detection
    faces =  face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 7, minSize = (30, 30))

    return faces

def recognise_faces(frame, known_faces, face_locations, known_face_names): 
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    names = []
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_faces, face_encoding)
        name = "Unknown"

        if True in matches:
            index = matches.index(True)
            name = known_face_names[index]

        names.append(name)
    
    return names

def save_new_face(frame, face_location, name, directory_path = "known_faces"):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    top, right, bottom, left = face_location
    face_image = frame[top:bottom, left:right]
    face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)

    file_path = os.path.join(directory_path, f"{name}.jpg")
    cv2.imwrite(file_path, face_image)
    print(f"New face saved as {file_path}")
