import heapq

# 오름차순 힙 정렬
def heapsort_asc(arr):
    h = []
    result = []
    for v in arr:
        heapq.heappush(h, v)
    
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result


# 내름차순 힙 정렬
def heapsort_desc(arr):
    h = []
    result = []
    for v in arr:
        heapq.heappush(h, -v)
    
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result


result = heapsort_asc([1,3,5,7,9,2,4,6,8,0])
result = heapsort_desc([1,3,5,7,9,2,4,6,8,0])

print(result)
