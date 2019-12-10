def check_valid(code):
    for i in range(len(code) - 1):
        if code[i] == code[i + 1]:
            return True
    return False


def check_valid_second(code):
    runs = set()
    start_idx = 0
    current_check = code[0]
    for i in range(1, 6):
        if current_check != code[i]:
            runs.add(i - start_idx)
            current_check = code[i]
            start_idx = i
    runs.add(6 - start_idx)
    return 2 in runs


def first(checker_function):
    digits = [3, 5, 5, 5, 5, 5]

    valid_count = 0
    valids = list()
    while digits[0] < 8:
        if checker_function(digits):
            valid_count += 1
            valids.append(digits.copy())

        digits[5] += 1
        i = 5
        while digits[i] == 10:
            digits[i - 1] += 1
            i -= 1

        if i != 5:
            for k in range(i + 1, 6):
                digits[k] = digits[i]

    return valid_count, valids


if __name__ == "__main__":
    # print(first(check_valid))
    k, valid = first(check_valid)
    a = 0
    for item in valid:
        if check_valid_second(item):
            a += 1
            print(item)
    print(a)
    print(check_valid_second([7, 7, 7, 7, 7, 8]))