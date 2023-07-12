


d = [0] * 99
arr = [1, 3, 1, 5]
d[0] = arr[0]
d[1] = max(arr[0], arr[1])
N = len(arr)
for i in range(2, N):
    d[i] = max(d[i-1], d[i-2] + arr[i])
print(d[N-1])