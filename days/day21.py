from collections import deque

from utils.utilities import AOCUtils

UTILS = AOCUtils(get_env=True)


class Day21:
    def __init__(self, day: int = 21):
        self.map = UTILS.get_input_by_line(day, strip=True)
        self.start = None
        self.hi_x = len(self.map[0])
        self.hi_y = len(self.map)

        for i, row in enumerate(self.map):
            for j, col in enumerate(row):
                if self.map[i][j] == "S":
                    self.start = (i, j)
                    break
            if self.start:
                break

        self.star1_ans = 0
        self.star2_ans = 0

    def star1(self, n: int = 64):
        q = deque([(self.start, 0)])
        seen, ans = set(), set()

        while q:
            coords, steps = q.popleft()
            if (coords, steps) in seen or steps >= n:
                if steps == n:
                    ans.add(coords)
                continue

            seen.add((coords, steps))
            row, col = coords
            for r, c in [
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1),
            ]:
                if (
                    0 <= r < self.hi_y
                    and 0 <= c < self.hi_x
                    and self.map[r][c] in {"S", "."}
                ):
                    q.append(((r, c), steps + 1))

        self.star1_ans = len(ans)
        print(f"Day 21, Star 1 Answer: {self.star1_ans}")
        return self.star1_ans


if __name__ == "__main__":
    day21 = Day21()
    day21.star1()  # 3605
    # day18.star2()
