# Edge Detection

## Overview
Edge detection is a technique used in image processing to identify the boundaries of objects within an image. By detecting discontinuities in brightness, it highlights significant changes in intensity, which correspond to object edges. This is a critical step in tasks like object detection, image segmentation, and feature extraction.

## How It Works
Edge detection works by analyzing the intensity gradients in an image. Gradients are changes in brightness from one pixel to another. Sharp changes, or high gradients, indicate the presence of an edge.

Several edge detection techniques are commonly used, each with different approaches to identifying edges:

### 1. Sobel Operator
The Sobel operator calculates the gradient of the image intensity in both the x (horizontal) and y (vertical) directions. It uses convolution with two 3x3 kernels to detect edges in these directions. The Sobel operator emphasizes edges where the change in intensity is greatest.

The Sobel kernels are defined as:

- **Horizontal kernel**: 
$$
\begin{bmatrix}
-1 & 0 & 1 \\
-2 & 0 & 2 \\
-1 & 0 & 1
\end{bmatrix}
$$

- **Vertical kernel**:
$$
\begin{bmatrix}
-1 & -2 & -1 \\
0 & 0 & 0 \\
1 & 2 & 1
\end{bmatrix}
$$

#### Steps Involved:
1. **Gradient Calculation**: The image is convolved with the horizontal and vertical Sobel kernels to obtain two gradient images, one for each direction.
   
2. **Magnitude Computation**: The gradient magnitudes are combined to compute the overall strength of the edge at each pixel:
   $$
   G = \sqrt{G_x^2 + G_y^2}
   $$
   
3. **Direction**: The direction of the edge can be computed as:
   $$
   \theta = \tan^{-1}\left(\frac{G_y}{G_x}\right)
   $$

#### Applications:
- **Edge Detection**: The Sobel operator is used to detect edges along both axes and is widely used in image processing applications.
  
### 2. Canny Edge Detection
The Canny Edge Detector is a multi-step algorithm designed to detect a wide range of edges in images. It is considered one of the best edge detection methods due to its ability to detect strong edges while reducing noise.

#### Steps Involved:
1. **Noise Reduction**: The image is first smoothed using a Gaussian filter to reduce noise and avoid detecting false edges.
   
2. **Gradient Calculation**: Sobel filters are applied to compute the gradient magnitude and direction.
   
3. **Non-Maximum Suppression**: Thin out the edges by suppressing any pixel that is not a local maximum along the gradient direction.
   
4. **Double Thresholding**: Apply two thresholds to categorize edges as strong, weak, or non-edges. Strong edges are retained, weak edges are retained only if they are connected to strong edges, and non-edges are discarded.
   
5. **Edge Tracking by Hysteresis**: Weak edges connected to strong edges are considered part of the object, while others are discarded.

#### Applications:
- **Edge Detection for Object Recognition**: Canny is widely used in advanced vision systems to detect object boundaries.
  
## Applications of Edge Detection
- **Feature Detection**: Used to detect important features such as lines, corners, and contours in images.
- **Image Segmentation**: Helps in segmenting an image into different regions by highlighting object boundaries.
- **Object Recognition**: Detects the edges of objects for recognition tasks in computer vision applications.
- **Medical Imaging**: Used to detect structures like blood vessels and tumors in medical scans.

## Example Code
Here’s an example of applying both Sobel and Canny edge detection using OpenCV in Python:

```python
import cv2

# Load the image
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Sobel Edge Detection
# Apply Sobel operator in X and Y direction
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# Combine X and Y gradients
sobel_combined = cv2.addWeighted(cv2.convertScaleAbs(sobel_x), 0.5, cv2.convertScaleAbs(sobel_y), 0.5, 0)

# Canny Edge Detection
canny_edges = cv2.Canny(image, 50, 150)

# Display the results
cv2.imshow('Original Image', image)
cv2.imshow('Sobel Edge Detection', sobel_combined)
cv2.imshow('Canny Edge Detection', canny_edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
