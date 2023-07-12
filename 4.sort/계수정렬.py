arr = [7,5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

cnt = [0] * (max(arr) + 1)   # 0으로 초기화

for i in range(len(arr)):
    cnt[arr[i]] += 1  # 각 데이터에 해당하는 인덱스 증가

for i in range(len(cnt)):
    for j in range(cnt[i]):
        print(i, end=' ')
