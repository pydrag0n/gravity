import pygame
import sys
import math
import random
from objects_ import Ball
from config import FPS, BACKROUND_COLOR, WIDTH, HEIGHT, FONT_SIZE

# Инициализация Pygame
pygame.init()



# Настройки окна

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GRV81")

# Настройка шрифта
font = pygame.font.Font(None, FONT_SIZE)


# Основной цикл
clock = pygame.time.Clock()


def main():
    global balls_list
    balls_list = []
    
    # TEST
    # for i in range(0, 100):
    #     b = Ball(surface=screen, x=random.randint(10, WIDTH), y=random.randint(10, HEIGHT))
    #     balls_list.append(b)

    while True:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    x, y = pygame.mouse.get_pos()
                    size = random.randint(5, 30)
                    b = Ball(surface=screen, x=x, y=y)
                    balls_list.append(b)
                    
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    balls_list = []
                if event.key == pygame.K_q:
                    for ba in balls_list:
                        ba.R_size -=1
        


        screen.fill(BACKROUND_COLOR)
        display_fpx_objs()
        for ball in balls_list:
            ball.apply_gravity(balls_list)
        update_obj_pos()
        
        
        pygame.display.flip()
        clock.tick(FPS)


def display_fpx_objs():
    fps = clock.get_fps()
    fps_surface = font.render(f"FPS: {int(fps)}", True, (255, 255, 255))
    obj_surface = font.render(f"OBJ: {len(balls_list)}", True, (255, 255, 255))
    screen.blit(fps_surface, (10, 10))
    screen.blit(obj_surface, (10, 30))


def update_obj_pos():
    for ball in balls_list:
        ball.update_position()
        ball.draw()


if __name__ == "__main__":
    main()