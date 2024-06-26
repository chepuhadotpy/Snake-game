import curses
import random

def main(stdscr):
    # Инициализация библиотеки curses
    curses.curs_set(0)
    sh, sw = stdscr.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(1)
    w.timeout(100)

    # Начальная позиция змейки и еды
    snk_x = sw // 4
    snk_y = sh // 2
    snake = [
        [snk_y, snk_x],
        [snk_y, snk_x - 1],
        [snk_y, snk_x - 2]
    ]

    food = [sh // 2, sw // 2]
    w.addch(int(food[0]), int(food[1]), curses.ACS_PI)

    # Начальное направление движения змейки
    key = curses.KEY_RIGHT

    while True:
        next_key = w.getch()
        key = key if next_key == -1 else next_key

        # Определение следующей позиции головы змейки
        new_head = [snake[0][0], snake[0][1]]

        if key == curses.KEY_DOWN:
            new_head[0] += 1
        if key == curses.KEY_UP:
            new_head[0] -= 1
        if key == curses.KEY_LEFT:
            new_head[1] -= 1
        if key == curses.KEY_RIGHT:
            new_head[1] += 1

        # Проверяем, что змейка не съела саму себя или не ударилась о стены
        if (new_head[0] in [0, sh-1] or
            new_head[1] in [0, sw-1] or
            new_head in snake):
            curses.endwin()
            quit()

        # Добавляем новую голову змейки
        snake.insert(0, new_head)

        # Проверяем, что змейка съела еду
        if snake[0] == food:
            food = None
            while food is None:
                nf = [
                    random.randint(1, sh - 2),
                    random.randint(1, sw - 2)
                ]
                food = nf if nf not in snake else None
            w.addch(food[0], food[1], curses.ACS_PI)
        else:
            # Удаляем хвост, если еда не была съедена
            tail = snake.pop()
            w.addch(int(tail[0]), int(tail[1]), ' ')

        # Отображаем голову змейки
        w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)

if __name__ == "__main__":
    curses.wrapper(main)

