


def solution(arr=[]):
    n = len(arr)  # 행
    m = len(arr[0])  # 열
    d = arr[::]

    for i in range(1, m):
        for j in range(n):
            
            sang = arr[j-1][i-1] if j > 1 else 0
            jung = arr[j][i-1]
            ha = arr[j+1][i-1] if j + 1 < n else 0
            d[j][i] += max(sang, jung, ha)

    result = 0
    for i in range(n):
        result = max(result, d[i][m-1])
    return result

arr = [
    [1, 3, 3, 2],
    [2, 1, 4, 1],
    [0, 6, 4, 7],
]
print(solution(arr))
