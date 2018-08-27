import random


class GrowingTree(object):
    """ Growing tree maze generation prepared to work from a generator grid """

    def __init__(self, grid):
        """
        # the grid of the maze
        # each cell of the maze is one of the following:
        # '#' is wall
        # '.' is empty space
        # ',' is exposed but undetermined
        # '?' is unexposed and undetermined
        """

        self.grid = grid
        self.width = len(self.grid[0])
        self.height = len(self.grid)
        self.frontier = []

    def create_hallways(self):
        """ fill grid with pathways betwene rooms """

        # choose a original point
        xchoice = random.randint(0, self.width - 1)
        ychoice = random.randint(0, self.height - 1)
        self.carve(ychoice, xchoice)

    def carve(self, y, x):
        """
        Make the cell at y,x a space.

        Update the frontier and self.grid accordingly.
        Note: this does not remove the current cell from frontier, it only adds new cells.
        """

        extra = []
        # self.grid[y][x] = '.'
        if x > 0:
            if self.grid[y][x - 1] == '?':
                self.grid[y][x - 1] = ','
                extra.append((y, x - 1))
        if x < self.width - 1:
            if self.grid[y][x + 1] == '?':
                self.grid[y][x + 1] = ','
                extra.append((y, x + 1))
        if y > 0:
            if self.grid[y - 1][x] == '?':
                self.grid[y - 1][x] = ','
                extra.append((y - 1, x))
        if y < self.height - 1:
            if self.grid[y + 1][x] == '?':
                self.grid[y + 1][x] = ','
                extra.append((y + 1, x))
        random.shuffle(extra)
        self.frontier.extend(extra)

    def harden(self, y, x):
        """ Make the cell at y,x a wall. """

        self.grid[y][x] = '#'

    def check(self, y, x, nodiagonals=True):
        """Test the cell at y,x: can this cell become a space?

        True indicates it should become a space,
        False indicates it should become a wall.
        """

        edgestate = 0
        if x > 0:
            if self.grid[y][x - 1] == '.':
                edgestate += 1
        if x < xwide - 1:
            if self.grid[y][x + 1] == '.':
                edgestate += 2
        if y > 0:
            if self.grid[y - 1][x] == '.':
                edgestate += 4
        if y < yhigh - 1:
            if self.grid[y + 1][x] == '.':
                edgestate += 8

        if nodiagonals:
            # if this would make a diagonal connecition, forbid it
            # the following steps make the test a bit more complicated and are not necessary,
            # but without them the mazes don't look as good
            if edgestate == 1:
                if x < xwide - 1:
                    if y > 0:
                        if self.grid[y - 1][x + 1] == '.':
                            return False
                    if y < yhigh - 1:
                        if self.grid[y + 1][x + 1] == '.':
                            return False
                return True
            elif edgestate == 2:
                if x > 0:
                    if y > 0:
                        if self.grid[y - 1][x - 1] == '.':
                            return False
                    if y < yhigh - 1:
                        if self.grid[y + 1][x - 1] == '.':
                            return False
                return True
            elif edgestate == 4:
                if y < yhigh - 1:
                    if x > 0:
                        if self.grid[y + 1][x - 1] == '.':
                            return False
                    if x < xwide - 1:
                        if self.grid[y + 1][x + 1] == '.':
                            return False
                return True
            elif edgestate == 8:
                if y > 0:
                    if x > 0:
                        if self.grid[y - 1][x - 1] == '.':
                            return False
                    if x < xwide - 1:
                        if self.grid[y - 1][x + 1] == '.':
                            return False
                return True
            return False
        else:
            # diagonal walls are permitted
            if [1, 2, 4, 8].count(edgestate):
                return True
            return False