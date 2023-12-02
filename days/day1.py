from advent_of_code_2023.utils.utilities import AOCUtils

UTILS = AOCUtils(input_path="/Users/stevendimaria/Desktop/AoC23")


class Day1:
    def __init__(self, day: int):
        self.calibration_values = UTILS.get_input_by_line(day=day)
        self.num_map = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
        }

    def star1(self, find_star2: bool = False) -> int:
        ans = 0
        for line in self.calibration_values:
            v1, v2 = "", ""
            s, e = 0, len(line) - 1
            while e > 0:
                if not v1:
                    if line[s].isdigit():
                        v1 = line[s]
                    elif find_star2:
                        v1 = self.star2(s=s, line=line)
                if not v2:
                    if line[e].isdigit():
                        v2 = line[e]
                    elif find_star2:
                        v2 = self.star2(e=e, line=line)

                if v1 and v2:
                    ans += int(v1 + v2)
                    break

                s += 1
                e -= 1

            if not v1:
                ans += int(v2 + v2)
            if not v2:
                ans += int(v1 + v1)

        print(ans)
        return ans

    def star2(self, line: str, s=None, e=None) -> str:
        out = ""

        if isinstance(s, int):
            e = s + 3
            if line[s:e] in {"one", "two", "six"}:
                out = self.num_map[line[s:e]]
            elif line[s : e + 1] in {"four", "five", "nine"}:
                out = self.num_map[line[s : e + 1]]
            elif line[s : e + 2] in {"three", "seven", "eight"}:
                out = self.num_map[line[s : e + 2]]
            else:
                pass
        elif isinstance(e, int):
            e += 1
            s = e - 3
            if line[s:e] in {"one", "two", "six"}:
                out = self.num_map[line[s:e]]
            elif line[s - 1 : e] in {"four", "five", "nine"}:
                out = self.num_map[line[s - 1 : e]]
            elif line[s - 2 : e] in {"three", "seven", "eight"}:
                out = self.num_map[line[s - 2 : e]]
            else:
                pass
        else:
            out = ""

        return out


if __name__ == "__main__":
    day1 = Day1(1)
    day1.star1()  # 54697
    day1.star1(find_star2=True)  # 54885
