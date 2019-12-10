from collections import defaultdict
from math import gcd


def get_asteroid_locations(data: str) -> (set, int, int):
    lines = data.split("\n")
    out = set()
    for y, line in enumerate(lines):
        for x, obj in enumerate(line):
            if obj == "#":
                out.add((x, y))

    return out, x + 1, y + 1


def check_visible(visible, not_visible):
    global x
    for other in k:
        if other == item or other in visible[item] or other in not_visible[item]:
            continue

        x_diff = item[0] - other[0]
        y_diff = item[1] - other[1]
        x = gcd(x_diff, y_diff)

        x_diff //= x
        y_diff //= x

        can_see = True
        for i in range(1, x):
            if (item[0] - x_diff * i, item[1] - y_diff * i) in k:
                not_visible[item].add(other)
                not_visible[other].add(item)
                can_see = False
                break

        if can_see:
            visible[item].add(other)
            visible[other].add(item)


if __name__ == "__main__":
    with open("data10.txt") as d:
        k, max_x, max_y = get_asteroid_locations(d.read())
        visible = defaultdict(set)
        not_visible = defaultdict(set)
        for item in list(k):
            check_visible(visible, not_visible)

        temp = max(visible, key=lambda x: len(visible[x]))

        for x in range(max_x):
            pass

        print(temp, len(visible[temp]), max_x, max_y)
