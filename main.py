import Life
import pygame


if __name__ == '__main__':
    size = width, height = 620, 620
    screen = pygame.display.set_mode(size)
    board = Life.Life(20, 20)
    MYEVENTTYPE = pygame.USEREVENT + 1
    t = 1000
    pygame.time.set_timer(MYEVENTTYPE, t)
    running = True
    life_is_going = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not life_is_going:
                board.get_click(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4 and life_is_going:
                t *= 2
                pygame.time.set_timer(MYEVENTTYPE, t)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 5 and life_is_going:
                if t // 2 != 0:
                    t //= 2
                pygame.time.set_timer(MYEVENTTYPE, t)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    life_is_going = not life_is_going
            if event.type == MYEVENTTYPE and life_is_going:
                board.next_move()
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()
