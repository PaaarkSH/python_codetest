def solution(A):
    a.sort()
    left, right = A[0], A[-1]
    pivot = (right + left) / 2
    left_boat = []
    right_boat = []
    for i, v in enumerate(hole):
        if pivot < v:
            right_boat.append(v)
        else:
            left_boat.append(v)

    left_boat_length = 1 if len(left_boat) <= 1 else left_boat[-1] - left_boat[0]
    right_boat_length = 1 if len(right_boat) <= 1 else right_boat[-1] - right_boat[0]
    ans = max(left_boat_length, right_boat_length)
    return ans