"""
binarysearch.com :: Task Schedule
jramaswami
"""


import collections
import heapq


class TaskQueue:

    def __init__(self):
        self.queue = []

    def push(self, task_time, task_count, task_id):
        heapq.heappush(self.queue, (task_time, -task_count, task_id))

    def pop(self):
        task_time, neg_task_count, task_id = heapq.heappop(self.queue)
        return task_time, -neg_task_count, task_id

    def __len__(self):
        return len(self.queue)


class Solution:

    def solve(self, tasks, k):
        # Count the kind of each task.
        ctr = collections.Counter(tasks)
        # Each type of task can be started at time 0.
        queue = TaskQueue()
        for task_id, task_count in ctr.items():
            queue.push(0, task_count, task_id)
        # Process tasks in time order.
        timer = 0
        while queue:
            task_time, task_count, task_id = queue.pop()
            if task_time >= timer:
                timer = task_time + 1
            else:
                timer += 1
            task_count -= 1
            if task_count:
                queue.push(timer + k, task_count, task_id)
            print(f"{task_id=} done @ {timer=}; {task_count=}")
        return timer


def test_1():
    tasks = [0, 0, 0, 1, 1, 0]
    k = 1
    expected = 7
    assert Solution().solve(tasks, k) == expected


def test_2():
    "WA"
    tasks = [1, 2, 2, 0, 2]
    k = 1
    expected = 5
    assert Solution().solve(tasks, k) == expected
