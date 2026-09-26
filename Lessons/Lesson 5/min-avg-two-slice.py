def solution(A):
    # Implement your solution here
    min_avg = (A[0] + A[1]) / 2
    min_index = 0

    for i in range(len(A) - 1):
        avg = (A[i] + A[i + 1]) / 2
        if avg < min_avg:
            min_avg = avg
            min_index = i

        if i < len(A) - 2:
            avg = (A[i] + A[i + 1] + A[i + 2]) / 3
            if avg < min_avg:
                min_avg = avg
                min_index = i

    return min_index