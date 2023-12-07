from collections import Counter
from heapq import heappush, heappop

from utils.utilities import AOCUtils

UTILS = AOCUtils(get_env=True)


class Day7:
    def __init__(self, day: int):
        inp = UTILS.get_input_by_line(day)

        self.hands = [
            (hand, int(bid)) for hand, bid in [x.strip().split() for x in inp]
        ]
        self.hand_types = {
            "highcard": 1,
            "onepair": 2,
            "twopair": 3,
            "threeofakind": 4,
            "fullhouse": 5,
            "fourofakind": 6,
            "fiveofakind": 7,
        }
        self.star1_ans = 0
        self.star2_ans = 0

    @staticmethod
    def get_hand_type(hand: str, star2: bool = False) -> str:
        cards = Counter(hand)

        if star2 and cards.get("J"):
            temp = sorted([x for x in cards.items()], key=lambda x: -x[1])
            if temp[0][0] == "J":
                temp.append(temp.pop(0))

            cards[temp[0][0]] += cards["J"]
            cards.pop("J")
            if not cards:
                cards = Counter("AAAAA")

        if len(cards) == 5:
            return "highcard"
        elif len(cards) == 4:
            return "onepair"
        elif len(cards) == 3:
            for _, n in cards.most_common(3):
                if n == 3:
                    return "threeofakind"
            return "twopair"
        elif len(cards) == 2:
            for _, n in cards.most_common(2):
                if n == 4:
                    return "fourofakind"
            return "fullhouse"
        elif len(cards) == 1:
            return "fiveofakind"

    @staticmethod
    def hand_to_nums(hand: str, card_rank: dict) -> list:
        out = []
        for c in hand:
            out.append(card_rank[c])

        return out

    def star1(self, star2: bool = False, card_rank: dict = None):
        ans, ct, h = 0, 0, []
        if not card_rank:
            card_rank = {v: k for k, v in enumerate("23456789TJQKA")}

        for hand, bid in self.hands:
            hand_type = self.get_hand_type(hand, star2)
            hand_val = self.hand_to_nums(hand, card_rank)
            heappush(h, (self.hand_types[hand_type], *hand_val, bid))

        while h:
            ct += 1
            ans += heappop(h)[-1] * ct

        if not star2:
            self.star1_ans = ans
            print(f"Day 7, Star 1 Answer: {ans}")
        else:
            self.star2_ans = ans
            print(f"Day 7, Star 2 Answer: {ans}")
        return ans

    def star2(self):
        card_rank = {v: k for k, v in enumerate("J23456789TQKA")}
        return self.star1(True, card_rank)


if __name__ == "__main__":
    day7 = Day7(7)
    day7.star1()  # 250946742
    day7.star2()  # 251824095
