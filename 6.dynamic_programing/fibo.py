d = [0] * 100

# 탑다운
def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]
d[1] = 1
d[2] = 1

# 바텀업
def fibo_new(n):
    for i in range(3, n+1):
        d[i] = d[i-1] + d[i-2]
# print(fibo(99))
# print(fibo_new(99))


def fibo_count(x):
    print('f(' + str(x) + ')', end=' ')
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo_count(x-1) + fibo_count(x-2)
    return d[x]

fibo_count(6)