"""
binarysearch.com :: Playlist Queue
jramaswami
"""
from sortedcontainers import SortedList


class PlaylistQueue:
    def __init__(self, songs):
        self.songs = dict(enumerate(songs))
        self.order = SortedList(list(range(len(songs))))
        self.count = len(songs)

    def play(self, i):
        index = self.order[i]
        song = self.songs[index]
        del self.songs[index]
        new_index = self.count
        self.count += 1
        self.order.pop(i)
        self.order.add(new_index)
        self.songs[new_index] = song
        return song
       

def test_1():
    q = PlaylistQueue(["a", "b", "c"])
    assert q.play(0) == "a" # Queue becomes ["b", "c", "a"]
    assert q.play(1) == "c" # Queue becomes ["b", "a", "c"]
    assert q.play(2) == "c" # Queue becomes ["b", "a", "c"]
    assert q.play(0) == "b" # Queue becomes ["a", "c", "b"]
