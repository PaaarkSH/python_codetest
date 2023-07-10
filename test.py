from itertools import permutations, combinations, product

data = ['a', 'b', 'c']

result1 = list(permutations(data, 2))
print(result1)  # 순열 

result2 = list(combinations(data, 2))
print(result2)  # 조합
