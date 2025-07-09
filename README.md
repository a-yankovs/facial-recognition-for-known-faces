
# Facial Recognition for Known Faces using OpenCV's Haar Cascades Model

## Key Features 
This is a quick mini-project that captures faces using the built-in computer camera, recognizes faces from a folder of saved faces, and labels new faces, using OpenCv's 'Haar Cascades' model.

### Process
- I accessed my computer's camera, and used it to recognise the location of each face in a frame. 
- Then, using the folder of known faces, I labelled each face in the frame:  
     - If it was a known face, I labelled it with the name the corresponding photo had in the known_faces folder. 
     - If it was an unknown face (not previously captured), I labelled it with the time the face was first detected (in year-month-day hour-minute-second format). 

### Project Demo
When it's just me in the frame:  

Camera view: my name (Alexandra) and the bounding box around my face.
          <img width="692" alt="Screenshot 2025-03-12 at 22 26 42" src="https://github.com/user-attachments/assets/0cd8ff42-b8c8-4544-b2fd-df5bb0d02e91" />

Terminal output:  
          <img width="1125" alt="Screenshot 2025-03-12 at 22 34 18" src="https://github.com/user-attachments/assets/b6f326bd-36cb-4a0f-98c1-325baaebdbc5" />

When it's me and an unknown face (Leonardo DiCaprio) in the frame:  

Camera view: my name (Alexandra), and the time the known name was recognised, and bounding boxes for both faces.  
          <img width="641" alt="Screenshot 2025-03-12 at 22 49 10" src="https://github.com/user-attachments/assets/29aefd38-b219-43d1-a39d-74efb77db177" />

Terminal output:  
          <img width="979" alt="Screenshot 2025-03-12 at 22 49 53" src="https://github.com/user-attachments/assets/7cc44da2-fdb2-4a5b-b466-7190036f2d9d" />

## Software Architechture
### `main.py`
- Runs facial recognition, using functions from `camera.py` and `face_recognition_model.py`.
### `known_faces/` 
- Folder storing all recorded faces, in .jpg format.
### `camera.py` 
- Intialises camera, sets its resulution and FPS.
- Continuously captures the current frame of the camera.
- Returns the captured frame.
### `face_recognition_model.py`
- Loads the previously-detected faces from known_faces folder.
- Detects face in each frame.
- Loads the Haar Cascades model.
- Saves new (unknown) faces into the known_faces folder.
