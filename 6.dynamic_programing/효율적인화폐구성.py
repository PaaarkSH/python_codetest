n = 2
m = 15
arr = [2,3]

d = [-1] * (m + 1)

d[0] = 0
for i in range(n):  # 화폐 가치를 보면서
    for j in range(arr[i], m + 1 ):  # 회폐 시작에서 만들어야되는 끝값까지
        if d[j -arr[j]] != -1:  # 화폐 가치 만큼 떨어진 곳에서 무한 값이 아닌 값이 있다면?
            d[j] = min(d[j], d[j-arr[i]] + 1)  # 마지막 전이라는게 결국 m까지 도달하면 1을 더할거라서


print(d[m])
