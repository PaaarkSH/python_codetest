def solution(S):
    str_list = [x for x in S]
    result = int(str_list[0])

    for ch in str_list[1:]:
        if int(ch) < 0 or result < 0:
            result += int(ch)
        else:
            result *= int(ch)
    return result


print(solution('02984'))  # 576
print(solution('567'))  # 210
