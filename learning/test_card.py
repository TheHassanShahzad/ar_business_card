import pygame
import cv2
import numpy as np
from PIL import Image

def mm_to_pixels(mm, dpi=300):
    return int((mm / 25.4) * dpi)

def generate_aruco_marker(marker_id, pixel_size):
    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
    marker = np.zeros((pixel_size, pixel_size), dtype=np.uint8)
    marker = cv2.aruco.generateImageMarker(aruco_dict, marker_id, pixel_size, marker, 1)
    marker = cv2.rotate(marker, cv2.ROTATE_90_CLOCKWISE)
    marker = cv2.flip(marker, 1)
    return marker

def main(display_width, display_height):
    pygame.init()
    screen = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("Business Card ArUco Markers")

    # Generate at 300 DPI for print quality
    PRINT_DPI = 300
    card_width_px = mm_to_pixels(85, PRINT_DPI)
    card_height_px = mm_to_pixels(55, PRINT_DPI)
    margin_px = mm_to_pixels(3.175, PRINT_DPI)

    # Calculate marker size (staying within margins)
    marker_size_px = min(card_height_px - (2 * margin_px), 
                        card_width_px - (2 * margin_px)) // 4

    # Create surface for the card at print resolution
    card_surface = pygame.Surface((card_width_px, card_height_px))
    card_surface.fill((255, 255, 255))

    # Generate and place markers
    for i in range(4):
        marker = generate_aruco_marker(i + 1, marker_size_px)
        marker_rgb = np.stack((marker,) * 3, axis=-1)
        marker_surface = pygame.surfarray.make_surface(marker_rgb)
        
        if i == 0:    # Top-left
            pos = (margin_px, margin_px)
        elif i == 1:  # Top-right
            pos = (card_width_px - margin_px - marker_size_px, margin_px)
        elif i == 2:  # Bottom-left
            pos = (margin_px, card_height_px - margin_px - marker_size_px)
        else:         # Bottom-right
            pos = (card_width_px - margin_px - marker_size_px, 
                  card_height_px - margin_px - marker_size_px)
        
        card_surface.blit(marker_surface, pos)

    # Scale the card surface to display size
    display_surface = pygame.transform.smoothscale(card_surface, (display_width, display_height))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    pygame.image.save(card_surface, "business_card_markers.png")

        screen.fill((200, 200, 200))
        screen.blit(display_surface, (0, 0))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    # Screen DPI for display window size
    SCREEN_DPI = 171.7  # Your laptop's actual DPI
    
    # Calculate display window size
    SCREEN_WIDTH = int((85 / 25.4) * SCREEN_DPI)   # For display window
    SCREEN_HEIGHT = int((55 / 25.4) * SCREEN_DPI)  # For display window
    
    main(SCREEN_WIDTH, SCREEN_HEIGHT)

    img = Image.open("business_card_markers.png")
    print(f"Image dimensions: {img.size[0]}x{img.size[1]} pixels")
    print(f"Display window dimensions: {SCREEN_WIDTH}x{SCREEN_HEIGHT} pixels")