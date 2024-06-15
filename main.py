import pygame
from Particle import Particle
import random 
from sys import exit
import math
from pygame.math import Vector2

particles = []
WIDTH, HEIGHT = 500, 500

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
        particle.guidance([0, WIDTH, 0, HEIGHT], particles)
        particle.update_pos()
           

def main():
    bg = pygame.Surface((WIDTH, HEIGHT))
    bg.fill((20, 20, 20))


    for i in range(2000):
        pos = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        angle = random.uniform(0, 2 * math.pi)  
        dir = Vector2(math.cos(angle), math.sin(angle))
        speed = 3
        radius = 2
        add_particle(pos, dir, speed, radius, (255, 255, 255))
 
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.blit(bg, (0, 0))

        draw_particles()

        clock.tick(30)
        pygame.display.update()

    pygame.quit()
    exit()

if __name__ == "__main__":

    pygame.init()

    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    WIDTH, HEIGHT = pygame.display.get_surface().get_size()
    pygame.display.set_caption("Particle Simulation")
    clock = pygame.time.Clock()

    main()
