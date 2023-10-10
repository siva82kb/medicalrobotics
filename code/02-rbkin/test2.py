import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

# Initialize Pygame
pygame.init()

# Constants for screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("3D Environment")

# Define the initial camera position and orientation
camera_x, camera_y, camera_z = 0, 0, -5
camera_rot_x, camera_rot_y = 0, 0
camera_speed = 0.1

# Function to draw the 3D environment
def draw_environment():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(camera_x, camera_y, camera_z)
    glRotatef(camera_rot_x, 1, 0, 0)
    glRotatef(camera_rot_y, 0, 1, 0)
    
    # Draw your 3D objects here
    
    glutSolidCube(1)  # Example: Drawing a cube

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == MOUSEMOTION:
            # Update camera rotation based on mouse movement
            x, y = event.rel
            camera_rot_x += y * camera_speed
            camera_rot_y += x * camera_speed

    # Check for keyboard input to move the camera
    keys = pygame.key.get_pressed()
    if keys[K_w]:
        camera_z += camera_speed
    if keys[K_s]:
        camera_z -= camera_speed
    if keys[K_a]:
        camera_x += camera_speed
    if keys[K_d]:
        camera_x -= camera_speed

    # Clear the screen
    screen.fill(BLACK)

    # Enable 3D rendering
    glEnable(GL_DEPTH_TEST)
    draw_environment()
    glDisable(GL_DEPTH_TEST)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
