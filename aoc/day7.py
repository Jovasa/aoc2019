from itertools import permutations

from aoc.day9 import IntcodeComputer


def find_best():
    with open("data7.txt") as data:
        prog = [int(x) for x in data.read().split(",")]

        best = 0
        for item in permutations([0, 1, 2, 3, 4]):
            print(item)

            comp_inp = 0
            for phase_setting in item:
                a = IntcodeComputer(prog)
                comp_inp = a.comp([phase_setting, comp_inp])

            best = max(comp_inp, best)

        print(best)


def find_best_feedback():
    with open("data7.txt") as data:
        program = [int(x) for x in data.read().split(",")]
        best = 0
        for phases in permutations([5, 6, 7, 8, 9]):
            programs = [IntcodeComputer(program) for _ in range(5)]
            inputs = [[phases[i], 0] for i in range(5)]
            finished = False
            latest = 0
            while not finished:
                for i in range(5):
                    a = programs[i].comp(inputs[i])
                    if not a:
                        finished = True
                        break
                    temp = a
                    if i == 4:
                        latest = temp
                    if not latest:
                        inputs[(i + 1) % 5][1] = temp
                    else:
                        inputs[(i + 1) % 5] = [temp]
            best = max(best, latest)
        print(best)


if __name__ == "__main__":
    find_best_feedback()
