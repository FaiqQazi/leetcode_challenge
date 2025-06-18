from collections import deque

class Solution:
    def turn_knob_up(self, current, i):
        if current[i] == "9":
            num = 0
        else:
            num = int(current[i]) + 1
        num_str = str(num)
        new_string = current[:i] + num_str + current[i+1:]
        return new_string

    def turn_knob_down(self, current, i):
        if current[i] == "0":
            num = 9
        else:
            num = int(current[i]) - 1
        num_str = str(num)
        new_string = current[:i] + num_str + current[i+1:]
        return new_string

    def openLock(self, deadends, target):
        graph = {}
        graph["0000"] = []
        queue = deque()
        queue.append(("0000", 0))
        visited = set()
        dead = set(deadends)

        while queue:
            current, steps = queue.popleft()

            if current in visited:
                continue
            visited.add(current)

            if current in dead:
                continue

            if current == target:
                return steps

            for i in range(4):
                up = self.turn_knob_up(current, i)
                down = self.turn_knob_down(current, i)
                queue.append((up, steps + 1))
                queue.append((down, steps + 1))

                if current not in graph:
                    graph[current] = []
                graph[current].append(up)
                graph[current].append(down)

        return -1
