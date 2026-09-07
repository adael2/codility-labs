def solution(A):
    # Implement your solution here
    B = set(A)
    for item in A:
        B.add(item)
    if len(B) != len(A):
        return 0
    sum_numbers = (max(B) * (max(B) + 1)) // 2
    if sum_numbers != sum(A):
        return 0
    return 1