from collections import deque

def shortest(N, bus_stop):
    result_arr = [[601 for _ in range(N)] for _ in range(N)]
    destinations = set((x - 1, y - 1) for x, y in bus_stop)

    def validation(x, y):
        return 0 <= x < N and 0 <= y < N

    def bfs(start, bus_stop):
        visited = [[False for _ in range(N)] for _ in range(N)]
        queue = deque([(start[0], start[1], 0)])
        visited[start[0]][start[1]] = True
        while queue:
            x, y, distance = queue.popleft()
            # 이거 좌표가 뭔가 계속 안맞더라...
            if (x, y) in destinations:
                return distance
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_x, new_y = x + dx, y + dy
                if validation(new_x, new_y) and not visited[new_x][new_y]:
                    queue.append((new_x, new_y, distance + 1))
                    visited[new_x][new_y] = True
        return 601

    for i in range(N):
        for j in range(N):
            result_arr[i][j] = bfs((i, j), bus_stop)
            # distance = bfs((i, j), bus_stop)
    return result_arr

def solution(N, bus_stop):
    answer = shortest(N, bus_stop)
    return answer