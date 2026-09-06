def solution(A):
    # Implement your solution here
    A.sort()
    size = len(A) + 1
    i = 1
    for element in A:
        if element != i:
            return i
        i += 1
    return size 