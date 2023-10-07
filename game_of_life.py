import pygame, sys, os, copy, time

sc_width_heighy = 800
total_cols = 80
cell_size = sc_width_heighy // total_cols
alive = 1
dead = 0

PAUSE_LENGTH = 0.15

#загрузка клетки
Alive_img = pygame.image.load(os.path.join("Graphics", "Alive.jpg"))

black = (128,128,128)
white = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((sc_width_heighy, sc_width_heighy))


def load_init_pattern():
    next_gen=[]
    with open ("initial_pattern.txt", "r") as file:
        for line in file:
            row=[]
            for char in line.strip():
                row.append(int(char))
            next_gen.append(row)
    return next_gen


def draw_grid():
    for row in range(total_cols):
        for col in range(total_cols):
            rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, black, rect, 1)

def display_cells(cells):
    for x in range(total_cols):
        for y in range(total_cols):
            if cells[y][x] == alive:
                screen.blit(Alive_img, (x*cell_size, y*cell_size))


def get_next_gen(current_gen, next_gen):
    for x in range(total_cols):
        for y in range(total_cols):
            left = (x-1) % total_cols
            right = (x+1) % total_cols
            above = (y-1) % total_cols
            below = (y+1) % total_cols

            numNeighbours = 0
            if current_gen[above][left] == alive:
                numNeighbours += 1
            if current_gen[above][x] == alive:
                numNeighbours += 1
            if current_gen[above][right] == alive:
                numNeighbours += 1
            if current_gen[y][left] == alive:
                numNeighbours += 1
            if current_gen[y][right] == alive:
                numNeighbours += 1
            if current_gen[below][left] == alive:
                numNeighbours += 1
            if current_gen[below][x] == alive:
                numNeighbours += 1
            if current_gen[below][right] == alive:
                numNeighbours += 1

            if current_gen[y][x] == alive and (numNeighbours == 2 or numNeighbours == 3):
                next_gen[y][x] = alive
            elif current_gen[y][x] == dead and numNeighbours == 3:
                next_gen[y][x] = alive
            else:
                next_gen[y][x] = dead