from utils.utilities import AOCUtils

UTILS = AOCUtils(get_env=True)


class Day9:
    def __init__(self, day: int=9):
        inp = UTILS.get_input_by_line(day)

        self.seqs = [[i for i in map(int, s.strip().split())] for s in inp]
        self.star1_ans = 0
        self.star2_ans = 0

    @staticmethod
    def get_vals(seq: list, star: int = 1) -> list:
        out = [seq]
        while sum(seq) != 0:
            temp = []
            for i in range(len(seq) - 1, 0, -1):
                temp.append(seq[i] - seq[i - 1])
            out.append((seq := temp[::-1]))

        ans = 0
        for j in range(len(out) - 1, 0, -1):
            if star == 1:
                ans += out[j - 1][-1]
            elif star == 2:
                ans = out[j - 1][0] - ans

        return ans

    def star1(self):
        for s in self.seqs:
            self.star1_ans += self.get_vals(s)

        print(f"Day 9, Star 1 Answer: {self.star1_ans}")
        return self.star1_ans

    def star2(self):
        for s in self.seqs:
            self.star2_ans += self.get_vals(s, star=2)

        print(f"Day 9, Star 2 Answer: {self.star2_ans}")
        return self.star2_ans


if __name__ == "__main__":
    day9 = Day9()
    day9.star1()  # 1684566095
    day9.star2()  # 1136
