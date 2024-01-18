# Import the pygame and random modules
import pygame
import random

# Initialize pygame
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Define the screen size and create the screen object
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption("Snake Game")


# Define the snake class
class Snake:
    # Initialize the snake with a position, a direction, and a body
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.body = []

    # Draw the snake on the screen
    def draw(self):
        # Draw the head of the snake
        pygame.draw.rect(screen, GREEN, [self.x, self.y, 20, 20])
        # Draw the body of the snake
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, [segment[0], segment[1], 20, 20])

    # Move the snake according to its direction
    def move(self):
        # Add the current position to the body
        self.body.append([self.x, self.y])
        # Remove the last segment of the body if the snake is not growing
        if len(self.body) > self.length:
            self.body.pop(0)
        # Update the position of the head
        self.x += self.dx
        self.y += self.dy
        # Wrap the snake around the screen edges
        if self.x < 0:
            self.x = SCREEN_WIDTH - 20
        if self.x > SCREEN_WIDTH - 20:
            self.x = 0
        if self.y < 0:
            self.y = SCREEN_HEIGHT - 20
        if self.y > SCREEN_HEIGHT - 20:
            self.y = 0

    # Check if the snake has collided with itself
    def collide(self):
        # Loop through the body segments
        for segment in self.body[:-1]:
            # If the head position matches a body segment, return True
            if self.x == segment[0] and self.y == segment[1]:
                return True
        # Otherwise, return False
        return False

    # Check if the snake has eaten the food
    def eat(self, food):
        # If the head position matches the food position, return True
        if self.x == food.x and self.y == food.y:
            return True
        # Otherwise, return False
        return False

    # Grow the snake by one segment
    def grow(self):
        # Increase the length attribute by one
        self.length += 1


# Define the food class
class Food:
    # Initialize the food with a random position
    def __init__(self):
        self.x = random.randrange(0, SCREEN_WIDTH, 20)
        self.y = random.randrange(0, SCREEN_HEIGHT, 20)

    # Draw the food on the screen
    def draw(self):
        pygame.draw.rect(screen, RED, [self.x, self.y, 20, 20])

    # Move the food to a new random position
    def move(self):
        self.x = random.randrange(0, SCREEN_WIDTH, 20)
        self.y = random.randrange(0, SCREEN_HEIGHT, 20)


# Create a snake object
snake = Snake(400, 300, 20, 0)
# Set the initial length of the snake
snake.length = 3

# Create a food object
food = Food()

# Define the clock object to control the game speed
clock = pygame.time.Clock()

# Define a variable to store the game state
game_over = False

# Main game loop
while not game_over:
    # Handle the events
    for event in pygame.event.get():
        # If the user clicks the close button, exit the game
        if event.type == pygame.QUIT:
            game_over = True
        # If the user presses a key, change the direction of the snake
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.dx = -20
                snake.dy = 0
            if event.key == pygame.K_RIGHT:
                snake.dx = 20
                snake.dy = 0
            if event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -20
            if event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 20

    # Move the snake
    snake.move()

    # Check if the snake has collided with itself or the screen edges
    if snake.collide():
        game_over = True

    # Check if the snake has eaten the food
    if snake.eat(food):
        # Grow the snake
        snake.grow()
        # Move the food to a new position
        food.move()

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw the snake and the food
    snake.draw()
    food.draw()

    # Update the display
    pygame.display.flip()

    # Set the game speed to 10 frames per second
    clock.tick(10)

# Quit pygame
pygame.quit()
