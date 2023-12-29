from collections import deque

from utils.utilities import AOCUtils

UTILS = AOCUtils(get_env=True)


class Day18:
    def __init__(self, day: int = 18):
        inp = UTILS.get_input_by_line(day, strip=True)

        self.dirs = []
        self.dist = []
        self.colors = []

        self.star1_ans = 0
        self.star2_ans = 0

        for li in inp:
            _dir, _dist, _color = li.split()
            self.dirs.append(_dir)
            self.dist.append(int(_dist))
            self.colors.append(_color[1:-1])

        self.hi_x, self.lo_x = 0, 0
        self.hi_y, self.lo_y = 0, 0
        self.edges = self.get_edges()

    def get_edges(self):
        edges = {(0, 0)}
        r, c = 0, 0

        for idx, d in enumerate(self.dirs):
            n = self.dist[idx]

            if d == "U":
                edges |= set([(i, c) for i in range(r, r + 1 + n)])
                r += n
            elif d == "D":
                edges |= set([(i, c) for i in range(r, r - 1 - n, -1)])
                r -= n
            elif d == "R":
                edges |= set([(r, i) for i in range(c, c + 1 + n)])
                c += n
            elif d == "L":
                edges |= set([(r, i) for i in range(c, c - 1 - n, -1)])
                c -= n

            self.hi_y, self.lo_y = max(self.hi_y, r), min(self.lo_y, r)
            self.hi_x, self.lo_x = max(self.hi_x, c), min(self.lo_x, c)

        return edges

    def find_fill(self):
        for r, c in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
            ans = 0
            for i in range(r + 1, self.hi_y + 1):
                if (i, c) in self.edges:
                    ans += 1
                    break
            for i in range(r - 1, self.lo_y - 1, -1):
                if (i, c) in self.edges:
                    ans += 1
                    break
            for i in range(c + 1, self.hi_x + 1):
                if (r, i) in self.edges:
                    ans += 1
                    break
            for i in range(c - 1, self.lo_x - 1, -1):
                if (r, i) in self.edges:
                    ans += 1
                    break

            if ans == 4:
                return (r, c)

        return None

    def star1(self) -> int:
        q = deque([self.find_fill()])

        while q:
            r, c = q.popleft()
            if (r, c) in self.edges:
                continue

            self.edges.add((r, c))
            for i, j in [(r - 1, c), (r + 1, c), (r, c + 1), (r, c - 1)]:
                for n in range(i, self.hi_y + 1):
                    if (n, j) in self.edges:
                        break
                    q.append((n, j))
                for n in range(i, self.lo_y - 1, -1):
                    if (n, j) in self.edges:
                        break
                    q.append((n, j))
                for n in range(j, self.hi_x + 1):
                    if (i, n) in self.edges:
                        break
                    q.append((i, n))
                for n in range(j, self.lo_x - 1, -1):
                    if (i, n) in self.edges:
                        break
                    q.append((i, n))

        self.star1_ans = len(self.edges)
        print(f"Day 18, Star 1 Answer: {self.star1_ans}")
        return self.star1_ans


if __name__ == "__main__":
    day18 = Day18()
    day18.star1()  # 95356
    # day18.star2()
