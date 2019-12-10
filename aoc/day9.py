from collections import deque, defaultdict


class IntcodeComputer:
    def __init__(self, program):
        self._program = defaultdict(int)
        for x, y in enumerate(program):
            self._program[x] = y
        self._pc = 0
        self._input_queue = deque()
        self._base = 0

    def _select_parameter(self, op_code, value):
        if op_code == 0:
            return self._program[value]
        if op_code == 1:
            return value
        if op_code == 2:
            return self._program[self._base + value]
        raise ValueError("Invalid parameter mode")

    def _select_position(self, op_code, value):
        if op_code == 0:
            return value
        if op_code == 2:
            return self._base + value
        raise ValueError("Invalid")

    def comp(self, input_stack: list):
        for item in input_stack:
            self._input_queue.append(item)
        while True:
            op_code = self._program[self._pc]
            if op_code == 99:
                return None

            elif op_code % 100 == 3:
                self._program[self._select_position(op_code // 100, self._program[self._pc + 1])] = self._input_queue.popleft()
                self._pc += 2
            elif op_code % 100 == 4:
                self._pc += 2
                return self._select_parameter(op_code // 100, self._program[self._pc - 1])

            elif op_code % 100 in [5, 6]:
                comp_val = self._select_parameter(op_code // 100 % 10, self._program[self._pc + 1])
                jump = self._select_parameter(op_code // 1000 % 10, self._program[self._pc + 2])
                if (comp_val and op_code & 1) or (not comp_val and op_code & 2):
                    self._pc = jump
                else:
                    self._pc += 3

            elif op_code % 100 == 9:
                self._base += self._select_parameter(op_code // 100, self._program[self._pc + 1])
                self._pc += 2

            else:
                a = self._select_position(op_code // 10000 % 10, self._program[self._pc + 3])

                op1 = self._select_parameter(op_code // 100 % 10, self._program[self._pc + 1])
                op2 = self._select_parameter(op_code // 1000 % 10, self._program[self._pc + 2])

                if op_code % 100 == 1:
                    self._program[a] = op1 + op2
                elif op_code % 100 == 2:
                    self._program[a] = op1 * op2
                elif op_code % 100 == 7:
                    self._program[a] = int(op1 < op2)
                elif op_code % 100 == 8:
                    self._program[a] = int(op1 == op2)
                else:
                    msg = f"i = {self._pc}"
                    raise ValueError(msg)

                self._pc += 4

        raise ValueError("Out of loop without exit")


if __name__ == "__main__":
    with open("data9.txt") as data:
        k = IntcodeComputer([int(x) for x in data.read().strip().split(",")])
        val = k.comp([2])
        while val is not None:
            print(val)
            val = k.comp([])
        print(val)
