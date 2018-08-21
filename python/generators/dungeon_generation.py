import random
from copy import deepcopy

map_config = {
    "width": 60,
    "height": 40,
    "avg_room_size": "normal",
    "tries": 150,
    "allow_overlap": False,
    "overlap_ratio": 10
}


class DungeonGenerator(object):
    """ generate random square dungeons with possible encounters treasures discriptions etc """

    ROOM_SIZES = ["tiny", "small", "normal", "large", "huge"]
    EMPTY_TILE = {"type": None, "objects": []}

    def __init__(self, map_config):
        # map generation config
        self.width = map_config['width']                        # map width in squares
        self.height = map_config['height']                      # map height in squares
        self.avg_room_size = map_config['avg_room_size']        # average room size
        self.tries = map_config['tries']                        # the higher the more dense dungeon you get
        self.allow_overlap = map_config['allow_overlap']        # allow rooms to over lap (non square rooms)
        self.overlap_ratio = map_config['overlap_ratio']        # the higher the moor room overlap there is
        self.room_sizes = self.get_room_sizes()
        self.empty_grid = self.empty_grid()

        # contents generation config (styling, objects)

        # CR generation config (monsters/traps/bosses

    def generate_dungeon(self):
        dungeon = self.add_rooms_to_grid(deepcopy(self.empty_grid))
        return dungeon

    def empty_grid(self):
        """ returns an empty grid layout for dungeon """
        grid = []
        for i in range(self.height):
            grid.append([deepcopy(self.EMPTY_TILE) for n in range(self.width)])

        return grid

    def get_room_sizes(self):
        idx = self.ROOM_SIZES.index(self.avg_room_size)
        min_size = min(idx - 2, 0)
        max_size = max(idx + 2, len(self.ROOM_SIZES) - 1)
        sizes = []

        for i, v in enumerate(range(min_size, max_size)):
            # since we work with index we need to convert it to room size
            size = (v + 2) * 2 + 2
            sizes += [size]

        return sizes

    def get_random_room_size(self):
        """
        Get a random room size based on most wanted size
        :param r_size: a room_size from ROOM_SIZES
        :return: x*y room size
        """

        avg = random.choice(self.room_sizes)
        s1 = random.randint(avg - 2, avg + 2)
        s2 = random.randint(random.randint(avg - 2, avg), random.randint(avg, avg + 2))
        return random.randint(*sorted([s1, s2])), random.randint(*sorted([s1, s2]))

    def add_rooms_to_grid(self, grid):
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

        def add_room_floors(grid):
            for y in range(pos_y, pos_y + room_y - 1):
                for x in range(pos_x, pos_x + room_x - 1):
                    grid[y][x]['type'] = 'floor'

            return grid

        def get_max_overlaps():
            if not rooms:
                return 0
            elif rooms and overlaps:
                return int(rooms * self.overlap_ratio / overlaps / 10) + 1
            return 1

        # add rooms to layout
        rooms = 0
        overlaps = 0
        for i in range(self.tries):
            max_overlaps = get_max_overlaps()
            room_x, room_y = self.get_random_room_size()

            # get random top left corner of room (map borders should always be wall)
            min_x, max_x = 2, self.width - (room_x + 1)
            min_y, max_y = 2, self.height - (room_y + 1)
            pos_x, pos_y = random.randint(min_x, max_x), random.randint(min_y, max_y)

            if find_overlap(grid):
                if self.allow_overlap:
                    if max_overlaps <= overlaps or random.randint(1, 100) > self.overlap_ratio:
                        continue
                    else:
                        overlaps += 1
                else:
                    continue

            # add room to grid
            rooms += 1
            grid = add_room_floors(grid)

        return grid

    def show_grid(self, grid):
        """ for debug purposes (gives a fasty estimation of its looks """
        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append("X " if grid[y][x]['type'] == 'floor' else "  ")
            print(''.join(row))
