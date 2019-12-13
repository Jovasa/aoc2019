import re
from math import gcd


def lcm(x, y):
    return x * y // gcd(x, y)


class Moon:
    def __init__(self, vector, name):
        self.position = vector.copy()
        self.velocity = [0, 0, 0]
        self.name = name

    def update_velocity(self, others):
        for other in others:
            if other is self:
                continue
            for dimension in range(3):
                if other.position[dimension] > self.position[dimension]:
                    self.velocity[dimension] += 1
                elif other.position[dimension] < self.position[dimension]:
                    self.velocity[dimension] -= 1

    def move(self):
        for i in range(3):
            self.position[i] += self.velocity[i]

    @property
    def energy(self):
        return sum([abs(x) for x in self.velocity]) * sum([abs(x) for x in self.position])

    def __repr__(self):
        return f"{self.position} {self.velocity}"


def main():
    moons = list()
    with open("data12.txt") as data:
        for line, name in zip(data, [1, 2, 3, 4]):
            a = re.search(r"x=(-?\d+), y=(-?\d+), z=(-?\d+)", line)
            moons.append(Moon([int(x) for x in a.groups()], name))

    velocities = [0, 0, 0]
    i = 0
    while not all(velocities):
        i += 1
        for moon in moons:
            moon.update_velocity(moons)
        for moon in moons:
            moon.move()

        for j in range(3):
            all_zeros = True
            for moon in moons:
                if moon.velocity[j] != 0:
                    all_zeros = False

            if all_zeros and velocities[j] == 0:
                velocities[j] = i

    print(velocities)

    print(lcm(lcm(velocities[0], velocities[1]), velocities[2]) * 2)

    energy = 0
    for moon in moons:
        energy += moon.energy
    print(energy)



if __name__ == "__main__":
    main()