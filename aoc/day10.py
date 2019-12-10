from collections import defaultdict
from math import gcd, atan, pi


def get_asteroid_locations(data: str) -> (set, int, int):
    lines = data.split("\n")
    out = set()
    for y, line in enumerate(lines):
        for x, obj in enumerate(line):
            if obj == "#":
                out.add((x, y))

    return out, x + 1, y + 1


def check_visible(asteroids, asteroid,  visible, not_visible):
    for other in asteroids:
        if other == asteroid or other in visible[asteroid] or other in not_visible[asteroid]:
            continue

        x_diff = asteroid[0] - other[0]
        y_diff = asteroid[1] - other[1]
        x = gcd(x_diff, y_diff)

        x_diff //= x
        y_diff //= x

        can_see = True
        for i in range(1, x):
            if (asteroid[0] - x_diff * i, asteroid[1] - y_diff * i) in asteroids:
                not_visible[asteroid].add(other)
                not_visible[other].add(asteroid)
                can_see = False
                break

        if can_see:
            visible[asteroid].add(other)
            visible[other].add(asteroid)


if __name__ == "__main__":
    with open("data10.txt") as d:
        k, max_x, max_y = get_asteroid_locations(d.read())
        visible = defaultdict(set)
        not_visible = defaultdict(set)
        for item in list(k):
            check_visible(k, item, visible, not_visible)

        temp = max(visible, key=lambda x: len(visible[x]))

        visible_to_best = visible[temp]
        print(temp, len(visible_to_best))

        angles = dict()
        for item in visible_to_best:
            x_di = item[0] - temp[0]
            y_di = temp[1] - item[1]
            if x_di == 0:
                angles[item] = atan(float('inf') * y_di)
            else:
                t = atan(abs(y_di/x_di))
                if y_di*x_di < 0:
                    t = -t

                if x_di < 0:
                    t -= pi

                angles[item] = t

        print(sorted(angles.items(), key=lambda x: x[1], reverse=True)[199])
