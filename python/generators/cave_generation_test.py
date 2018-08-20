# roughly based on http://noelberry.ca/#thecaves
from random import randint
from copy import copy

height = 30     # squares
width = 20      # squares

# create a full filled map
layout = []
empty_object = {
    "solid": True,
}
for i in range(height):
    row = []
    for n in range(width):
        row.append(copy(empty_object))
    layout.append(row)

# miners dig out space in layout (start random around center)
x = randint(randint(0, width / 2), randint(width / 2, width))
y = randint(randint(0, height / 2), randint(height / 2, height))

miners = [{"x": x, "y": y}]




