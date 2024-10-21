import cv2

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

    # Naloga 2

    # Grayscale image
    grayFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #cv2.imshow("Grayscale",grayFrame)

    # High contrast
    HCGrayFrame = cv2.equalizeHist(grayFrame)
    cv2.imshow("High contrast grayscale",HCGrayFrame)

    # Filters
    # Gaussian Blur
    GBGrayFrame = cv2.GaussianBlur(HCGrayFrame,(5,5),cv2.BORDER_DEFAULT) 
    #cv2.imshow("Gaussian Blur",GBGrayFrame)
    # Bilateral Filter
    BFGrayFrame = cv2.bilateralFilter(HCGrayFrame, 9, 75, 75)
    #cv2.imshow("Bilateral Filter",BFGrayFrame)

    # Edge detection
    # Sobel
    Image = HCGrayFrame
    grad_x = cv2.Sobel(Image, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(Image, cv2.CV_64F, 0, 1, ksize=3)

    abs_grad_x = cv2.convertScaleAbs(grad_x)
    abs_grad_y = cv2.convertScaleAbs(grad_y)

    grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    cv2.imshow('Sobel Image',grad)

    # Canny
    CannyFrame = cv2.Canny(HCGrayFrame, 50, 80)
    cv2.imshow("Canny Image",CannyFrame)

    # Thresholding
    ret, thresholdFrame = cv2.threshold(HCGrayFrame, 120, 255, cv2.THRESH_BINARY)
    cv2.imshow("Thresholding",thresholdFrame)



    # Exit the loop when user presses any key
    if cv2.waitKey(1) != -1:
        break

# Release the camera and close all active windows before exiting the program
capture.release()
cv2.destroyAllWindows()