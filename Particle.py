from functions_geometric import euclidean_distance
import pygame
from pygame.math import Vector2

class Particle:
    def __init__(self, position, direction, speed, radius, color):
        self.pos = Vector2(position)
        self.dir = Vector2(direction).normalize()
        self.speed = speed
        self.radius = radius
        self.alive = True  # Adicionando o atributo alive para determinar se a partícula está viva
        self.color = color
        self.collision_status = False
        
    def draw(self, screen):
        if self.alive:  # Verificando se a partícula está viva antes de desenhá-la
            pygame.draw.circle(screen, self.color, (int(self.pos[0]), int(self.pos[1])), self.radius)

    def check_collision(self, particles):
        if self.alive:  # Verificando se a partícula está viva antes de verificar colisão
            for particle in particles:
                # if particle.pos != self.pos and self.is_collided(particle):
                #     self.handle_collision(particle)
                    break
    
    def guidance(self, box, particles):
        if self.alive:  # Verificando se a partícula está viva antes de realizar a orientação
            self.boundary_update_dir(box)
            self.check_collision( particles)

    def boundary_update_dir(self, box):
        if self.alive:  # Verificando se a partícula está viva antes de atualizar sua direção
            if self.pos.x <= box[0] + self.radius and self.dir.x < 0:
                self.dir.x *= -1
            elif self.pos.x >= box[1] - self.radius and self.dir.x > 0:
                self.dir.x *= -1
            if self.pos.y <= box[2] + self.radius and self.dir.y < 0:
                self.dir.y *= -1
            elif self.pos.y >= box[3] - self.radius and self.dir.y > 0:
                self.dir.y *= -1

    def handle_collision(self, particle):
        if self.alive:  # Verificando se a partícula está viva antes de manipular a colisão
            # self.increase_size()
            particle.remove_particle()
    
    def increase_size(self):
        self.radius += 5

    def remove_particle(self):
        self.alive = False  # Definindo a partícula como morta
        # self.pos = Vector2(-1000, -1000)

    def is_collided(self, particle):
        return self.alive and particle.alive and euclidean_distance(self.pos, particle.pos) <= self.radius + particle.radius

    def update_pos(self):
        if self.alive:  # Verificando se a partícula está viva antes de atualizar sua posição
            self.pos += self.dir * self.speed
    
    def change_pos(self, x, y):
        self.pos = Vector2(x, y)
    
    def euclidean_distance(point_1, point_2):
        s = 0.0
        for i in range(len(point_1)):
            s += ((point_1[i] - point_2[i]) ** 2)
        return s ** 0.5

