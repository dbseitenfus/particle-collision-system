import pygame
from Particle import Particle
import random 
from sys import exit
import math
from pygame.math import Vector2

particles = []
WIDTH, HEIGHT = 800, 800
grid = []
grid_size = 50

def add_particle_to_grid(particle):
    i, j = get_particle_position_on_grid(particle)
    grid[i][j].append(particle)

def get_particle_position_on_grid(particle):
    x = particle.pos.x
    y = particle.pos.y
    i = int(x//grid_size)-1 if x > 0 else 0
    j = int(y//grid_size)-1 if y > 0 else 0
    return (i,j)
    
def clear_grid():
    grid.clear()
    rows = HEIGHT//grid_size 
    columns = WIDTH//grid_size 
    for i in range(rows):
        grid.append([])
        for j in range(columns):
            grid[i].append([])

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
        add_particle_to_grid(particle)
        i,j = get_particle_position_on_grid(particle)
        particle.guidance([0, WIDTH, 0, HEIGHT], grid[i][j])

def create_particles():
    for i in range(5000):
        pos = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        angle = random.uniform(0, 2 * math.pi)  
        dir = Vector2(math.cos(angle), math.sin(angle))
        speed = 2
        radius = 2
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
        clear_grid()
        draw_particles()
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
