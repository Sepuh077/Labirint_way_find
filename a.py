import random

maze_w = 50
maze_h = 50
way = []
possible_way = []
wrong_way = []

def not_touch_way(pos, previous_pos):
    cx, cy = pos
    if [cx - 1, cy] in way and cx - 1 != previous_pos[0] and cy != previous_pos[1]:
        return False
    if [cx + 1, cy] in way and cx + 1 != previous_pos[0] and cy != previous_pos[1]:
        return False
    if [cx, cy + 1] in way and cx != previous_pos[0] and cy + 1 != previous_pos[1]:
        return False
    if [cx, cy - 1] in way and cx != previous_pos[0] and cy - 1 != previous_pos[1]:
        return False

    return True



def create_way():
    x, y = 0, 0
    i = 0
    way.append([0, 0])
    while True:
        if (x == maze_w - 2 and y == maze_h - 1) or (x == maze_w-1 and y == maze_h - 2):
            x, y = maze_w - 1, maze_h - 1
            way.append([x, y])
        if x == maze_w - 1 and y == maze_h - 1:
            break
        
        possible_way.clear()
        if x > 0 and [x - 1, y] not in wrong_way and not_touch_way((x - 1, y), [x, y]) and [x - 1, y] not in way:
            possible_way.append([x - 1, y])
        if y < maze_h - 1 and [x, y + 1] not in wrong_way and not_touch_way((x, y + 1), [x, y]) and [x, y + 1] not in way:
            possible_way.append([x, y + 1])
        if x < maze_w - 1 and [x + 1, y] not in wrong_way and not_touch_way((x + 1, y), [x, y]) and [x + 1, y] not in way:
            possible_way.append([x + 1, y])
        if y > 0 and [x, y - 1] not in wrong_way and not_touch_way((x, y - 1), [x, y]) and [x, y - 1] not in way:
            possible_way.append([x, y - 1])

        if possible_way.__len__() == 0:
            wrong_way.append([x, y])
            way.remove([x, y])
            x, y = way[way.__len__() - 1][0], way[way.__len__() - 1][1]
        else:
            num = random.randint(0, possible_way.__len__() - 1)
            x = possible_way[num][0]
            y = possible_way[num][1]
            way.append([x, y])

        i += 1

create_way()

for i in range(maze_w):
    for j in range(maze_h):
        if [i, j] in way:
            print("#", end=" ")
        else:
            print(".", end=" ")

    print()

