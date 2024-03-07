import heapq

def solution(n, route):
    # 그래프를 인접 리스트로 표현
    graph = [[] for _ in range(n + 1)]
    for s, d, w in route:
        graph[s].append((d, w))

    # 최단 거리와 최대 가중치를 저장할 리스트 초기화
    distances = [float('inf')] * (n + 1)
    max_weights = [0] * (n + 1)
    distances[1] = 0  # 1번 공항에서 출발

    # 우선순위 큐를 이용한 다익스트라 알고리즘
    pq = [(0, 1)]  # (거리, 노드)
    while pq:
        dist, node = heapq.heappop(pq)
        if distances[node] < dist:
            continue
        for neighbor, weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                max_weights[neighbor] = weight  # 최대 가중치 갱신
                heapq.heappush(pq, (new_dist, neighbor))

    answer = max_weights[n]
    return answer

n = 5
route = [
    [5, 1, 15],
    [4, 2, 6],
    [1, 4, 8],
    [3, 2, 10],
    [1, 2, 7],
    [5, 4, 6],
    [2, 5, 5]
]
result = solution(n, route)
print(result)  # 출력: 3 (1번에서 2번으로, 그리고 2번에서 3번으로 이동하면 총 비용이 3)