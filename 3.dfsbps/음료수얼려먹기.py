
#
N = 4
M = 5
graph = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
]
result = 0
stack = []

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            stack.append([i, j])
        
        if stack:
            while stack:
                v = stack.pop()
                x = v[0]
                y = v[1]
                if 0 <= x < N and 0 <= y < M:
                    if graph[x][y] == 0:
                        graph[x][y] = 1
                        stack.append([x - 1, y])
                        stack.append([x, y - 1])
                        stack.append([x + 1, y])
                        stack.append([x, y + 1])
            result += 1


print(result)

