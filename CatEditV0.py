import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SIZE = 50

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Initialize screen and clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flames Edit V0.X.X')
clock = pygame.time.Clock()

class GameObject:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

# Initialize player
player = GameObject(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, PLAYER_SIZE, PLAYER_SIZE, BLUE)

# Dynamic Scripting System
def execute_script(script, obj):
    try:
        # Define a limited set of safe commands
        safe_commands = {
            'move_left': 'obj.x -= 5',
            'move_right': 'obj.x += 5',
            'move_up': 'obj.y -= 5',
            'move_down': 'obj.y += 5'
        }
        
        # Execute the command if it's safe
        if script in safe_commands:
            eval(safe_commands[script])
        else:
            print(f"Unknown command: {script}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Scripting Console
    script = input("Enter script command (move_left, move_right, move_up, move_down): ")
    execute_script(script, player)

    # Rendering
    screen.fill(WHITE)
    player.draw(screen)

    pygame.display.update()
    clock.tick(60)
