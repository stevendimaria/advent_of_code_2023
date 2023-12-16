from utils.answers import *
from days import *

DAYS = [
    DAY1 := day1.Day1(1),
    DAY2 := day2.Day2(2),
    DAY3 := day3.Day3(3),
    DAY4 := day4.Day4(4),
    DAY5 := day5.Day5(5),
    DAY6 := day6.Day6(6),
    DAY7 := day7.Day7(7),
    DAY8 := day8.Day8(8),
    DAY9 := day9.Day9(9),
    DAY10 := day10.Day10(10),
    DAY11 := day11.Day11(11),
    DAY12 := day12.Day12(12),
    DAY13 := day13.Day13(13),
    DAY14 := day14.Day14(14),
    DAY15 := day15.Day15(15),
    DAY16 := day16.Day16(16)
]


class UnitError(Exception):
    pass

def run_unit_tests():
    if DAY1.star1() != DAY1_1: raise UnitError('Error in Day 1, Star1')
    if DAY1.star1(find_star2=True) != DAY1_2: raise UnitError('Error in Day 1, Star2')
    if DAY2.star1() != DAY2_1: raise UnitError('Error in Day 2, Star1')
    if DAY2.star2() != DAY2_2: raise UnitError('Error in Day 2, Star2')
    if DAY3.star1() != DAY3_1: raise UnitError('Error in Day 3, Star1')
    if DAY3.star2() != DAY3_2: raise UnitError('Error in Day 3, Star2')
    if DAY4.star1() != DAY4_1: raise UnitError('Error in Day 4, Star1')
    if DAY4.star2() != DAY4_2: raise UnitError('Error in Day 4, Star2')
    if DAY5.star1() != DAY5_1: raise UnitError('Error in Day 5, Star1')
    if DAY5.star2() != DAY5_2: raise UnitError('Error in Day 5, Star2')
    if DAY6.star1() != DAY6_1: raise UnitError('Error in Day 6, Star1')
    if DAY6.star2() != DAY6_2: raise UnitError('Error in Day 6, Star2')
    if DAY7.star1() != DAY7_1: raise UnitError('Error in Day 7, Star1')
    if DAY7.star2() != DAY7_2: raise UnitError('Error in Day 7, Star2')
    if DAY8.star1() != DAY8_1: raise UnitError('Error in Day 8, Star1')
    if DAY8.star2() != DAY8_2: raise UnitError('Error in Day 8, Star2')
    if DAY9.star1() != DAY9_1: raise UnitError('Error in Day 9, Star1')
    if DAY9.star2() != DAY9_2: raise UnitError('Error in Day 9, Star2')
    if DAY10.star1() != DAY10_1: raise UnitError('Error in Day 10, Star1')
    if DAY10.star2() != DAY10_2: raise UnitError('Error in Day 10, Star2')
    if DAY11.star(e=2) != DAY11_1: raise UnitError('Error in Day 11, Star1')
    if DAY11.star(star_num=2, e=1000000) != DAY11_2: raise UnitError('Error in Day 11, Star2')
    if DAY12.star1() != DAY12_1: raise UnitError('Error in Day 12, Star1')
    # if DAY12.star2() != DAY12_2: raise UnitError('Error in Day 12, Star2')
    if DAY13.star1() != DAY13_1: raise UnitError('Error in Day 13, Star1')
    if DAY13.star2() != DAY13_2: raise UnitError('Error in Day 13, Star2')
    if DAY14.star1() != DAY14_1: raise UnitError('Error in Day 14, Star1')
    if DAY14.star2() != DAY14_2: raise UnitError('Error in Day 14, Star2')
    if DAY15.star1() != DAY15_1: raise UnitError('Error in Day 15, Star1')
    if DAY15.star2() != DAY15_2: raise UnitError('Error in Day 15, Star2')
    if DAY16.star1() != DAY16_1: raise UnitError('Error in Day 16, Star1')
    if DAY16.star2() != DAY16_2: raise UnitError('Error in Day 16, Star2')

    return 'Unit Tests: PASS'


if __name__ == "__main__":
    run_unit_tests()




