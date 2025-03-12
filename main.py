import cv2
import face_recognition


cam = cv2.VideoCapture(0)

if not cap.isOpened(): 
    print("Camera is not found!")
    break

known_image = face_recognition.load_image_file("known_person.jpg")
# 128D feature vector extracted from the face 
known_encoding = face_recognition.face_encodings(known_image)[0]

# storing the econding of the face in a list with labels for each person
known_faces = [known_encoding]
known_face_names = ["Sasha"]

# ret - boolean - whether the frame was captured successfully 
# frame - the camptured frame itself - npy array 
while True: 
    ret, frame = cam.read()
    if not ret: 
        print("Frame not caputed :(")
        break 

# converts to grayscale - easier to process for Haar Cascades 
gray = cv2.cvtColor(frame, cv2, COLOR_BGR2GRAY)

# load the pre-trained model 
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# faces: contained the boundign boxes for each face 
# scaleFactor: scales the image so that image that might be smaller or bigger bc of distance and resolution 
# tries dteetcing the face at different scales. used 1.2 because it's faster, but scales images by a larger percentage at each scale  
# minNeighbors: the minimum number of chose 7 as it reduces the number of false positives - accuracy is important 
# minSize: smallest face size that is detected in pixels - helps reduce noise - helps improve speed of detection
faces =  face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 7, minSize = (30, 30))

# returns a list of all faces in the image, and then computes 128D encoding for each face
face_locations = face_recognition.face_locations(frame)
face_encodings = face_recognition.face_encodings(frame, face_locations)

# top, right, bottom, left - coordinates of the bounds of the bouding box 
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_faces, face_encodings
    name = "Unknown"

    if True in matches:
        index = matches.index(True)
        name = known_face_names[first_match_index]

# draw the bounding box and add the label
cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
cv2.putText(frame, name, right - 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, font_size = 0.5, text_color = (255, 255, 255), font_thickness = 1)

cv2.imshow('Face Recognition', frame)

# 1 : how long to wait for key press. if q key is pressed, we exit 
if cv2.waitKey(1) & OxFF == ord('q')
    break

cam.release() 
cv2.destoyAllWindows()




