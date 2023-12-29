from utils.utilities import AOCUtils

UTILS = AOCUtils(get_env=True)


class Day4:
    def __init__(self, day: int = 4):
        self.cards = UTILS.get_input_by_line(day, strip=True)
        self.data = self.get_data(self.cards)
        self.num_matches = {}
        self.star1_ans = 0
        self.star2_ans = 0

    @staticmethod
    def get_data(cards: list):
        data = {}

        for card in cards:
            nums = card.split(":")
            card_num = nums[0].split(" ")[-1]
            wins, plays = nums[1].split("|")
            wins, plays = wins.split(" "), plays.split(" ")
            data[int(card_num)] = (wins, plays)

        return data

    def star1(self):
        for k, v in self.data.items():
            self.num_matches[k] = 0
            points, matches = 0, (set(v[0]) & set(v[1])) - {""}

            if matches:
                points += 2 ** (len(matches) - 1)
                self.star1_ans += points
                self.num_matches[k] += len(matches)

        print(f"Day 4, Star 1 Answer: {self.star1_ans}")
        return self.star1_ans

    def star2(self):
        count = {k: 0 for k in self.data}

        for k in self.data:
            count[k] += 1
            if not self.num_matches[k]:
                continue

            for i in range(k + 1, k + 1 + self.num_matches[k]):
                count[i] += count[k]

        self.star2_ans = sum([v for _, v in count.items()])

        print(f"Day 4, Star 2 Answer: {self.star2_ans}")
        return self.star2_ans


if __name__ == "__main__":
    day4 = Day4()
    day4.star1()  # 21105
    day4.star2()  # 5329815
