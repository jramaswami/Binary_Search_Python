"""
binarysearch.com :: Task Hare
jramaswami
"""
class Solution:
    def solve(self, tasks, people):
        tasks.sort()
        people.sort()

        soln = 0
        while people and tasks:
            while tasks[-1] > people[-1]:
                tasks.pop()
            
            if tasks:
                tasks.pop()
                people.pop()
                soln += 1

        return soln


def test_1():
    tasks = [3, 2, 9, 13]
    people = [10, 5, 2, 1]
    assert Solution().solve(tasks, people) == 3

def test_2():
    tasks = [2, 2]
    people = [1]
    assert Solution().solve(tasks, people) == 0
