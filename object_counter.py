import cv2

# Load the image
image = cv2.imread("objects.jpeg")
image = cv2.resize(image, (600, 600))  # Optional: resize for consistency

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply binary thresholding
_, thresh = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV)

# Find contours (external objects only)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours and count them
object_count = len(contours)
for contour in contours:
    cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)

# Put text showing count
cv2.putText(image, f'Total Objects: {object_count}', (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Display result
cv2.imshow("Detected Objects", image)
cv2.waitKey(0)
cv2.destroyAllWindows()