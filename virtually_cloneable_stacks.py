"""
binarysearch.com :: Virtually Cloneable Stacks
jramaswami
"""
class VirtuallyCloneableStacks:
    def __init__(self):
        self.stacks = [0]

    def copyPush(self, i):
        self.stacks.append(self.stacks[i] + 1)

    def copyPop(self, i):
        self.stacks.append(self.stacks[i] - 1)
        
    def size(self, i):
        return self.stacks[i]


def test_1():
    s = VirtuallyCloneableStacks()
    s.copyPush(0)
    s.copyPush(1)
    s.copyPop(2)
    s.size(0) == 0
    s.size(1) == 1
    s.size(2) == 2
    s.size(3) == 1
