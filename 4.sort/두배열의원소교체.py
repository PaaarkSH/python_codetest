



def solution(N, K, arr=[]):
    a = arr[0]
    b = arr[1]

    a.sort()
    b.sort(reverse=True)
    for i in range(K):
        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]
        else:
            break
    return sum(a)


print(solution(5,3,[
    [1,2,5,4,3],
    [5,5,6,6,5],
]))