from bisect import bisect_left, bisect_right

a = [1,2,4,4,8]
x = 4

# print(bisect_left(a, x))
# print(bisect_right(a, x))


def count_by_range(a, left, right):
    right_index = bisect_right(a, right)
    left_index = bisect_left(a, left)
    return right_index - left_index

arr = [1,2,3,3,3,3,4,4,8,9]
print(count_by_range(arr,4,4))
print(count_by_range(arr,-1,3))
