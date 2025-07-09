# File containing face recognition and loading from known_faces folder.   
import cv2
import face_recognition 
import os # Module used for interacting with laptop's operating system. 

# Function which loads and encodes the known faces from the known_faces folder.
# Parameters:
#   Path to the folder containing the known faces. Default = "known_faces_folder".
# Returns: 
#   known_faces: A list of Numpy arrays containign face encodings for each person in the known faces folder. 
#   known_face_names: A list of corresponding names extracted from the image filenames. 
def load_known_faces_from_folder(directory_path = "known_faces_folder"):
    known_faces = []
    known_face_names = []

    
    for filename in os.listdir(directory_path):
        if filename.endswith(".jpg"): 
            image_path = os.path.join(directory_path, filename)
            known_face = face_recognition.load_image_file(image_path)
            
            # Creates a 128D feature vector extracted from the face. 
            known_encoding = face_recognition.face_encodings(known_face)

            # If faces are found in the image
            if known_encoding: 
                known_faces.append(known_encoding[0])
                 # Extract the recognized face's name from the file name.
                known_face_names.append(filename.split(".")[0]) 

    return known_faces, known_face_names

# Function which detects faces in each frame of a video using Haar Cascade classifier.
# Parameters: 
#   frame: A single BGR image.
# Returns: 
#   faces: A list of bounding boxes (starting_x, starting_y, width, height) for each detected face. 
def detect_faces(frame): 
    # Convert image to grayscale - easier to process for Haar Cascades.  
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Load the pre-trained model. 
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Detect rectanglular regions that might contain faces in the grey-scaled image, then filter them to 
    # accurately determine whether it is a face.  
    faces =  face_cascade.detectMultiScale(
        gray, 
        scaleFactor = 1.1,  # scaleFactor: how much the image is reduced at each scale.
        minNeighbors = 7,   # minNeighbors: the minimum number of neighboring rectangles with face detected.
                            # I chose 7 as it reduces the number of false positives.
        minSize = (30, 30)) # minSize: smallest face size that is detected in pixels.

    return faces

# Function which recognises faces in a single frame using face encodings.
# Parameters:
#   frame: An BGR image (a frame from the video from the webcam). 
#   known_faces: List of face encodings for known faces. 
#   face_locations: List of face locations in the frame (used to reduce computation).
#   known_face_names: List of names corresponding to known_faces.
# Returns: 
#    names: A list of names which have been recognised - implemented to be used in the future. 
def recognise_faces(frame, known_faces, face_locations, known_face_names): 
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    names = []
    # compares 128 - dimensional vectors in face_encodings in known_faces
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_faces, face_encoding)
        name = "Unknown"
        if True in matches:
            index = matches.index(True)
            name = known_face_names[index]

        names.append(name)
    return names

# Function which saves a previously-unrecognised face into the knonw_faces folder.
# Parameters:
#   frame: An BGR image (a frame from the video from the webcam). 
#   face_location: Tuple of face bounding box coordinates (top, right, bottom, left).
#   name: String label to assign to the saved face image.
#   directory_path: Path to the directory where known faces are stored. 
def save_new_face(frame, face_location, name, directory_path = "known_faces"):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    # Extract the face region from the frame using the given coordinates.
    top, right, bottom, left = face_location
    face_image = frame[top:bottom, left:right]

    # Converts image to RGB for easier processing in the future. 
    face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)

    file_path = os.path.join(directory_path, f"{name}.jpg")
    cv2.imwrite(file_path, face_image)
    print(f"New face saved as {file_path}")
