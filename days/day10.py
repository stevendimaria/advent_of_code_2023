import matplotlib.path

from collections import deque

from utils.utilities import AOCUtils

UTILS = AOCUtils(get_env=True)


class Day10:
    def __init__(self, day: int):
        inp = UTILS.get_input_by_line(day)

        self.map = [l.strip() for l in inp]
        self.n_pipes = {"|", "L", "J", "S"}
        self.s_pipes = {"|", "7", "F", "S"}
        self.w_pipes = {"-", "J", "7", "S"}
        self.e_pipes = {"-", "L", "F", "S"}
        self.start = None
        self.seen = set()
        self.path = []

        self.star1_ans = 0
        self.star2_ans = 0

        for r, i in enumerate(self.map):
            if self.start:
                break
            for c in range(r):
                if self.map[r][c] == "S":
                    self.start = (r, c)
                    break

    def return_adj(self, r: int, c: int) -> list:
        out = []

        if (
            r > 0
            and self.map[r - 1][c] in self.s_pipes
            and self.map[r][c] in self.n_pipes
        ):
            out.append((r - 1, c))
        if (
            r < len(self.map) - 1
            and self.map[r + 1][c] in self.n_pipes
            and self.map[r][c] in self.s_pipes
        ):
            out.append((r + 1, c))
        if (
            c > 0
            and self.map[r][c - 1] in self.e_pipes
            and self.map[r][c] in self.w_pipes
        ):
            out.append((r, c - 1))
        if (
            c < len(self.map[r]) - 1
            and self.map[r][c + 1] in self.w_pipes
            and self.map[r][c] in self.e_pipes
        ):
            out.append((r, c + 1))

        return out

    def get_path(self):
        path, seen = [self.start], set()
        cycle = False

        while not cycle:
            seen.add(path[-1])
            found = False
            for y, x in self.return_adj(*path[-1]):
                if (y, x) not in seen:
                    path.append((y, x))
                    found = True
                    break
            cycle = not found

        return path

    def star1(self):
        q = deque([(self.start, 0)])

        while q:
            coords, steps = q.popleft()
            if coords in self.seen:
                continue
            self.seen.add(coords)

            _nxt = self.return_adj(*coords)
            q.extend([(tup, steps + 1) for tup in _nxt])
            self.star1_ans = max(self.star1_ans, steps)

        print(f"Day 10, Star 1 Answer: {self.star1_ans}")
        return self.star1_ans

    def star2(self):
        p = self.get_path()
        polygon = matplotlib.path.Path(p)

        for r in range(len(self.map)):
            for c in range(len(self.map[r])):
                if (r, c) not in self.seen and polygon.contains_point((r, c)):
                    self.star2_ans += 1

        print(f"Day 10, Star 2 Answer: {self.star2_ans}")
        return self.star2_ans


if __name__ == "__main__":
    day10 = Day10(10)
    day10.star1()  # 6842
    day10.star2()  # 393
