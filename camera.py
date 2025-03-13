import cv2 

# Function which initialises camera and sets its resolution and fps
# Returns the new camera object 
def camera_init():
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Error: Could not initialize camera.")
        return None
    print("Camera initialized successfully.")
    # reduced resolution to help speed up program 
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640) 
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    cam.set(cv2.CAP_PROP_FPS, 30)
    return cam

# Contiuously captures the current frame of the camera  
# Returns the captured frame 
def capture_frame(cam):
    # ret - boolean - whether the frame was captured successfully 
    # frame - the camptured frame itself - npy array 
    ret, frame = cam.read()
    if not ret:
        print("Error: Unable to capture frame.")
        return None
    # print("Captured a frame.")  # Debugging line
    return frame
