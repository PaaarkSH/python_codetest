

def binary_search(arr, target, start, end):
    if start > end:
        return
    mid = (start + end) // 2

    if arr[mid] == target:  # 찾으면 리턴
        return mid
    elif arr[mid] > target:  # 찾는값이 중간점보다 작으면
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid + 1, end)    


def binary_search_while(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:  # 찾으면 리턴
            return mid
        elif arr[mid] > target:  # 찾는값이 중간점보다 작으면
            end = mid - 1
        else:
            start = mid + 1
    return -1


arr = [
    1,3,5,7,9,11,13,15,17,19
]
print(binary_search(arr, 7, 0, 10-1))
print(binary_search_while(arr, 7, 0, 10-1))

