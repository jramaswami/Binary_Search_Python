"""
binarysearch.com :: Unlock Rooms
jramaswami
"""


class Solution:

    def solve(self, keys_in_rooms):
        keys_obtained = [0 for _ in keys_in_rooms]
        keys_obtained[0] = 1
        visited = set()

        def dfs(room):
            visited.add(room)
            for key in keys_in_rooms[room]:
                keys_obtained[key] += 1

            if all(k > 0 for k in keys_obtained):
                # We have unlocked all rooms.  We can stop here.
                return True

            for next_room, key_count in enumerate(keys_obtained):
                if key_count > 0 and next_room not in visited:
                    result = dfs(next_room)
                    if result:
                        return True

            visited.remove(room)
            for key in keys_in_rooms[room]:
                keys_obtained[key] += 1
            return False

        return dfs(0)


def test_1():
    rooms = [[1, 3], [2], [0], []]
    assert Solution().solve(rooms) == True


def test_2():
    rooms = [[1, 3], [2], [0], [], []]
    assert Solution().solve(rooms) == False
