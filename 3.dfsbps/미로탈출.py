from collections import deque

graph = [
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
]
N = 5
M = 6

queue = deque()
queue.append((0, 0))

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1 ,1]

while queue:
    x, y = queue.popleft()
    

        # 반복 안에서 이전 x y 와 움직인 이후의 xy가 둘다 있어야 이동한 값이 계산되서 그냥 append 만 해서는 안되서 
        # for 문으로 동서남북을 만든 이후에 append 해야겠네  

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] != 0:
            if graph[nx][ny] == 1:  # 최단 경로일때만 1 
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

print(graph[N-1][M-1])
print(graph)


