import random as rnd
from shutil import move

maze = []
W, H = 40, 20


def factory(w, h):
    maze = []
    for _ in range(h):
        row = []
        for _ in range(w):
            row.append("▓▓")
        maze.append(row)
    return maze


def show(maze, w, h):
    for r in range(h):
        for c in range(w):
            print(maze[r][c], end="")
        print()


def fix(k, max):
    if k <= 0:
        k = 1
    if k >= max:
        k = max - 2
    return k


def random_direction():
    return rnd.choices([0, 1, 2, 3], k=1, weights=[0.50, 0.2, 0.2, 0.1])[0]


def mover(maze, w, h, ch, echo=True):
    x, y = 1, rnd.randrange(0, H)
    maze[y][x] = ch

    D = {0: (1, 0), 1: (0, 1), 2: (0, -1), 3: (-1, 0)}  # Direction
    d = 0

    counter = 0
    while True:
        if rnd.random() < 0.50:  # Change turn
            d = random_direction()
        x += D[d][0]
        y += D[d][1]

        x = fix(x, W)
        y = fix(y, H)

        if maze[y][x] == ch and counter < 1000:
            counter += 1
            # print(counter)
            d = random_direction()
            continue
        counter = 0

        maze[y][x] = ch

        if echo:
            print()
            print()
            show(maze, w, h)

        if x >= W - 2:  # or y>=H-2:
            break


if __name__ == "__main__":
    maze = factory(W, H)
    show(maze, W, H)

    for _ in range(4):
        mover(maze, W, H, "  ", False)

    print()
    show(maze, W, H)

"""
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                          ▓▓                    ▓▓▓▓▓▓
▓▓                          ▓▓▓▓▓▓▓▓▓▓▓▓          ▓▓    ▓▓    ▓▓    ▓▓▓▓      ▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓  ▓▓▓▓  ▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓        ▓▓▓▓▓▓            ▓▓
▓▓▓▓▓▓          ▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓      ▓▓▓▓▓▓▓▓▓▓      ▓▓▓▓  ▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓
▓▓        ▓▓        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓      ▓▓▓▓  ▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓
▓▓▓▓  ▓▓  ▓▓      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓          ▓▓▓▓▓▓▓▓
▓▓▓▓  ▓▓  ▓▓    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓  ▓▓▓▓▓▓▓▓
▓▓        ▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓      ▓▓▓▓  ▓▓▓▓▓▓▓▓
▓▓    ▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓      ▓▓▓▓
▓▓                  ▓▓▓▓▓▓  ▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓
▓▓    ▓▓▓▓▓▓    ▓▓  ▓▓                                        ▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓
▓▓▓▓▓▓▓▓▓▓      ▓▓          ▓▓              ▓▓▓▓              ▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓
▓▓▓▓▓▓▓▓              ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓    ▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓          ▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                    ▓▓      ▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓              ▓▓        ▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                      ▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
"""