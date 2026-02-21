"""
Snake Game
A classic arcade Snake game built with Pygame. 
Features custom graphics, score tracking, and a restart/quit menu.
"""

import pygame
import random
import sys

# Game Configuration
SNAKE_SPEED = 15
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 480

# Define Colors (RGB)
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
YELLOW = pygame.Color(255, 255, 0)
VIOLET = pygame.Color(138, 43, 226)
LIGHT_GREEN = pygame.Color(100, 200, 100)
DARK_GREEN = pygame.Color(0, 100, 0)

# Game states
RUNNING = 'running'
GAME_OVER = 'game_over'

def initialize_game():
    """Resets all game variables for a new game session."""
    snake_position = [100, 50]
    # Snake body consists of blocks [x, y]
    snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
    food_position = [random.randrange(1, WINDOW_WIDTH // 10) * 10,
                     random.randrange(1, WINDOW_HEIGHT // 10) * 10]
    direction = 'RIGHT'
    change_to = direction
    score = 0
    return snake_position, snake_body, food_position, direction, change_to, score

def draw_snake(game_window, snake_body):
    """Draws the snake with custom circular segments and eyes on the head."""
    for i, pos in enumerate(snake_body):
        if i == 0:  # Head - brighter green
            pygame.draw.circle(game_window, (0, 200, 0), (pos[0] + 5, pos[1] + 5), 5)
            # Add eyes to head
            pygame.draw.circle(game_window, WHITE, (pos[0] + 3, pos[1] + 3), 1)
            pygame.draw.circle(game_window, WHITE, (pos[0] + 7, pos[1] + 3), 1)
        else:  # Body - lighter green
            pygame.draw.circle(game_window, LIGHT_GREEN, (pos[0] + 5, pos[1] + 5), 5)
        # Add border/outline to each segment
        pygame.draw.circle(game_window, DARK_GREEN, (pos[0] + 5, pos[1] + 5), 5, 1)

def draw_food(game_window, food_position):
    """Draws an apple-style food object."""
    # Apple body
    pygame.draw.circle(game_window, RED, (food_position[0] + 5, food_position[1] + 5), 5)
    # Apple stem
    pygame.draw.line(game_window, GREEN, (food_position[0] + 5, food_position[1]), 
                    (food_position[0] + 5, food_position[1] - 3), 2)

def show_score(game_window, score, color, font, size):
    """Displays the current score on the screen."""
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render(f'Score: {score}', True, color)
    game_window.blit(score_surface, (0, 0))

def show_game_over_menu(game_window, final_score):
    """Displays the translucent game over menu with restart/quit instructions."""
    overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    overlay.set_alpha(200)
    overlay.fill(BLACK)
    game_window.blit(overlay, (0, 0))
    
    game_over_font = pygame.font.SysFont('times new roman', 50)
    game_over_text = game_over_font.render('GAME OVER!', True, RED)
    game_window.blit(game_over_text, 
                    (WINDOW_WIDTH/2 - game_over_text.get_width()/2, 60))
    
    score_font = pygame.font.SysFont('times new roman', 40)
    score_text = score_font.render(f'Score: {final_score}', True, YELLOW)
    game_window.blit(score_text,
                    (WINDOW_WIDTH/2 - score_text.get_width()/2, 150))
    
    instruction_font = pygame.font.SysFont('arial', 24)
    restart_text = instruction_font.render('Press R - RESTART', True, GREEN)
    game_window.blit(restart_text,
                    (WINDOW_WIDTH/2 - restart_text.get_width()/2, 250))
    
    quit_text = instruction_font.render('Press Q - QUIT', True, RED)
    game_window.blit(quit_text,
                    (WINDOW_WIDTH/2 - quit_text.get_width()/2, 300))
    
    pygame.display.update()

def main():
    # Initialize Pygame and the window
    pygame.init()
    pygame.display.set_caption('Snake Game')
    game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    # Load initial game state
    snake_position, snake_body, food_position, direction, change_to, score = initialize_game()
    food_spawn = True
    game_state = RUNNING

    # Main Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if game_state == RUNNING:
                    if event.key == pygame.K_UP:
                        change_to = 'UP'
                    if event.key == pygame.K_DOWN:
                        change_to = 'DOWN'
                    if event.key == pygame.K_LEFT:
                        change_to = 'LEFT'
                    if event.key == pygame.K_RIGHT:
                        change_to = 'RIGHT'
                
                if game_state == GAME_OVER:
                    if event.key == pygame.K_r:
                        snake_position, snake_body, food_position, direction, change_to, score = initialize_game()
                        food_spawn = True
                        game_state = RUNNING
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
        
        if game_state == RUNNING:
            # Validate direction change (prevent snake from reversing into itself)
            if change_to == 'UP' and direction != 'DOWN':
                direction = 'UP'
            if change_to == 'DOWN' and direction != 'UP':
                direction = 'DOWN'
            if change_to == 'LEFT' and direction != 'RIGHT':
                direction = 'LEFT'
            if change_to == 'RIGHT' and direction != 'LEFT':
                direction = 'RIGHT'

            # Move the snake head
            if direction == 'UP':
                snake_position[1] -= 10
            if direction == 'DOWN':
                snake_position[1] += 10
            if direction == 'LEFT':
                snake_position[0] -= 10
            if direction == 'RIGHT':
                snake_position[0] += 10

            # Grow snake body
            snake_body.insert(0, list(snake_position))

            # Check if food is eaten
            if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
                score += 10
                food_spawn = False
            else:
                snake_body.pop()

            # Spawn new food
            if not food_spawn:
                food_position = [random.randrange(1, WINDOW_WIDTH // 10) * 10,
                                random.randrange(1, WINDOW_HEIGHT // 10) * 10]
                food_spawn = True

            # Render graphics
            game_window.fill(VIOLET)
            draw_snake(game_window, snake_body)
            draw_food(game_window, food_position)

            # Collision Detection: Walls
            if (snake_position[0] < 0 or snake_position[0] > WINDOW_WIDTH - 10 or 
                snake_position[1] < 0 or snake_position[1] > WINDOW_HEIGHT - 10):
                game_state = GAME_OVER

            # Collision Detection: Self
            for block in snake_body[1:]:
                if snake_position[0] == block[0] and snake_position[1] == block[1]:
                    game_state = GAME_OVER

            show_score(game_window, score, WHITE, 'times new roman', 20)
            pygame.display.update()
            clock.tick(SNAKE_SPEED)
        
        elif game_state == GAME_OVER:
            show_game_over_menu(game_window, score)
            clock.tick(10)

if __name__ == '__main__':
    main()