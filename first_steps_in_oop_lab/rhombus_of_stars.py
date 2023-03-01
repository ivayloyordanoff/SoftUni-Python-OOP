def print_row():
    space = size - row - 1
    stars = row + 1

    print(" " * space + "* " * stars)


size = int(input())

for row in range(size):
    print_row()

for row in range(size - 2, -1, -1):
    print_row()
