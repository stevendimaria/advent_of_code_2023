from math import lcm
from utils.utilities import AOCUtils

UTILS = AOCUtils(get_env=True)


class Node:
    def __init__(self, name: str, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right


class Day8:
    def __init__(self, day: int=8):
        inp = UTILS.get_input_by_line(day)

        self.nodes = {}
        self.steps = inp[0].strip()
        self.n_steps = len(self.steps)
        self.star1_ans = 0
        self.star2_ans = 0

        for d in inp[2:]:
            head, dirs = d.split(" = ")
            l, r = dirs[1:4], dirs[6:9]
            if not self.nodes.get(head):
                self.nodes[head] = Node(head)
            if not self.nodes.get(l):
                self.nodes[l] = Node(l)
            if not self.nodes.get(r):
                self.nodes[r] = Node(r)

            self.nodes[head].right = self.nodes[r]
            self.nodes[head].left = self.nodes[l]

    def star1(self):
        curr, step = self.nodes["AAA"], 0

        while curr.name != "ZZZ":
            self.star1_ans += 1
            if step >= self.n_steps:
                step = 0

            if self.steps[step] == "R":
                curr = self.nodes[curr.right.name]
            elif self.steps[step] == "L":
                curr = self.nodes[curr.left.name]

            step += 1

        print(f"Day 8, Star 1 Answer: {self.star1_ans}")
        return self.star1_ans

    def star2(self):
        nodes, step = [], 0
        for n in self.nodes:
            if n[-1] == "A":
                nodes.append(self.nodes[n])

        step_list = []
        for node in nodes:
            steps, step = 0, 0
            while node.name[-1] != "Z":
                if step >= self.n_steps:
                    step = 0

                if self.steps[step] == "R":
                    node = self.nodes[node.right.name]
                elif self.steps[step] == "L":
                    node = self.nodes[node.left.name]

                step += 1
                steps += 1
            step_list.append(steps)

        self.star2_ans = lcm(*step_list)
        print(f"Day 8, Star 2 Answer: {self.star2_ans}")
        return self.star2_ans


if __name__ == "__main__":
    day8 = Day8()
    day8.star1()  # 13207
    day8.star2()  # 12324145107121
