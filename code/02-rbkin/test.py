import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Coordinate Frames")

# Function to draw coordinate frames
def draw_coordinate_frames():
    # Draw the red coordinate frame
    pygame.draw.line(screen, RED, (100, 100), (200, 100), 2)  # X-axis
    pygame.draw.line(screen, RED, (100, 100), (100, 200), 2)  # Y-axis
    pygame.draw.circle(screen, RED, (100, 100), 5)  # Origin
    
    # Draw the blue coordinate frame
    pygame.draw.line(screen, BLUE, (300, 300), (400, 300), 2)  # X-axis
    pygame.draw.line(screen, BLUE, (300, 300), (300, 400), 2)  # Y-axis
    pygame.draw.circle(screen, BLUE, (300, 300), 5)  # Origin

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw the coordinate frames
    draw_coordinate_frames()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
