
def solution(N, lst):
    lst.sort()
    cnt = 0  # 포함된 모험가 수
    result = 0  # 총 그룹
    for s in lst:
        cnt += 1  # 사람을 넣고
        if cnt >= s:  # 공포
            result += 1
            cnt = 0
    return result


print(solution(5, [2, 3, 1, 2, 2]))

