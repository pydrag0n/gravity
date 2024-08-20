import pygame
import math
from config import (G, 
                    def_color, 
                    def_size, 
                    def_mass, 
                    def_x, 
                    def_y, 
                    def_vx, 
                    def_vy,
                    def_isdraw_line,
                    def_line_color,
                    def_line_width
                    )

class Ball:
    def __init__(self, 
                 surface,
                 color: tuple=def_color,
                 r_size: int=def_size,
                 mass: int=def_mass,
                 x: float=def_x, y: float=def_y,
                 vx: int=def_vx, vy:int=def_vy,
                 isdraw_line: bool=def_isdraw_line,
                 line_color: tuple=def_line_color
                 ) -> None:
        
        self.surface = surface
        self.color = color
        self.R_size = r_size
        self.M = mass
        self.x = x
        self.y = y
        self.vx = vx  # Начальная скорость по x
        self.vy = vy # Начальная скорость по y
        self.isdraw_line = isdraw_line
        self.spawn_point = []
        self.line_color = line_color
        self.line_width = def_line_width
        
        
    def draw(self):
        pygame.draw.circle(self.surface, 
                           self.color, 
                           (int(self.x), 
                            int(self.y)), 
                           self.R_size
                           )
        
        if self.isdraw_line:
            if len(self.spawn_point) > 1:
                pygame.draw.lines(self.surface, 
                                  self.line_color, 
                                  False, 
                                  self.spawn_point, 
                                  self.line_width
                                  )

    def apply_gravity(self, balls):
        for other in balls:
            if other != self:
                dx = other.x - self.x
                dy = other.y - self.y
                distance = math.sqrt(dx**2 + dy**2)

                # Обработка коллизий
                if distance < self.R_size + other.R_size:
                    # Находим нормализованный вектор
                    overlap = self.R_size + other.R_size - distance
                    norm_dx = dx / distance
                    norm_dy = dy / distance
                    
                    # Обравляем позиции шаров
                    self.x -= norm_dx * overlap * 0.5
                    self.y -= norm_dy * overlap * 0.5
                    other.x += norm_dx * overlap * 0.5
                    other.y += norm_dy * overlap * 0.5
                
                # Рассчитываем силу притяжения и изменение скорости
                if distance > 0:
                    force = G * (self.M * other.M) / (distance**2)
                    fx = force * (dx / distance)
                    fy = force * (dy / distance)
                    self.vx += fx / self.M
                    self.vy += fy / self.M
            
    def update_position(self):
        self.spawn_point.append((self.x, self.y)) # сохраняем точку спавна
        self.x += self.vx
        self.y += self.vy
        
