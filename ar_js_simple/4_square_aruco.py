import cv2
import numpy as np
# Add this import statement
from cv2 import aruco

print(cv2.__version__)

def create_test_pattern():
    # Create a white background (1300x1300 pixels for 13cm at 100dpi)
    pattern = np.ones((1300, 1300), dtype=np.uint8) * 255
    
    # Create ArUco dictionary
    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
    
    # Marker size (300 pixels = 3cm at 100dpi)
    marker_size = 300
    
    # Generate and place markers
    positions = [
        (350, 350),   # Marker 0 - Top Left
        (950, 350),   # Marker 1 - Top Right
        (350, 950),   # Marker 2 - Bottom Left
        (950, 950)    # Marker 3 - Bottom Right
    ]
    
    for i, pos in enumerate(positions):
        marker = np.zeros((marker_size, marker_size), dtype=np.uint8)
        marker = cv2.aruco.generateImageMarker(aruco_dict, i, marker_size)
        x, y = pos
        pattern[y-marker_size//2:y+marker_size//2, 
                x-marker_size//2:x+marker_size//2] = marker
    
    # Add marker IDs
    font = cv2.FONT_HERSHEY_SIMPLEX
    # cv2.putText(pattern, "ID: 0", (300, 300), font, 1, 0, 2)
    # cv2.putText(pattern, "ID: 1", (900, 300), font, 1, 0, 2)
    # cv2.putText(pattern, "ID: 2", (300, 900), font, 1, 0, 2)
    # cv2.putText(pattern, "ID: 3", (900, 900), font, 1, 0, 2)
    
    return pattern

# Generate and save the pattern
pattern = create_test_pattern()
cv2.imwrite('test_pattern.png', pattern)