import math
from heapq import heappush, heappop

from utils.utilities import AOCUtils

UTILS = AOCUtils(get_env=True)


class Day5:
    def __init__(self, day: int=5):
        self.maps = UTILS.get_input_by_line(day, strip=True)
        self.seeds = []
        self.seed_ranges = []
        self.conversions = {}
        self.map_order = []
        self.star1_ans = math.inf
        self.star2_ans = math.inf

        self.get_data()

    def get_data(self):
        def get_vals(vals: list):
            out = []
            while vals:
                _next = vals.pop(0)
                if not _next:
                    break
                elif _next[0].isdigit():
                    out.append(_next.split(" "))
                else:
                    break

            out = [[int(x) for x in convs] for convs in out]
            return out

        seeds = self.maps.pop(0)
        seeds = seeds.split(":")[1].split(" ")[1:]
        self.seeds = [int(s) for s in seeds]

        for i in range(0, len(self.seeds), 2):
            self.seed_ranges.append((self.seeds[i], self.seeds[i] + self.seeds[i + 1]))

        for i, _map in enumerate(self.maps):
            if not _map or _map[0].isdigit():
                continue

            _map = _map.strip()
            self.map_order.append(_map)
            self.conversions[_map] = get_vals(self.maps[i + 1 :])

    def star1(self):
        seed_paths = {}

        for s in self.seeds:
            seed_paths[s] = [s]

            for m in self.map_order:
                curr = seed_paths[s][-1]
                found = False
                for dst, src, rng in self.conversions[m]:
                    if src <= curr <= src + rng:
                        adj = dst - src
                        seed_paths[s].append(curr + adj)
                        found = True
                        break
                if not found:
                    seed_paths[s].append(curr)

        for _, v in seed_paths.items():
            self.star1_ans = min(self.star1_ans, v[-1])

        print(f"Day 5, Star 1 Answer: {self.star1_ans}")
        return self.star1_ans

    def star2(self):
        src_ranges = []

        for m in self.map_order:
            if not src_ranges:
                for r in self.seed_ranges:
                    heappush(src_ranges, r)

            dest_ranges = []
            for dst, src, rng in self.conversions[m]:
                heappush(dest_ranges, (src, src + rng, dst - src))

            _next = set()
            while src_ranges:
                lo_src, hi_src = heappop(src_ranges)
                lo_dest, hi_dest, adj = heappop(dest_ranges)

                if hi_src < lo_dest:
                    _next |= {(lo_src, hi_src)}
                    heappush(dest_ranges, (lo_dest, hi_dest, adj))
                elif lo_src < lo_dest:
                    if hi_src <= hi_dest:
                        _next |= {(lo_src, lo_dest - 1), (lo_dest + adj, hi_src + adj)}
                        heappush(dest_ranges, (lo_dest, hi_dest, adj))
                        heappush(src_ranges, (lo_dest, hi_src))
                    else:
                        _next |= {(lo_src, lo_dest - 1), (lo_dest + adj, hi_dest + adj)}
                        heappush(src_ranges, (hi_dest, hi_src))
                elif lo_src <= hi_dest:
                    if hi_src <= hi_dest:
                        _next |= {(lo_src + adj, hi_src + adj)}
                        heappush(dest_ranges, (lo_dest, hi_dest, adj))
                    else:
                        _next |= {(lo_src + adj, hi_dest + adj)}
                        heappush(src_ranges, (hi_dest, hi_src))
                else:
                    if not dest_ranges:
                        _next |= {(lo_src, hi_src)}
                    else:
                        heappush(src_ranges, (lo_src, hi_src))

            temp_heap = []
            while _next:
                heappush(temp_heap, _next.pop())
            src_ranges = temp_heap

        while src_ranges:
            lo, hi = heappop(src_ranges)
            self.star2_ans = min(lo, self.star2_ans)

        print(f"Day 5, Star 2 Answer: {self.star2_ans}")
        return self.star2_ans


if __name__ == "__main__":
    day5 = Day5(5)
    day5.star1()  # 389056265
    day5.star2()  # 137516820
