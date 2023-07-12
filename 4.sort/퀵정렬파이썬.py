arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]  # 피벗
    tail = arr[1:]  # 피벗을 제외한 리스트

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)
    

print(quick_sort(arr))