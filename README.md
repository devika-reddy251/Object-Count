# 🧠 Object Count using Digital Image Processing

This project implements object counting using digital image processing techniques. It takes an image as input and accurately counts the number of distinct objects present in the image using preprocessing, thresholding, and contour detection.

## 🖼️ Example Use Case

- Counting coins in an image
- Counting cells in microscopy images
- Counting products in automated inspection systems

## 🔍 Features

- Supports static image input
- Noise reduction and image preprocessing
- Adaptive or fixed thresholding
- Contour detection using OpenCV
- Accurate object count with visualization


## 🛠️ Technologies Used

- **Python 3**
- **OpenCV** – Image processing and object detection
- **NumPy** – Array manipulation
- (Optional) **Matplotlib** – For visualization

## 🚀 How It Works

1. **Read input image**
2. **Convert to grayscale**
3. **Apply Gaussian Blur to reduce noise**
4. **Threshold the image to segment objects**
5. **Find contours of individual objects**

file structure
├── object_counter.py
├── sample_images/
│   └── test1.jpg
├── output/
│   └── test1_output.jpg
├── README.md

6. **Count and display the number of objects**

