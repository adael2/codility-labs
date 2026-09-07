def solution(A):
    # Implement your solution here
    left = 0
    total = 0
    for item in A:
        if item == 0:
            left += 1
        else:
            total += left
    if total > 1000000000:
        return -1
    return total