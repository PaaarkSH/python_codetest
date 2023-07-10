# n 과 k를 입력 받는다고 가정
n = 25
k = 3
result = 0

while True:
    target = (n // k) * k  # n을 k로 나눠서 만약 나눠 떨어지지 않더라도 가장 근처의 수를 찾음
    result += (n - target)
    n = target
    # 지금 나눠 떨어진다면 아무일이 없지만 안나눠 진다면 1을 빼는것과 같음
    # 따라서 n 이 k 로 나눠떨어지는 값을 찾는것과 같음

    if n < k:  # n이 k 보다 작을 때 반복 탈출
        break

    result += 1
    n //= k

result += (n - 1)
print(result)

