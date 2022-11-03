"""
binarysearch.com :: Weekly Contest 42 :: Virtual Boolean Array
https://binarysearch.com/room/Weekly-Contest-42-B2uSxptT2C?questionsetIndex=1
jramaswami
"""
class BooleanArray:
    def __init__(self):
        self.bools = set()
        # val holds the value of the indices in self.bools
        # so val is True then the indices in self.bools is True
        self.val = True

    def setTrue(self, i):
        if self.val == True:
            self.bools.add(i)
        else:
            self.bools.discard(i)

    def setFalse(self, i):
        if self.val == False:
            self.bools.add(i)
        else:
            self.bools.discard(i)
        
    def setAllTrue(self):
        self.val = False
        self.bools = set()

    def setAllFalse(self):
        self.val = True
        self.bools = set()
        
    def getValue(self, i):
        if self.val == True:
            return i in self.bools
        else:
            return i not in self.bools


def test_1():
    a = BooleanArray()
    assert a.getValue(9) == False
    a.setAllTrue()
    assert a.getValue(3) == True
    a.setFalse(4)
    assert a.getValue(4) == False

def test_2():
    a = BooleanArray()
    a.setTrue(5)
    assert a.getValue(5) == True
    a.setFalse(5)
    assert a.getValue(5) == False
