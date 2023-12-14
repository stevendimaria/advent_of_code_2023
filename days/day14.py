from utils.utilities import AOCUtils, BiDict

UTILS = AOCUtils(get_env=True)
B = 1000000000


class Day14:
    def __init__(self, day: int, inp=None):
        self.inp = UTILS.get_input_by_line(day)

        self.platform = [[s for s in x.strip()] for x in self.inp]
        self.dirs = {
            "N": (
                (-1, 0),
                range(len(self.platform) - 1, 0, -1),
                range(len(self.platform[0])),
            ),
            "W": ((0, -1), range(len(self.platform)), range(1, len(self.platform[0]))),
            "S": ((1, 0), range(len(self.platform) - 1), range(len(self.platform[0]))),
            "E": ((0, 1), range(len(self.platform)), range(len(self.platform[0]) - 1)),
        }

        self.star1_ans = 0
        self.star2_ans = 0

    def refresh(self):
        self.platform = [[s for s in x.strip()] for x in self.inp]

    def make_platform_tuples(self):
        return tuple([tuple([s for s in x]) for x in self.platform])

    def tilt(self, d: str):
        moved = True

        while moved:
            moved = False
            for i in self.dirs[d][1]:
                for j in self.dirs[d][2]:
                    if self.platform[i][j] in {".", "#"}:
                        continue

                    if (
                        self.platform[i + self.dirs[d][0][0]][j + self.dirs[d][0][1]]
                        == "."
                    ):
                        (
                            self.platform[i + self.dirs[d][0][0]][
                                j + self.dirs[d][0][1]
                            ],
                            self.platform[i][j],
                        ) = (
                            self.platform[i][j],
                            self.platform[i + self.dirs[d][0][0]][
                                j + self.dirs[d][0][1]
                            ],
                        )
                        moved = True

    def get_points(self):
        pts, ans = 0, 0
        for row in self.platform[::-1]:
            pts += 1
            for col in row:
                if col == "O":
                    ans += pts
        return ans

    def star1(self):
        self.tilt("N")
        self.star1_ans = self.get_points()

        print(f"Day 14, Star 1 Answer: {self.star1_ans}")
        return self.star1_ans

    def star2(self):
        self.refresh()

        curr = self.make_platform_tuples()
        seen, iters, it = set(), BiDict(), 0

        while curr not in seen:
            seen.add(curr)
            iters.insert(curr, it)
            it += 1

            for d in ["N", "W", "S", "E"]:
                self.tilt(d)
            curr = self.make_platform_tuples()

        cycle = it - (start := iters.fetch(curr))
        rem = B - ((((B - start) // cycle) * cycle) + start)
        self.platform = iters.fetch(start + rem)
        self.star2_ans = self.get_points()

        print(f"Day 14, Star 2 Answer: {self.star2_ans}")
        return self.star2_ans


if __name__ == "__main__":
    day14 = Day14(14)
    day14.star1()  # 106997
    day14.star2()  # 99641
