"""
binarysearch.com :: Weekly Contest 33 :: CPU Scheduling
"""
import heapq
from collections import namedtuple

class Solution:
    def solve(self, tasks):
        # Sort by queue time
        tasks.sort(key=lambda t: t[1], reverse=True)
        timer = 0
        queue = []
        soln = []
        while tasks or queue:
            # Enqueue task
            while tasks and tasks[-1][1] <= timer:
                heapq.heappush(queue, (tasks[-1][2], tasks[-1][0]))
                tasks.pop()

            if queue:
                task_duration, task_id = heapq.heappop(queue)
                soln.append(task_id)
                timer = timer + task_duration
            else:
                timer = tasks[-1][1]

        return soln


def test_1():
    tasks = [ [0, 1, 5], [1, 1, 5], [2, 2, 2] ]
    solver = Solution()
    assert solver.solve(tasks) == [0, 2, 1]

def test_2():
    tasks = []
    solver = Solution()
    assert solver.solve(tasks) == []

def test_3():
    tasks = [[0, 0, 0], [1, 100000000, 0]]
    soln = [0]
    for t in range(2, 1000000):
        tasks.append((t, 0, 0))
        soln.append(t)
    soln.append(1)
    solver = Solution()
    assert solver.solve(tasks) == soln
