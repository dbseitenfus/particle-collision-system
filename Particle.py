import pygame
from pygame.math import Vector2
import math

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
                if particle.pos != self.pos and self.is_collided(particle):
                    self.handle_collision(particle)
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
            normal = self.pos - particle.pos
            normal = normal.normalize()
            
            # Vetor tangente
            tangent = Vector2(-normal.y, normal.x)
            
            # Projeção das velocidades no vetor normal e tangente
            v1n = self.dir.dot(normal)
            v1t = self.dir.dot(tangent)
            v2n = particle.dir.dot(normal)
            v2t = particle.dir.dot(tangent)
            
            # As velocidades tangenciais permanecem as mesmas
            v1t_new = v1t
            v2t_new = v2t
            
            # Troca das velocidades normais
            v1n_new = v2n
            v2n_new = v1n
            
            # Convertendo escalares para vetores
            v1n_new_vec = v1n_new * normal
            v1t_new_vec = v1t_new * tangent
            v2n_new_vec = v2n_new * normal
            v2t_new_vec = v2t_new * tangent
            
            # Novas direções
            self.dir = v1n_new_vec + v1t_new_vec
            particle.dir = v2n_new_vec + v2t_new_vec
            
            # Corrigir as posições para evitar sobreposição
            overlap = (self.radius + particle.radius) - self.pos.distance_to(particle.pos)
            correction = normal * (overlap / 2)
            self.pos += correction
            particle.pos -= correction
    
    def increase_size(self):
        self.radius += 5

    def remove_particle(self):
        self.alive = False  # Definindo a partícula como morta
        # self.pos = Vector2(-1000, -1000)

    def euclidean_distance(self, point_1, point_2):
        s = 0.0
        for i in range(len(point_1)):
            s += ((point_1[i] - point_2[i]) ** 2)
        return s ** 0.5

    def is_collided(self, particle):
        return self.alive and particle.alive and self.euclidean_distance(self.pos, particle.pos) <= self.radius + particle.radius

    def update_pos(self):
        if self.alive:  # Verificando se a partícula está viva antes de atualizar sua posição
            self.pos += self.dir * self.speed
    
    def change_pos(self, x, y):
        self.pos = Vector2(x, y)
    

