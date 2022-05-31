"""
binarysearch.com :: Border Crossing
jramaswami
"""


import heapq
import collections
import math


class Solution:

    def solve(self, roads, countries, start, end):
        city_countries = collections.defaultdict(int)
        for country, cities in enumerate(countries):
            for city in cities:
                city_countries[city] = country

        graph= collections.defaultdict(list)
        for u, v, w in roads:
            graph[u].append((v, w))

        dist = collections.defaultdict(lambda: (math.inf, math.inf))
        dist[start] = (0, 0)
        queue = []
        queue.append((0, 0, start))
        while queue:
            cu, wu, u = heapq.heappop(queue)
            if u == end:
                return [cu, wu]
            if (cu, wu) != dist[u]:
                continue
            for v, wv in graph[u]:
                cv = cu
                if city_countries[v] != city_countries[u]:
                    cv = cu + 1
                if (cv, wu + wv) < dist[v]:
                    dist[v] = (cv, wu + wv)
                    heapq.heappush(queue, (cv, wu + wv, v))

def test_1():
    roads = [ [0, 1, 1], [1, 2, 1], [0, 2, 4] ]
    countries = [ [0], [1], [2] ]
    start = 0
    end = 2
    expected = [1, 4]
    assert Solution().solve(roads, countries, start, end) == expected


def test_2():
    roads = [ [0, 1, 1], [1, 3, 2], [0, 2, 2], [2, 3, 2] ]
    countries = [ [0], [1, 2], [3] ]
    start = 0
    end = 3
    expected = [2, 3]
    assert Solution().solve(roads, countries, start, end) == expected


def test_3():
    "RTE"
    roads = [[1,0,5]]
    countries = [[0,1]]
    start = 1
    end = 0
    expected = [0, 5]
    assert Solution().solve(roads, countries, start, end) == expected


def test_4():
    "WA"
    roads = [[1,0,5],[0,1,4]]
    countries = [[1,2],[0]]
    start = 1
    end = 0
    expected = [1, 5]
    assert Solution().solve(roads, countries, start, end) == expected
