def solution(A, K):
    # Implement your solution here
    if not A:
        return A

    B = A.copy()
    size = len(A)

    for i in range(0, size):
        B[(i + K) % size] = A[i]

    return B