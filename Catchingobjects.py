import pygame
import random
import sys


pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Object with Bombs")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)


paddle_width = 100
paddle_height = 20
paddle_x = WIDTH // 2 - paddle_width // 2
paddle_y = HEIGHT - 50
paddle_speed = 10

object_width = 30
object_height = 30
object_x = random.randint(0, WIDTH - object_width)
object_y = 0
object_speed = 5


bomb_width = 30
bomb_height = 30
bomb_x = random.randint(0, WIDTH - bomb_width)
bomb_y = 0
bomb_speed = 10


score = 0
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()


running = True
while running:
    screen.fill(WHITE)

   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += paddle_speed

    
    object_y += object_speed

   
    bomb_y += bomb_speed

    
    if (
        paddle_x < object_x < paddle_x + paddle_width
        or paddle_x < object_x + object_width < paddle_x + paddle_width
    ) and paddle_y < object_y + object_height < paddle_y + paddle_height:
        score += 1
        object_x = random.randint(0, WIDTH - object_width)
        object_y = 0
        object_speed += 0.2  

    
    if (
        paddle_x < bomb_x < paddle_x + paddle_width
        or paddle_x < bomb_x + bomb_width < paddle_x + paddle_width
    ) and paddle_y < bomb_y + bomb_height < paddle_y + paddle_height:
        print("GAME OVER. YOU CAUGHT A BOMB!!!!")
        print("Final Score:", score)
        pygame.quit()
        sys.exit()

    
    if object_y > HEIGHT:
        object_x = random.randint(0, WIDTH - object_width)
        object_y = 0

    
    if bomb_y > HEIGHT:
        bomb_x = random.randint(0, WIDTH - bomb_width)
        bomb_y = 0

    
    pygame.draw.rect(screen, BLUE, (paddle_x, paddle_y, paddle_width, paddle_height))

   
    pygame.draw.rect(screen, GREEN, (object_x, object_y, object_width, object_height))

   
    pygame.draw.rect(screen, RED, (bomb_x, bomb_y, bomb_width, bomb_height))

   
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    
    pygame.display.flip()

    
    clock.tick(30)
