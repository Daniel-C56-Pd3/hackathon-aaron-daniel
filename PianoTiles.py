import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Piano Tiles")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Set up font
font = pygame.font.Font(None, 36)

# Game variables
tile_width = screen_width // 5
tile_height = screen_height // 5
tile_speed = 6  # Speed at which the tiles move down
score = 0
game_over = False

# Create a list to store tiles
tiles = []

# Function to draw tiles
def draw_tiles():
    for tile in tiles:
        pygame.draw.rect(screen, tile['color'], (tile['x'], tile['y'], tile_width, tile_height))

# Function to check if tile was clicked
def check_tile_hit(x, y):
    global score
    for tile in tiles:
        if tile['x'] < x < tile['x'] + tile_width and tile['y'] < y < tile['y'] + tile_height:
            if tile['color'] == GREEN:  # Only hit green tiles
                score += 1
                tiles.remove(tile)
                return True
    return False

# Game loop
while not game_over:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if not check_tile_hit(x, y):
                game_over = True  # Player missed a tile

    # Move tiles down
    for tile in tiles:
        tile['y'] += tile_speed
        if tile['y'] >= screen_height:
            tiles.remove(tile)
            game_over = True  # Player missed a tile

    # Add new tiles
    if random.random() < 0.03:  # Random chance to add a new tile
        tile_x = random.randint(0, 3) * tile_width  # Random column (0 to 3)
        new_tile = {
            'x': tile_x,
            'y': -tile_height,  # Start just above the screen
            'color': GREEN  # All tiles are green now
        }
        tiles.append(new_tile)

    # Draw tiles and score
    draw_tiles()
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Check for game over (if game over, display message)
    if game_over:
        game_over_text = font.render("Game Over!", True, WHITE)
        screen.blit(game_over_text, (screen_width // 2 - 100, screen_height // 2 - 50))
        final_score_text = font.render(f"Final Score: {score}", True, WHITE)
        screen.blit(final_score_text, (screen_width // 2 - 100, screen_height // 2))

    # Update the screen
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Clean up
pygame.quit()
