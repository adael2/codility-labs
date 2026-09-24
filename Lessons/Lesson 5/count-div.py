def solution(A, B, K):
    # Implement your solution here
    b = B // K
    a = A // K
    result = b - a
    if A % K == 0:
        result += 1
    return result
