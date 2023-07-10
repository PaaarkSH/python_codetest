def solution(N, moves=None):
    posi = [0, 0]
    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    dic = {
        'U': 0,
        'D': 1,
        'L': 2,
        'R': 3,
    }

    for move in moves:
        direct = dic.get(move, 0)
        if 0 < posi[0] + dx[direct] < N:
            posi[0] += dx[direct]
        if 0 < posi[1] + dy[direct] < N:
            posi[1] += dy[direct]
    return [posi[0] + 1, posi[1] + 1]


print(solution(5, ['R', 'R', 'R', 'U', 'D', 'D']))
