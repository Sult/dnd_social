import random
from copy import deepcopy

ROOM_SIZES = ["tiny", "small", "normal", "large", "huge"]


tile = {
    "type": None,
    "objects": []
}


# settings
width = 80
height = 45
r_size = "normal"
tries = 50     # the higher the more dense dungeon you get

# Create empty room layout
grid = []
for i in range(height):
    row = []
    for n in range(width):
        row.append(deepcopy(tile))
    grid.append(row)


def get_random_room_size(r_size: str) -> tuple:
    """
    Get a random room size based on most wanted size
    :param r_size: a room_size from ROOM_SIZES
    :return: x*y room size
    """

    def get_weigths(n, k):
        if k in (0, n):
            return 1
        return get_weigths(n - 1, k - 1) + get_weigths(n - 1, k)

    # setup weigthed list of room sizes
    if not get_random_room_size.sizes:
        idx = ROOM_SIZES.index(r_size)
        min_size = min(idx - 2, 0)
        max_size = max(idx + 2, len(ROOM_SIZES) - 1)
        sizes = []
        # weights = [get_weigths(max_size - min_size, k) for k in range(min_size, max_size)]
        for i, v in enumerate(range(min_size, max_size)):
            # since we work with index we need to convert it to room size
            size = (v + 2) * 2 + 2
            sizes += [size] #  * weights[i]      # add weights

        get_random_room_size.sizes = sizes

    # get a random size
    avg = random.choice(get_random_room_size.sizes)
    s1 = random.randint(random.randint(avg - 2, avg), random.randint(avg, avg + 2))
    s2 = random.randint(random.randint(avg - 2, avg), random.randint(avg, avg + 2))
    return random.randint(*sorted([s1, s2])), random.randint(*sorted([s1, s2]))

get_random_room_size.sizes = []


def fill_grid_with_rooms(tries, grid, width, heigth):
    """
    fills a layout with random room sizes for x-tries
    A room is always surrounded by walls (width 1)
    :param tries: times to try to fit a room inside layout
    :param grid: the map grid
    :return: grid filled with rooms and walls
    """

    def find_overlap(grid):
        # find if there is room overlap on grid
        for y in range(pos_y - 1, pos_y + room_y):
            grid_row = grid[y]
            for x in range(pos_x - 1, pos_x + room_x):
                if grid_row[x]['type'] == 'floor':
                    return True
        return False

    def add_room_walls(grid):
        # add top/bottom wall
        top = pos_y - 1
        bottom = pos_y + room_y
        for x in range(pos_x - 1, pos_x + room_x):
            grid[top][x]['type'] = 'wall'
            grid[bottom][x]['type'] = 'wall'

        # add side walls
        left = pos_x - 1
        right = pos_x + room_x + 1
        for y in range(pos_y - 1, pos_y + room_y):
            grid[y][left]['type'] = 'wall'
            grid[y][right]['type'] = 'wall'
        return grid

    def add_room_floors(grid):
        for y in range(pos_y, pos_y + room_y - 1):
            for x in range(pos_x, pos_x + room_x - 1):
                grid[y][x]['type'] = 'floor'
        return grid

    # add rooms to layout
    for i in range(tries):
        room_x, room_y = get_random_room_size(r_size)

        # get random top left corner of room (map borders should always be wall)
        min_x, max_x = 2, width - (room_x + 1)
        min_y, max_y = 2, heigth - (room_y + 1)
        pos_x, pos_y = random.randint(min_x, max_x), random.randint(min_y, max_y)

        if find_overlap(grid):
            # rooms are overlapping, continue to next try
            continue

        # add room to grid
        # FIXME: add wall already in find overlap, and if wall is found, return original before adding room
        # grid = add_room_walls(grid)
        grid = add_room_floors(grid)

    return grid


def show_grid(grid):
    for y in range(height):
        row = []
        for x in range(width):
            row.append("X " if grid[y][x]['type'] == 'floor' else "  ")
        print(''.join(row))