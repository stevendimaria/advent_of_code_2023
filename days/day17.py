import math

from heapq import heappush, heappop

from utils.utilities import AOCUtils

UTILS = AOCUtils(get_env=True)


class Day17:
    def __init__(self, day: int = 17):
        self.blocks = UTILS.get_input_by_line(day, strip=True)
        self.cache = {}

        self.star1_ans = math.inf
        self.star2_ans = math.inf

    def move_crucible(self, start, min_mv, max_mv):
        h, seen, ans = [], set(), math.inf
        heappush(h, (int(self.blocks[0][0]) * -1, 0, 0, 0, "R"))

        while h:
            tot, r, c, st, d = heappop(h)

            if (
                not 0 <= r < len(self.blocks)
                or not 0 <= c < len(self.blocks[0])
                or (r, c, d, st) in seen
                or tot >= ans
            ):
                continue

            tot += int(self.blocks[r][c])
            if r == int(len(self.blocks)) - 1 and c == int(len(self.blocks[0])) - 1:
                if st >= min_mv:
                    ans = min(ans, tot)
                    continue

            seen.add((r, c, d, st))

            if d == "D" and st < max_mv:
                heappush(h, (tot, r + 1, c, st + 1, "D"))
            elif d in {"R", "L"} and st >= min_mv:
                heappush(h, (tot, r + 1, c, 1, "D"))

            if d == "U" and st < max_mv:
                heappush(h, (tot, r - 1, c, st + 1, "U"))
            elif d in {"R", "L"} and st >= min_mv:
                heappush(h, (tot, r - 1, c, 1, "U"))

            if d == "R" and st < max_mv:
                heappush(h, (tot, r, c + 1, st + 1, "R"))
            elif d in {"U", "D"} and st >= min_mv:
                heappush(h, (tot, r, c + 1, 1, "R"))

            if d == "L" and st < max_mv:
                heappush(h, (tot, r, c - 1, st + 1, "L"))
            elif d in {"U", "D"} and st >= min_mv:
                heappush(h, (tot, r, c - 1, 1, "L"))

        return ans

    def star1(self):
        self.star1_ans = self.move_crucible(
            (int(self.blocks[0][0]) * -1, 0, 0, 0, "R"), 1, 3
        )
        print(f"Day 17, Star 1 Answer: {self.star1_ans}")
        return self.star1_ans

    def star2(self):
        self.star2_ans = self.move_crucible(
            (int(self.blocks[0][0]) * -1, 0, 0, 0, "R"), 4, 10
        )
        print(f"Day 17, Star 2 Answer: {self.star2_ans}")
        return self.star2_ans


if __name__ == "__main__":
    day17 = Day17()
    day17.star1()  # 861
    day17.star2()  # 1037
