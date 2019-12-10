
def first():
    with open("data1.txt") as data:
        value = 0
        for line in data:
            num = int(line)
            value += num // 3 - 2

        print(value)


def second():
    with open("data2.txt") as data:
        value = 0
        for line in data:

            temp = int(line)
            while temp > 8:
                temp = temp // 3 - 2
                value += temp

        print(value)


if __name__ == "__main__":
    first()
    second()
