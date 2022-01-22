"""
binarysearch.com :: Task Schedule
jramaswami
"""


import collections
import heapq


class TaskQueue:

    def __init__(self):
        self.queue = []

    def pop(self):
        neg_task_count, task_id = heapq.heappop(self.queue)
        return -neg_task_count, task_id

    def push(self, task_count, task_id):
        heapq.heappush(self.queue, (-task_count, task_id))

    def __len__(self):
        return len(self.queue)


class TimerQueue:

    def __init__(self):
        self.queue = []

    def top_time(self):
        return self.queue[0][0]

    def pop(self):
        _, task_count, task_id = heapq.heappop(self.queue)
        return task_count, task_id

    def push(self, task_time, task_count, task_id):
        heapq.heappush(self.queue, (task_time, task_count, task_id))

    def __len__(self):
        return len(self.queue)


class Solution:

    def solve(self, tasks, k):
        # Count the kind of each task.
        ctr = collections.Counter(tasks)
        # Each type of task can be started at time 0.
        task_queue = TaskQueue()
        for task_id, task_count in ctr.items():
            task_queue.push(task_count, task_id)

        timer_queue = TimerQueue()
        timer = 0
        while task_queue or timer_queue:
            # If the task_queue is empty, advance time to the first eligible
            # time for a task in the timer queue.
            if not task_queue:
                timer = timer_queue.top_time()

            # First put any eligible tasks back on the queue.
            while timer_queue and timer_queue.top_time() <= timer:
                task_count, task_id = timer_queue.pop()
                task_queue.push(task_count, task_id)

            # Process task id with the hightest task count.
            task_count, task_id = task_queue.pop()
            timer += 1
            task_count -= 1
            # If the the task id still has outstanding tasks, put it in the
            # timer queue to be done later.
            if task_count:
                timer_queue.push(timer + k, task_count, task_id)
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
