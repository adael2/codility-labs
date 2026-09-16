def solution(N, A):
    # Implement your solution here
    B = [0] * N
    current_max = 0
    last_max_applied = 0

    for item in A:
        if 1 <= item <= N:
            idx = item - 1
            if B[idx] < last_max_applied:
                B[idx] = last_max_applied
            B[idx] += 1
            if B[idx] > current_max:
                current_max = B[idx]
        else:
            last_max_applied = current_max
    for i in range(N):
        if B[i] < last_max_applied:
            B[i] = last_max_applied
    return B