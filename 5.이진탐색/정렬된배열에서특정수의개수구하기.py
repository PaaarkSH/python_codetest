from bisect import bisect_left, bisect_right

def count_by_range(a, left, right):
    right_index = bisect_right(a, right)
    left_index = bisect_left(a, left)
    return right_index - left_index

arr = [1,1,2,2,2,2,3]
print(arr, 2, 2)
