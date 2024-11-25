<<<<<<< Updated upstream
import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up the game screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("FNF-like Game")

# Set up clock to control frame rate
clock = pygame.time.Clock()

# Load assets (music, images, etc.)
# Replace with the actual paths to your assets
background = pygame.Surface((screen_width, screen_height))
background.fill((255, 255, 255))  # White background for simplicity
pygame.mixer.music.load("your_song.mp3")

# Define key mappings (this will depend on your game's design)
key_map = {
    pygame.K_LEFT: 'left',
    pygame.K_DOWN: 'down',
    pygame.K_RIGHT: 'right',
    pygame.K_UP: 'up'
}

# Define the timing for beats (in real games, beats are based on the music)
# This is just an example of how the rhythm can be set up.
# You could sync this with the actual beats of the song.
beats = [
    {'time': 1, 'key': pygame.K_LEFT},
    {'time': 2, 'key': pygame.K_DOWN},
    {'time': 3, 'key': pygame.K_RIGHT},
    {'time': 4, 'key': pygame.K_UP},
]

# Initialize game state variables
start_time = None
current_beat = 0
score = 0
def game_loop():
    global start_time, current_beat, score

    # Play the song
    pygame.mixer.music.play()

    # Start timing
    start_time = time.time()

    # Main game loop
    running = True
    while running:
        screen.fill((0, 0, 0))  # Clear screen (black background)
        
        # Check for events (key presses)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in key_map:
                    # Check if keypress matches the current beat
                    if current_beat < len(beats) and event.key == beats[current_beat]['key']:
                        # Correct keypress
                        score += 10
                        current_beat += 1
                    else:
                        # Incorrect keypress
                        score -= 5
        
        # Display the score (just an example)
        font = pygame.font.SysFont("Arial", 36)
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        
        # Draw the background (you can replace it with characters or animation)
        screen.blit(background, (0, 0))

        # Check if the song is still playing
        elapsed_time = time.time() - start_time

        # Handle beats timing
        if current_beat < len(beats) and elapsed_time >= beats[current_beat]['time']:
            current_beat += 1

        # Update the screen
        pygame.display.update()

        # Limit the frame rate
        clock.tick(60)

# Start the game loop
game_loop()

# Quit pygame
pygame.quit()
character_image = pygame.image.load("character.png")
screen.blit(character_image, (400, 300))  # Position the character
=======
import pygame, sys, random, time
from pygame.locals import *

# set up pygame
pygame.init()
mainClock = pygame.time.Clock()

# set up the window
WINDOWWIDTH = 1000
WINDOWHEIGHT = 1000
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Final')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
NEWBLOCK = 40
BLOCKSIZE = 20
player = pygame.Rect(500, 500, 30, 30)
blocks = []

moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 7

DOWNLEFT = 1
DOWNRIGHT = 3
UPLEFT = 7
UPRIGHT = 9

b1 ={'rect':pygame.Rect(1, 1, 50, 50), 'color':RED, 'dir':UPLEFT}
b2 ={'rect':pygame.Rect(925, 1, 50, 50), 'color':RED, 'dir':UPRIGHT}
b3 ={'rect':pygame.Rect(760, 760, 50, 50), 'color':RED, 'dir':UPLEFT}
b4 ={'rect':pygame.Rect(1, 925, 50, 50), 'color':RED, 'dir':UPRIGHT}
b5 ={'rect':pygame.Rect(1, 462, 50, 50), 'color':RED, 'dir':UPLEFT}
b6 ={'rect':pygame.Rect(462, 231, 50, 50), 'color':RED, 'dir':UPRIGHT}
b7 ={'rect':pygame.Rect(231, 462, 50, 50), 'color':RED, 'dir':UPLEFT}
b8 ={'rect':pygame.Rect(325, 325, 50, 50), 'color':RED, 'dir':UPLEFT}
b9 ={'rect':pygame.Rect(100, 625, 50, 50), 'color':RED, 'dir':UPLEFT}
b10 ={'rect':pygame.Rect(530, 1, 50, 50), 'color':RED, 'dir':UPLEFT}
blocks = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10]

while True:
# check for events
    for event in pygame.event.get():
if event.type == QUIT:
pygame.quit()
sys.exit()
if event.type == KEYDOWN:
# change the keyboard variables
if event.key == K_LEFT or event.key == ord('a'):
moveRight = False
moveLeft = True
if event.key == K_RIGHT or event.key == ord('d'):
moveLeft = False
moveRight = True
if event.key == K_UP or event.key == ord('w'):
moveDown = False
moveUp = True
if event.key == K_DOWN or event.key == ord('s'):
moveUp = False
moveDown = True
if event.type == KEYUP:
if event.key == K_ESCAPE:
pygame.quit()
sys.exit()
if event.key == K_LEFT or event.key == ord('a'):
moveLeft = False
if event.key == K_RIGHT or event.key == ord('d'):
moveRight = False
if event.key == K_UP or event.key == ord('w'):
moveUp = False
if event.key == K_DOWN or event.key == ord('s'):
moveDown = False

for b in blocks:
# move the block data structure
if b['dir'] == DOWNLEFT:
b['rect'].left -= MOVESPEED
b['rect'].top += MOVESPEED
if b['dir'] == DOWNRIGHT:
b['rect'].left += MOVESPEED
b['rect'].top += MOVESPEED
if b['dir'] == UPLEFT:
b['rect'].left -= MOVESPEED
b['rect'].top -= MOVESPEED
if b['dir'] == UPRIGHT:
b['rect'].left += MOVESPEED
b['rect'].top -= MOVESPEED
# check if the block has move out of the window
if b['rect'].top < 0:
# block has moved past the top
if b['dir'] == UPLEFT:
b['dir'] = DOWNLEFT
if b['dir'] == UPRIGHT:
b['dir'] = DOWNRIGHT
if b['rect'].bottom > WINDOWHEIGHT:
# block has moved past the bottom
if b['dir'] == DOWNLEFT:
b['dir'] = UPLEFT
if b['dir'] == DOWNRIGHT:
b['dir'] = UPRIGHT
if b['rect'].left < 0:
# block has moved past the left side
if b['dir'] == DOWNLEFT:
b['dir'] = DOWNRIGHT
if b['dir'] == UPLEFT:
b['dir'] = UPRIGHT
if b['rect'].right > WINDOWWIDTH:
# block has moved past the right side
if b['dir'] == DOWNRIGHT:
b['dir'] = DOWNLEFT
if b['dir'] == UPRIGHT:
b['dir'] = UPLEFT
# draw the block onto the surface
pygame.draw.rect(windowSurface, b['color'], b['rect'])

pygame.display.update()
time.sleep(0.02)

windowSurface.fill(BLACK)
if moveDown and player.bottom < WINDOWHEIGHT:
player.top += MOVESPEED
if moveUp and player.top > 0:
player.top -= MOVESPEED
if moveLeft and player.left > 0:
player.left -= MOVESPEED
if moveRight and player.right < WINDOWWIDTH:
player.right += MOVESPEED

for b in blocks[:]:
if player.colliderect(players):
players.remove(player)

pygame.draw.rect(windowSurface, WHITE, player)
>>>>>>> Stashed changes
Piano
11/22/24
1. I need to make a code where I can play a piano when I run the code. The first problem I faced was when the code said a error about pygame. I said chatgpt how to fix this problem and I suggest to use th code pip install pygame but it still didn't work so i uninstalled pygames and than install it again and it work. But, I guess today was not my day because the problem of the pygame thing came up again. Also, that I need to fixed a way for the code to play music but i don't know how to do that. 
2. I used chatgpt to help make the nosie that didn't work and than I watch a video about it and it kinda worked. Also, I use chatgpt to fix my pygame problem . At first for my code I had no idea how to start it but than it gave me a code, (screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) pygame.display.set_caption("Virtual Piano"))
3. My first question - How to make a game screen for my code in python. - I don't know waht this means can you eplain it better. - Why is this code not work but i worked yesterday.
4. The problem was to use pip install pygame but it still didn't work. Than one day it worked until it didn't work today T_T. 
5. ChatGPT DIDN'T work, I asked it to solve a problem like the pygames thing doesn't work are there any anyother ways to do this. IT GAVE ME THE SAME SOLUTION THAT DIDN'T WORK when I clearly stated IT DIDN'T WORK.
6. I did run tests like after each section i did i ran a test, but chatgpt is so bad very time i asked it a question like how to fix the code it didn't help.
7) I learned how to make a game screen and that pygames are fun. Oh also, I learn how to break a code in to little steps like first I did the game screen and than did the codes. It is also, apparent that installing pygames on my computer is very hard and annoying.