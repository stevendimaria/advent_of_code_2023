from utils.utilities import AOCUtils

UTILS = AOCUtils(get_env=True)


class Day11:
    def __init__(self, day: int = 11):
        self.galaxy = UTILS.get_input_by_line(day, strip=True)
        self.n_galaxies = 0
        self.galaxies = {}
        self.empty = {"rows": {}, "cols": {}}

        self.star1_ans = 0
        self.star2_ans = 0

    def expand_galaxy(self, galaxy, e):
        n = 0
        rows, cols = {}, {}

        for r in range(len(galaxy)):
            if not rows.get(r):
                rows[r] = 0

            for c in range(len(galaxy[r])):
                if not cols.get(c):
                    cols[c] = 0

                if galaxy[r][c] == "#":
                    rows[r] = 1
                    cols[c] = 1
                    n += 1
                    self.galaxies[n] = (r, c)
        self.n_galaxies = n

        for i in range(len(galaxy)):
            if not rows.get(i):
                self.empty["rows"][i] = e
        for j in range(len(galaxy[0])):
            if not cols.get(j):
                self.empty["cols"][j] = e

    def star(self, e, star_num: int = 1):
        self.expand_galaxy(self.galaxy, e)
        ans = 0

        for i in range(1, self.n_galaxies + 1):
            for j in range(i + 1, self.n_galaxies + 1):
                r1, c1 = self.galaxies[i]
                r2, c2 = self.galaxies[j]

                for x in range(min(r1, r2), max(r1, r2)):
                    ans += self.empty["rows"].get(x, 1)
                for y in range(min(c1, c2), max(c1, c2)):
                    ans += self.empty["cols"].get(y, 1)

        if star_num == 1:
            self.star1_ans = ans
            print(f"Day 11, Star 1 Answer: {ans}")
            return self.star1_ans
        else:
            self.star2_ans = ans
            print(f"Day 11, Star 2 Answer: {ans}")
            return self.star2_ans


if __name__ == "__main__":
    day11 = Day11()
    day11.star(e=2)  # 9627977
    day11.star(star_num=2, e=1000000)  # 644248339497
