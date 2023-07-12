arr = [15, 11, 4, 8, 5, 2, 4]
# 순서를 뒤집어 '최장 증가 수열' 문제로 변환
n = len(arr)
arr.reverse()

d = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if arr[j] < arr[i]:
            d[i] = max(d[i], d[j] + 1)


print(n - max(d))