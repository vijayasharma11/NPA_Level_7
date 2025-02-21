import pygame
import random

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 400
GRAVITY = 0.5
JUMP_STRENGTH = -10
SPEED = 5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel Runner")

# Load assets
player_img = pygame.image.load("images/player.png")
obstacle_img = pygame.image.load("images/obstacle.png")
 # Replace with actual image path

# Define player class
class Player:
    def __init__(self):
        self.image = pygame.transform.scale(player_img, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 100, HEIGHT - 100
        self.velocity_y = 0
        self.on_ground = True
    
    def jump(self):
        if self.on_ground:
            self.velocity_y = JUMP_STRENGTH
            self.on_ground = False
    
    def update(self):
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y
        if self.rect.y >= HEIGHT - 100:
            self.rect.y = HEIGHT - 100
            self.on_ground = True

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Define obstacle class
class Obstacle:
    def __init__(self, x):
        self.image = pygame.transform.scale(obstacle_img, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = HEIGHT - 100
    
    def update(self):
        self.rect.x -= SPEEDplayer_img 
        if self.rect.x < -50:
            self.rect.x = WIDTH + random.randint(100, 300)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Initialize player and obstacles
player = Player()
obstacles = [Obstacle(WIDTH + i * 300) for i in range(3)]

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(30)
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()
    
    # Update objects
    player.update()
    for obstacle in obstacles:
        obstacle.update()
        if player.rect.colliderect(obstacle.rect):
            running = False  # End game on collision
    
    # Draw objects
    player.draw(screen)
    for obstacle in obstacles:
        obstacle.draw(screen)
    
    pygame.display.flip()

pygame.quit()
