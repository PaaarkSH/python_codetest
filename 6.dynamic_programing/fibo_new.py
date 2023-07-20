# res 변수를 decorator 안으로 넣어서 생성
def fibo_deco(fn):
    res = {}

    def inner(n):
        if not res.get(n):
            res[n] = fn(n)
        return res[n]

    return inner


@fibo_deco
def fibo(n):
    if n < 3:
        return 1
    return fibo(n - 1) + fibo(n - 2)


print(fibo(6))  # 1 1 2 3 5 8
