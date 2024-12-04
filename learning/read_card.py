import cv2
import numpy as np

# Load the image
image = cv2.imread("business_card_markers.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect ArUco markers
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
parameters = cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)

corners, ids, rejected = detector.detectMarkers(gray)

# Print detected marker IDs
if ids is not None:
    print("Detected marker IDs:", ids.flatten())
    # Print positions
    for i, corner in enumerate(corners):
        print(f"Marker {ids[i][0]} position: {corner[0]}")
else:
    print("No markers detected")