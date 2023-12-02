from advent_of_code_2023.utils.utilities import AOCUtils

UTILS = AOCUtils(input_path="/Users/stevendimaria/Desktop/AoC23")


class Day2:
    def __init__(self, day: int, show_ans: int = 1):
        self.show_ans = show_ans
        self.games = UTILS.get_input_by_line(day)
        self.data = {}
        self.limit = {
            "red": 12,
            "green": 13,
            "blue": 14,
        }
        self.star1_ans = 0
        self.star2_data = {}
        self.star2_ans = 0

    def get_data(self, game: str, star2: bool = True) -> int:
        _id, _games = game.split(":")
        _id = int(_id.split(" ")[1])
        self.data[_id] = []

        for g in _games.split(";"):
            self.data[_id].append({})
            _data = g.split(",")
            for d in _data:
                _, amt, col = d.split(" ")
                col = col.strip()

                self.data[_id][-1][col] = int(amt)

        if star2:
            self.star2_data[_id] = {
                "red": 1,
                "green": 1,
                "blue": 1,
            }
        return _id

    def star1(self, star2: bool = True) -> int:
        for game in self.games:
            _id = self.get_data(game)
            flag = True
            for d in self.data[_id]:
                for k, v in d.items():
                    if flag and self.limit[k] < v:
                        flag = False
                    if star2:
                        self.star2_data[_id][k] = max(self.star2_data[_id][k], v)
            if flag:
                self.star1_ans += _id

        if self.show_ans:
            print(f"Day 2, Star 1 Answer: {self.star1_ans}")
        return self.star1_ans

    def star2(self) -> int:
        for _id, vals in self.star2_data.items():
            curr = 1
            for c, i in vals.items():
                curr *= i
            self.star2_ans += curr

        if self.show_ans:
            print(f"Day 2, Star 2 Answer: {self.star2_ans}")
        return self.star2_ans


if __name__ == "__main__":
    day2 = Day2(2)
    day2.star1()  # 2439
    day2.star2()  # 63711
