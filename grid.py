import pygame

from game_of_life import *


#жизнь
grid_state = [[dead for _ in range(total_cols)]
              for _ in range(total_cols)]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #сохранение файла поколения
            with open ("initial_pattern.txt", "w") as file:
                for row in grid_state:
                    row_string = ""
                    for cell in row:
                        row_string += str(cell)
                    file.write(row_string + "\n")
            pygame.quit()
            sys.exit()



        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            col = pos[0] // cell_size
            row = pos[1] // cell_size

            if grid_state[row][col] == dead:
                grid_state[row][col] = alive
            else:
                grid_state[row][col] = dead



    screen.fill(white)
    draw_grid()
    display_cells(grid_state)

    pygame.display.update()
