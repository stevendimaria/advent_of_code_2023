from collections import deque

from utils.utilities import AOCUtils

UTILS = AOCUtils(get_env=True)


class Day16:
    def __init__(self, day: int=16):
        self.tiles = UTILS.get_input_by_line(day, strip=True)
        self.dirs = {"R": [0, 1], "L": [0, -1], "U": [-1, 0], "D": [1, 0]}
        self.cache = {}
        self.star1_ans = 0
        self.star2_ans = 0

    def pass_check(self, r, c, d):
        check = False
        if self.tiles[r][c] == ".":
            check = True
        if d in {"U", "D"} and self.tiles[r][c] == "|":
            check = True
        if d in {"R", "L"} and self.tiles[r][c] == "-":
            check = True
        return check

    def mirror(self, r, c, d):
        if self.tiles[r][c] == "/":
            if d == "R":
                return r - 1, c, "U"
            elif d == "D":
                return r, c - 1, "L"
            elif d == "L":
                return r + 1, c, "D"
            elif d == "U":
                return r, c + 1, "R"
        elif self.tiles[r][c] == "\\":
            if d == "R":
                return r + 1, c, "D"
            elif d == "D":
                return r, c + 1, "R"
            elif d == "L":
                return r - 1, c, "U"
            elif d == "U":
                return r, c - 1, "L"

    def splitter(self, r, c):
        if self.tiles[r][c] == "|":
            return [(r - 1, c, "U"), (r + 1, c, "D")]
        return [(r, c + 1, "R"), (r, c - 1, "L")]

    def len_check(self, r, c):
        return 0 <= r < len(self.tiles) and 0 <= c < len(self.tiles[0])

    def star1(self, start=(0, 0, "R"), star=1):
        seen, ans, q = set(), set(), deque([start])

        while q:
            r, c, d = q.popleft()
            if (r, c, d) in seen:
                continue
            seen.add((r, c, d))
            ans.add((r, c))

            if self.pass_check(r, c, d):
                _r, _c = r + self.dirs[d][0], c + self.dirs[d][1]
                if self.len_check(_r, _c):
                    q.append((_r, _c, d))
            elif self.tiles[r][c] in {"/", "\\"}:
                nxt = self.mirror(r, c, d)
                if self.len_check(nxt[0], nxt[1]):
                    q.append(self.mirror(r, c, d))
            else:
                for nxt in self.splitter(r, c):
                    if self.len_check(nxt[0], nxt[1]):
                        q.append(nxt)

        if star != 1:
            self.star2_ans = max(len(ans), self.star2_ans)
        else:
            self.star1_ans = len(ans)
            print(f"Day 16, Star 1 Answer: {self.star1_ans}")
            return self.star1_ans

    def star2(self):
        for r in range(len(self.tiles)):
            self.star1(start=(r, 0, "R"), star=2)
            self.star1(start=(r, len(self.tiles[0]) - 1, "L"), star=2)
        for c in range(len(self.tiles[0])):
            self.star1(start=(0, c, "D"), star=2)
            self.star1(start=(len(self.tiles) - 1, c, "U"), star=2)

        print(f"Day 16, Star 2 Answer: {self.star2_ans}")
        return self.star2_ans


if __name__ == "__main__":
    day16 = Day16()
    day16.star1()  # 7498
    day16.star2()  # 7846
