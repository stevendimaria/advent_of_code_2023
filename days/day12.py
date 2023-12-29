from functools import lru_cache

from utils.utilities import AOCUtils

UTILS = AOCUtils(get_env=True)


class Day12:
    def __init__(self, day: int = 12):
        inp = UTILS.get_input_by_line(day)

        self.directions = [x.strip() for x in inp]
        self.springs = []
        self.num_springs = []

        self.star1_ans = 0
        self.star2_ans = 0

        for l in self.directions:
            spr, n_spr = l.split()
            self.springs.append(spr)
            self.num_springs.append([int(n) for n in n_spr.split(",")])

    @lru_cache(maxsize=None)
    def get_combos(self, spring: str):
        if "?" not in spring:
            return [spring]

        pre, post = spring.split("?", 1)
        return self.get_combos(pre + "." + post) + self.get_combos(pre + "#" + post)

    def star1(self):
        for i, spring in enumerate(self.springs):
            ans = 0
            combos = self.get_combos(spring)
            for c in combos:
                c = [len(x) for x in c.split(".") if x]
                if c == self.num_springs[i]:
                    ans += 1
            self.star1_ans += ans

        print(f"Day 12, Star 1 Answer: {self.star1_ans}")
        return self.star1_ans


if __name__ == "__main__":
    day12 = Day12()
    day12.star1()  # 7857
    # day12.star2()
