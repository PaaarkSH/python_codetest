

"""
from collections import deque

def shortest_path_distances(grid, goals):
    def is_valid(x, y):
        return 0 <= x < N and 0 <= y < N and grid[x][y] != 1

    def bfs(start, goal):
        visited = [[False for _ in range(N)] for _ in range(N)]
        queue = deque([(start[0], start[1], 0)])  # (x, y, 거리) 정보를 큐에 넣음
        visited[start[0]][start[1]] = True

        while queue:
            x, y, distance = queue.popleft()

            if (x, y) == goal:
                return distance

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_x, new_y = x + dx, y + dy
                if is_valid(new_x, new_y) and not visited[new_x][new_y]:
                    queue.append((new_x, new_y, distance + 1))
                    visited[new_x][new_y] = True

        return float('inf')  # goal에 도달할 수 없는 경우 무한대 반환

    N = len(grid)
    result_grid = [[float('inf') for _ in range(N)] for _ in range(N)]

    for goal in goals:
        for i in range(N):
            for j in range(N):
                distance = bfs((i, j), goal)
                result_grid[i][j] = min(result_grid[i][j], distance)

    return result_grid

# 예제 사용법:
grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
goals = [(2, 2), (0, 2)]
result = shortest_path_distances(grid, goals)
for row in result:
    print(row)
"""

from collections import deque

def shortest(N, bus_stop):
    result_arr = [[float('inf')] * N for _ in range(N)]
    def validation(x, y):
        return 0 <= x < N and 0 <= y < N

    def bfs(goal):
        visited = [[False] * N for _ in range(N)]
        queue = deque([(goal[0], goal[1], 0)])
        visited[goal[0]][goal[1]] = True
        while queue:
            x, y, distance = queue.popleft()
            if (x, y) == goal:
                return distance

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_x, new_y = x + dx, y + dy
                if validation(new_x, new_y) and not visited[new_x][new_y]:
                    queue.append((new_x, new_y, distance + 1))
                    visited[new_x][new_y] = True

        return float('inf')
    for goal in bus_stop:
        distance = bfs((goal[0], goal[1]))

    return result_arr

def solution(N, bus_stop):
    answer = shortest(N, bus_stop)
    return answer


print(solution(3, [[1,2]]))
print(solution(3, [[1,2], [3,3]]))