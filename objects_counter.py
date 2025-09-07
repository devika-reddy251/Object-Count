import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread("objects.jpeg")
image = cv2.resize(image, (600, 600))  # Optional: Resize

# Keep a copy of the original image for display
original_image = image.copy()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Blur to remove noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Threshold to create binary image
_, thresh = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
object_count = len(contours)

# Draw contours on the image
for contour in contours:
    cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)

# Convert BGR to RGB for matplotlib display
original_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
detected_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Create a plot with original and processed image + bar chart
plt.figure(figsize=(12, 6))

# Show original image
plt.subplot(1, 3, 1)
plt.imshow(original_rgb)
plt.title("Original Image")
plt.axis("off")

# Show image with detected objects
plt.subplot(1, 3, 2)
plt.imshow(detected_rgb)
plt.title("Detected Objects")
plt.axis("off")

# Bar graph for object count
plt.subplot(1, 3, 3)
plt.bar(["Objects Detected"], [object_count], color='orange')
plt.title("Object Count")
plt.ylabel("Count")

plt.tight_layout()
plt.show()