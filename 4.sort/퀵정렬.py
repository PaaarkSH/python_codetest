arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = start  # 피벗은 첫 원소
    left = start + 1  # 왼쪽
    right = end  # 오른쪽

    while (left <= right):  # 분할이 되기 전까지
        # 왼쪽에서는 자기보다 큰 값을 가질때까지 반복
        while (left <= end and arr[left] <= arr[pivot]):
            left += 1
        # 오른쪽에서는 자기보다 작은 값을 가질 때 까지 반복
        while (right > start and arr[right] >= arr[pivot]):
            right -= 1
        if (left > right):  # 엇갈리면 피벗이랑 right 를 교채
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    # 분할 과정이 됬다면
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


quick_sort(arr, 0, len(arr) - 1)
print(arr)
