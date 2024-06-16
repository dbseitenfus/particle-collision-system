import pygame
from Particle import Particle
import random 
from sys import exit
import math
from pygame.math import Vector2
from particles_manager import *

particles = []
WIDTH, HEIGHT = 700, 700
particles_manager = ParticlesManager(WIDTH, HEIGHT, 10)
    
def add_particle(position, direction, speed, radius, color):
    particles.append(Particle(position, direction, speed, radius, color))

def set_particles_speed(speed):
    global particles_speed
    particles_speed = speed
    for particle in particles:
        particle.speed = particles_speed

def draw_particles():
    for particle in particles:
        particle.draw(screen)
        particle.update_pos()
        particles_manager.add_particle_to_grid(particle)
        i,j = particles_manager.get_particle_position_on_grid(particle)
        if i < particles_manager.columns_size and j < particles_manager.rows_size:
            particle.guidance([0, WIDTH, 0, HEIGHT], particles_manager.grid[i][j])

def create_particles():
    for i in range(7000):
        pos = (WIDTH//2,HEIGHT//2)
        angle = random.uniform(0, 2 * math.pi)  
        dir = Vector2(math.cos(angle), math.sin(angle))
        speed = 3
        radius = 1
        add_particle(pos, dir, speed, radius, (255, 255, 255))

def render():
    bg = pygame.Surface((WIDTH, HEIGHT))
    bg.fill((20, 20, 20))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.blit(bg, (0, 0))
        particles_manager.clear_grid()
        draw_particles()
        # draw_partitions(screen)
        clock.tick(30)
        pygame.display.update()
           

def main():
    create_particles()
    render()
    pygame.quit()
    exit()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Particle Simulation")
    clock = pygame.time.Clock()

    main()
