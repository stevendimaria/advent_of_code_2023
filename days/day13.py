from utils.utilities import AOCUtils

UTILS = AOCUtils(get_env=True)


class Day13:
    def __init__(self, day: int = 13):
        inp = UTILS.get_input_by_line(day)

        self.patterns = [[]]
        for li in inp:
            if li == "\n":
                self.patterns.append([])
            else:
                self.patterns[-1].append(li.strip())

        self.star1_ans = 0
        self.star2_ans = 0

    def transpose(self, pattern):
        out = [[] for _ in range(len(pattern[0]))]
        for pat in pattern:
            for i, ch in enumerate(pat):
                out[i].append(ch)

        return ["".join(o) for o in out]

    def get_symmetrical(self, pattern, tol):
        def check_same(li1, li2):
            return sum(x != y for x, y in zip(li1, li2)) <= tol

        ans = 0
        for i in range(len(pattern) - 1):
            rng = range(min(i + 1, len(pattern) - 1 - i))
            if all(check_same(pattern[i - j], pattern[i + j + 1]) for j in rng):
                ans += i + 1
        return ans

    def star1(self):
        h, v = 0, 0

        for pattern in self.patterns:
            h += self.get_symmetrical(pattern, 0) * 100
            v += self.get_symmetrical(self.transpose(pattern), 0)

        self.star1_ans = h + v
        print(f"Day 13, Star 1 Answer: {self.star1_ans}")
        return self.star1_ans

    def star2(self):
        h, v = 0, 0

        for pattern in self.patterns:
            h += self.get_symmetrical(pattern, 1) * 100
            v += self.get_symmetrical(self.transpose(pattern), 1)

        self.star2_ans = h + v - self.star1_ans
        print(f"Day 13, Star 2 Answer: {self.star2_ans}")
        return self.star2_ans


if __name__ == "__main__":
    day13 = Day13()
    day13.star1()  # 28651
    day13.star2()  # 25450
