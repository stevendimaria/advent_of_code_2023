from utils.utilities import AOCUtils

UTILS = AOCUtils(get_env=True)


class Day3:
    def __init__(self, day: int = 3):
        self.engine_schematic = UTILS.get_input_by_line(day)
        self.line_len = len(self.engine_schematic[0])
        self.length = len(self.engine_schematic)
        self.nums = {}
        self.num_indices = {}
        self.skip = {".", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        self.star1_ans = 0
        self.star2_ans = 0

    def get_nums(self):
        def get_num(num_str):
            _num = ""
            for ch in num_str:
                if ch.isdigit():
                    _num += ch
                else:
                    break

            return _num

        r, c = 0, 0
        while r < self.length:
            if self.engine_schematic[r][c].isdigit():
                num = get_num(self.engine_schematic[r][c:])
                self.nums[(c, c + len(num), r)] = int(num)

                for i in range(c, c + len(num)):
                    if self.engine_schematic[r][i].isdigit():
                        self.num_indices[(r, i)] = int(num)

                c += len(num)
            else:
                c += 1

            if c == self.line_len:
                r, c = r + 1, 0

    def check_adjacent(self, start_x: int, end_x: int, y_idx: int) -> bool:
        if start_x > 0 and self.engine_schematic[y_idx][start_x - 1] not in self.skip:
            return True
        if (
            end_x != self.line_len - 1
            and self.engine_schematic[y_idx][end_x] not in self.skip
        ):
            return True
        if y_idx > 0:
            if set(self.engine_schematic[y_idx - 1][start_x:end_x]) - self.skip:
                return True
            elif (
                start_x > 0
                and self.engine_schematic[y_idx - 1][start_x - 1] not in self.skip
            ):
                return True
            elif (
                end_x < self.line_len - 1
                and self.engine_schematic[y_idx - 1][end_x] not in self.skip
            ):
                return True
        if y_idx < self.length - 1:
            if set(self.engine_schematic[y_idx + 1][start_x:end_x]) - self.skip:
                return True
            elif (
                start_x > 0
                and self.engine_schematic[y_idx + 1][start_x - 1] not in self.skip
            ):
                return True
            elif (
                end_x < self.line_len - 1
                and self.engine_schematic[y_idx + 1][end_x] not in self.skip
            ):
                return True

        return False

    def star1(self):
        self.get_nums()

        for k, v in self.nums.items():
            if self.check_adjacent(*k):
                self.star1_ans += v

        print(f"Day 3, Star 1 Answer: {self.star1_ans}")
        return self.star1_ans

    def star2(self):
        for r in range(self.length):
            for c in range(self.line_len):
                if self.engine_schematic[r][c] == "*":
                    adj_digits = set()

                    if c > 0 and self.engine_schematic[r][c - 1].isdigit():
                        adj_digits |= {(r, c - 1)}
                    if (
                        c < self.line_len - 1
                        and self.engine_schematic[r][c + 1].isdigit()
                    ):
                        adj_digits |= {(r, c + 1)}
                    if r > 0:
                        above_set = set()

                        if c > 0 and self.engine_schematic[r - 1][c - 1].isdigit():
                            above_set |= {(r - 1, c - 1)}
                        if self.engine_schematic[r - 1][c].isdigit():
                            above_set |= {(r - 1, c)}
                        if (
                            c < self.line_len - 1
                            and self.engine_schematic[r - 1][c + 1].isdigit()
                        ):
                            above_set |= {(r - 1, c + 1)}

                        if len(above_set) == 3 or len(above_set) == 1:
                            adj_digits |= {above_set.pop()}
                        elif len(above_set) == 2:
                            if self.engine_schematic[r - 1][c].isdigit():
                                adj_digits |= {above_set.pop()}
                            else:
                                adj_digits |= above_set
                        else:
                            pass

                    if r < self.length - 1:
                        below_set = set()

                        if c > 0 and self.engine_schematic[r + 1][c - 1].isdigit():
                            below_set |= {(r + 1, c - 1)}
                        if self.engine_schematic[r + 1][c].isdigit():
                            below_set |= {(r + 1, c)}
                        if (
                            c < self.line_len - 1
                            and self.engine_schematic[r + 1][c + 1].isdigit()
                        ):
                            below_set |= {(r + 1, c + 1)}

                        if len(below_set) == 3 or len(below_set) == 1:
                            adj_digits |= {below_set.pop()}
                        elif len(below_set) == 2:
                            if self.engine_schematic[r + 1][c].isdigit():
                                adj_digits |= {below_set.pop()}
                            else:
                                adj_digits |= below_set
                        else:
                            pass

                    if len(adj_digits) == 2:
                        c1, c2 = adj_digits.pop(), adj_digits.pop()
                        self.star2_ans += self.num_indices[c1] * self.num_indices[c2]

        print(f"Day 3, Star 2 Answer: {self.star2_ans}")
        return self.star2_ans


if __name__ == "__main__":
    day3 = Day3()
    day3.star1()  # 527144
    day3.star2()  # 81463996
