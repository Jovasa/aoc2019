from typing import Dict


class CelestialBody:
    def __init__(self, name: str):
        self._children = set()
        self.name = name
        self.parent = None

    def __iadd__(self, other: 'CelestialBody'):
        self._children.add(other)
        other.parent = self
        return self

    @property
    def children_count(self) -> int:
        if not self._children:
            return 0

        else:
            count = 0
            for child in self._children:
                count += child.children_count + 1
            return count

    @property
    def neighbors(self) -> set('CelestialBody'):
        temp = self._children.copy()
        if self.parent:
            temp.add(self.parent)
        return temp

    def count_distance_breadth(self, other: 'CelestialBody') -> int:
        to_be_tested = self._children.copy()
        to_be_tested.add(self.parent)
        already_tested = {self}
        distance = -1  # Based on how the question is laid we cannot be orbiting the other objcet
        while other not in to_be_tested:
            already_tested.update(to_be_tested)
            temp = set()
            for item in to_be_tested:
                temp.update(item.neighbors)
            temp -= already_tested
            to_be_tested = temp
            distance += 1

        return distance

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


def parse_file(file_name) -> Dict[str, 'CelestialBody']:
    data_out = dict()
    with open(file_name) as input_f:
        for row in input_f:
            objects = row.strip().split(")")

            center = objects[0]
            orbiter = objects[1]

            if center not in data_out:
                data_out[center] = CelestialBody(center)
            if orbiter not in data_out:
                data_out[orbiter] = CelestialBody(orbiter)

            data_out[center] += (data_out[orbiter])

    return data_out


if __name__ == "__main__":
    data = parse_file("data6.txt")
    print(sum([body.children_count for body in data.values()]))
    print(data["YOU"].count_distance_breadth(data["SAN"]))
    print(data["SAN"].count_distance_breadth(data["YOU"]))
