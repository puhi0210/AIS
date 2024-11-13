import cv2
from mtcnn import MTCNN
import copy


# Initialize the MTCNN detector
detector = MTCNN()

# Open the camera at the ID 0 
capture = cv2.VideoCapture(0)

# Check if camera is activated
if not (capture.isOpened()):
    print("Error: Could not access the camera")

# Set resolution of video frames
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("Press any key to exit...")

while(True):
    # Read current frame
    ret, frame = capture.read() # ret is a bool equal to True, when frame is read correctly

    # Display current camera frame
    cv2.imshow("Camera is live :)",frame)

    # NALOGA 2
    
    ## Convert the frame to GRAYSCALE
    # Grayscale images are easier to process and are often used in image analysis.
    grayFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale",grayFrame)

    ## Apply histogram equalization for high CONTRAST
    # This enhances the contrast of the grayscale image by spreading out the most frequent intensity values.
    HCGrayFrame = cv2.equalizeHist(grayFrame)
    cv2.imshow("High contrast grayscale",HCGrayFrame)

    ## Apply FILTERS to enhance the image

    # Gaussian Blur
    # This filter smooths the image by averaging the pixels in a defined kernel size (5x5).
    GBGrayFrame = cv2.GaussianBlur(HCGrayFrame,(5,5),cv2.BORDER_DEFAULT) 
    cv2.imshow("Gaussian Blur", GBGrayFrame)

    # Bilateral Filter
    # This filter reduces noise while preserving edges. It uses both spatial and intensity information.
    BFGrayFrame = cv2.bilateralFilter(HCGrayFrame, 9, 75, 75)
    cv2.imshow("Bilateral Filter",BFGrayFrame)

    ## EDGE DETECTION 

    # Edge detection using SOBEL operator
    Image = HCGrayFrame
    # Compute gradients in the x direction (horizontal edges)
    grad_x = cv2.Sobel(Image, cv2.CV_64F, 1, 0, ksize=3)
    # Compute gradients in the y direction (vertical edges)
    grad_y = cv2.Sobel(Image, cv2.CV_64F, 0, 1, ksize=3)

    # Convert gradients to absolute values to visualize edges
    abs_grad_x = cv2.convertScaleAbs(grad_x)
    abs_grad_y = cv2.convertScaleAbs(grad_y)

    # Combine the gradients to create a single edge image
    # The weights (0.5 each) determine the contribution of each gradient.
    grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    cv2.imshow('Sobel Image',grad)

    # CANNY edge detection
    # This algorithm detects edges by looking for areas of high gradient intensity.
    CannyFrame = cv2.Canny(HCGrayFrame, 50, 80)
    cv2.imshow("Canny Image",CannyFrame)

    ## TRASHOLDING

    # Apply TRASHOLDING to create a binary image
    # Pixels above the threshold (120) are set to white (255), and others are set to black (0).
    ret, thresholdFrame = cv2.threshold(HCGrayFrame, 120, 255, cv2.THRESH_BINARY)
    cv2.imshow("Thresholding",thresholdFrame)


    ## NALOGA 3

    # FACE DETECTION 
    
    frame_faces = copy.deepcopy(frame)
    #frame_faces = cv2.imread("/home/miha/Projects/AIS/labVaje/vaja1/data/oscar.jpg")
    grayFrame_faces = cv2.cvtColor(frame_faces,cv2.COLOR_BGR2GRAY)
    # Nalaganje prednatreniranega modela
    face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
    # haarcascade_frontalface_alt
    #face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_profileface.xml")
    # Detekcija obraza
    faces = face_cascade.detectMultiScale(
        grayFrame_faces,               # Input image (grayscale)
        scaleFactor=1.1,    # Scale factor for image reduction
        minNeighbors=5,     # Number of neighbors to retain a detectionhaarcascade_frontalface_alt
        minSize=(30, 30),   # Minimum size of face to detect (optional)
    )
    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame_faces, (x, y), (x+w, y+h), (255, 0, 255), 2)
    # Show the image with the detected faces
    cv2.imshow('Face Detection', frame_faces)
    

    ## NALOGA 4
    
    # FACE DETECTION with MTCNN

    frame_faces_mtcnn = copy.deepcopy(frame)
    #frame_faces_mtcnn = cv2.imread("/home/miha/Projects/AIS/labVaje/vaja1/data/oscar.jpg")
    # Detect faces in the frame
    faces_mtcnn = detector.detect_faces(frame_faces_mtcnn)

    # Draw bounding boxes around detected faces
    for face in faces_mtcnn:
        x, y, width, height = face['box']
        cv2.rectangle(frame_faces_mtcnn, (x, y), (x + width, y + height), (255, 0, 0), 2)

    # Display the frame with detected faces
    cv2.imshow('Real-Time Face Detection (MTCNN)', frame_faces_mtcnn)
    


    # Exit the loop when user presses any key
    if cv2.waitKey(1) != -1:
        break

# Release the camera and close all active windows before exiting the program
capture.release()
cv2.destroyAllWindows()