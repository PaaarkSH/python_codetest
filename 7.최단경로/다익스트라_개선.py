import heapq


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    di