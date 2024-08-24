def solution(M, load):
    from itertools import combinations

    n = len(load)
    max_mask = 1 << n
    dp = [float('inf')] * max_mask
    dp[0] = 0  # 아무 물건도 배치하지 않은 상태에서 0개의 트럭 사용

    for mask in range(max_mask):
        if dp[mask] == float('inf'):
            continue

        # 현재 상태에서 물건들을 배치하는 모든 가능한 조합을 시도
        for subset in range(1, max_mask):
            if (mask & subset) == 0:  # 현재 상태에서 subset의 물건들이 배치되지 않은 경우
                current_weight = 0
                for i in range(n):
                    if (subset & (1 << i)) != 0:
                        current_weight += load[i]

                # subset의 물건들을 하나의 트럭에 실을 수 있는지 확인
                if current_weight <= M:
                    dp[mask | subset] = min(dp[mask | subset], dp[mask] + 1)

    # 모든 물건이 배치된 상태의 최소 트럭 수를 반환
    result = dp[max_mask - 1]
    if result == float('inf'):
        result = [x for x in dp if x != float('inf')][-1]

    return result if result != 0 else -1


# # 테스트 케이스
# print("Test Case 0: ", solution(1, [2, 3, 7, 8]))  # Expected output: 2
# print("Test Case 1: ", solution(10, [2, 3, 7, 8]))  # Expected output: 2
# print("Test Case 2: ", solution(5, [2, 2, 2, 2, 2]))  # Expected output: 3
# print("Test Case 3: ", solution(20, [16, 15, 9, 17, 1, 3]))  # Expected output: 4
#
# # 추가 테스트 케이스
# print("Test Case 4: ", solution(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # Expected output: 6
# print("Test Case 5: ", solution(15, [5, 10, 15, 20, 25]))  # Expected output: 2

# 새로운 추가 테스트 케이스
print("Test Case 6: ", solution(4, [5, 5, 5]))  # Expected output: 3 (1+2+2+4+1, 8, 4)

