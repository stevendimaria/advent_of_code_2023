from utils.utilities import AOCUtils

UTILS = AOCUtils(get_env=True)


class Day6:
    def __init__(self, day: int):
        inp = UTILS.get_input_by_line(day)

        self.times = [int(x) for x in inp[0].split(":")[1].split()]
        self.dists = [int(x) for x in inp[1].split(":")[1].split()]
        self.n_races = 0
        self.races = []
        self.star2_race = [
            (
                int("".join(inp[0].split(":")[1].split())),
                int("".join(inp[1].split(":")[1].split())),
            )
        ]
        self.star1_ans = 0
        self.star2_ans = 0

        for i in range(len(self.times)):
            self.n_races += 1
            self.races.append((self.times[i], self.dists[i]))

    @staticmethod
    def get_wins(races: list):
        ans = 1

        for t, d in races:
            first = 0
            while (t - first) * first < d:
                first += 1

            ans *= 1 + (t - first) - first

        return ans

    def star1(self):
        self.star1_ans = self.get_wins(self.races)

        print(f"Day 6, Star 1 Answer: {self.star1_ans}")
        return self.star1_ans

    def star2(self):
        """
        Brute force is reasonable in this case, but boring

        self.star2_ans = self.get_wins(self.star2_race)
        """

        t, d = self.star2_race[0]
        first, last = 0, t
        while first < last:
            mid = (first + last) // 2

            if (t - mid) * mid > d:
                last = mid - 1
            elif (t - mid) * mid < d:
                first = mid + 1
            else:
                break

        self.star2_ans = 1 + (t - first) - first

        print(f"Day 6, Star 2 Answer: {self.star2_ans}")
        return self.star2_ans


if __name__ == "__main__":
    day6 = Day6(6)
    day6.star1()  # 608902
    day6.star2()  # 46173809
