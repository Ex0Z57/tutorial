import pygame

# Initialize Pygame
pygame.init()

# Set the width and height of the screen (in pixels)
screen_width = 800
screen_height = 600

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("Jumping DEMO")

# Square properties
square_size = 100
square_color = (255, 0, 0)  # Red color

# Square initial position (bottom left corner)
square_x = 0
square_y = screen_height - square_size

# Jump variables
jump_height = 100
jump_speed = 5
is_jumping = False
jump_count = 0

# Gravity variables
gravity = 1
fall_speed = 0

# Pygame clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                is_jumping = True
                jump_count = 0

    # Jumping logic
    if is_jumping:
        if jump_count < jump_height:
            square_y -= jump_speed + 17
            jump_count += 1
        else:
            is_jumping = False

    # Falling logic
    if is_jumping:
        
      fall_speed += gravity
      square_y += fall_speed 


    # Fill the screen with a color (e.g., white)
    screen.fill((255, 255, 255))

    # Draw the square
    pygame.draw.rect(screen, square_color, (square_x, square_y, square_size, square_size))

    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
