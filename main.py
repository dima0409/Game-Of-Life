from game_of_life import *

next_gen = load_init_pattern()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    current_gen = copy.deepcopy(next_gen)

    screen.fill(white)
    draw_grid()
    display_cells(current_gen)

    time.sleep(PAUSE_LENGTH)

    pygame.display.update()

    get_next_gen(current_gen, next_gen)