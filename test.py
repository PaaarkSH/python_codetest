def solution(A):
    prev, diff = -1, 10 ** 9
    A.sort()
    for a in A:
        if prev != -1:
            diff = min(diff, abs(a - prev))
        prev = a
    return diff if len(set(A)) != 1 else 0


print(solution([1, 1]))
print(solution([1, 1, 1, 5]))
print(solution([10, 5]))
print(solution([9, 11, 7]))
print(solution([7, 13, 10]))  # 7 10 13

