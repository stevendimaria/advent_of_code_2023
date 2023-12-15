from collections import OrderedDict
from utils.utilities import AOCUtils

UTILS = AOCUtils(get_env=True)


class Day15:
    def __init__(self, day: int):
        self.directions = UTILS.get_input_by_line(day)[0].strip().split(",")

        self.star1_ans = 0
        self.star2_ans = 0

    @staticmethod
    def get_val(word: str, mult: int = 17, mod: int = 256, box: int = 0):
        for ch in word:
            ascii_code = ord(ch)
            box += ascii_code
            box *= mult
            box %= mod
        return ascii_code, box

    def star1(self):
        self.star1_ans = sum([self.get_val(w)[1] for w in self.directions])

        print(f"Day 15, Star 1 Answer: {self.star1_ans}")
        return self.star1_ans

    def star2(self):
        boxes = {i: OrderedDict() for i in range(256)}

        for w in self.directions:
            label, lens = w.split("=") if "=" in w else w.split("-")
            box = self.get_val(label)[1]

            if not lens and boxes[box].get(label):
                del boxes[box][label]
            elif lens:
                boxes[box][label] = int(lens)

        for box_num, box in boxes.items():
            for slot, label in enumerate(box):
                focal_length = box[label]
                self.star2_ans += (1 + box_num) * (slot + 1) * focal_length

        print(f"Day 15, Star 2 Answer: {self.star2_ans}")
        return self.star2_ans


day15 = Day15(15)
day15.star1()  # 511416
day15.star2()  # 290779
