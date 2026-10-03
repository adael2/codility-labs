def Solution(A):
    n = len(A)
    max_ending_here = [0] * n
    max_starting_here = [0] * n

    for i in range(1, n - 1):
        max_ending_here[i] = max(0, max_ending_here[i - 1] + A[i])

    for i in range(n - 2, 0, -1):
        max_starting_here[i] = max(0, max_starting_here[i + 1] + A[i])

    max_double_slice_sum = 0
    for i in range(1, n - 1):
        max_double_slice_sum = max(max_double_slice_sum, max_ending_here[i - 1] + max_starting_here[i + 1])

    return max_double_slice_sum