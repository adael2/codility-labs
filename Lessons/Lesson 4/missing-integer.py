def solution(A):
    # Implement your solution here
    count = 1
    B = set(A)
    B = sorted(B)
    for item in B:
        if item <= 0:
            continue
        if item != count:
            break
        count += 1
    return count