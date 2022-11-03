"""
binarysearch.com :: Cluster Management
https://binarysearch.com/room/Weekly-Contest-37-u2kU8duwTB?questionsetIndex=1
"""
class Solution:
    def solve(self, cores, tasks):

        def solve0(task_index, running_cores):
            if task_index >= len(tasks):
                return True
            else:
                can_do = False
                # For the given task, you can put it on any core that
                # can take it.
                for core_index, core_tasks in enumerate(running_cores):
                    if core_tasks + tasks[task_index] <= cores[core_index]:
                        running_cores0 = list(running_cores)
                        running_cores0[core_index] += tasks[task_index]
                        can_do = can_do or solve0(task_index + 1, running_cores0)
                return can_do

        return solve0(0, [0 for _ in cores])


def test_1():
    cores = [8, 10]
    tasks = [2, 3, 3, 3, 7]
    solver = Solution()
    assert solver.solve(cores, tasks) == True

def test_2():
    cores = [1, 3]
    tasks = [2, 2]
    solver = Solution()
    assert solver.solve(cores, tasks) == False