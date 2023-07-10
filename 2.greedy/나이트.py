
alpha = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
}

dxy = [
    [1, 2],
    [1, -2],
    [-1, 2],
    [-1, -2],
    [2, 1],
    [2, -1],
    [-2, 1],
    [-2, -1],
]

def solution(posi=''):
    cnt = 0
    x = alpha.get(posi[0])
    y = int(posi[1]) - 1

    for pin in dxy:
        dx = pin[0]
        dy = pin[1]
        if 0 < x + dx < 8 and 0 < y + dy < 8:
            cnt += 1
    return cnt


print(solution('a1'))  # 2


