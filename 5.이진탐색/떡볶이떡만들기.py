def solution(N, M, arr):
    arr.sort()
    start = arr[0]
    end = arr[len(arr)-1]

    result = 0
    while start <= end:
        mid = (start + end) // 2
        num = sum( x - mid if x > mid else 0 for x in arr)
        if num == M:
            return mid
        elif num > M:  # 자르고 남의 떡의 길이가 요구하는것보다 클때
            result = mid
            start = mid + 1
        else:  # 자르고 남은 떡의 길이가 요구하는것보다 작을때
            end = mid -1  # 끝점을 중간점의 왼쪽으로 옮김

    return result


arr = [19, 14, 10, 17]
print(solution(4, 6, arr))
