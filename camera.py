
import cv2 
    
def camera_init():
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Error: Could not initialize camera.")
        return None
    print("Camera initialized successfully.")
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Reduce resolution to speed up
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

     # Set FPS to a higher value (e.g., 30 FPS)
    cam.set(cv2.CAP_PROP_FPS, 30)  # Or another camera index if needed  # Debugging line
    return cam

# ret - boolean - whether the frame was captured successfully 
# frame - the camptured frame itself - npy array 
def capture_frame(cam):
    ret, frame = cam.read()
    if not ret:
        print("Error: Unable to capture frame.")
        return None
    # print("Captured a frame.")  # Debugging line
    return frame