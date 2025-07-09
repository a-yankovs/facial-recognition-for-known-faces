# File containing camera functions.
import cv2 

# Function which initialises camera and sets its resolution and FPS (frames per second).
# Returns: 
#   cam: A new video capture object.
def camera_init():
    # Initialise camera object. 
    cam = cv2.VideoCapture(0) 
    if not cam.isOpened():
        print("Error: Could not initialize camera.")
        return None
    print("Camera initialized successfully.")

    # Reduced resolution to help speed up program (Default resolution was 1280 x 720).
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640) 
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cam.set(cv2.CAP_PROP_FPS, 30)
    return cam

# Contiuously captures the current frame of the camera.
# Parameters: 
#   cam: A video capture object.  
# Returns: 
#   frame: The captured frame.
def capture_frame(cam):

    # captured - boolean: returns whether the frame was captured successfully
    # frame - npy array: the camptured frame itself 
    captured, frame = cam.read()
    if not captured:
        print("Error: Unable to capture frame.")
        return None
    # print("Frame captured!")  
    return frame
