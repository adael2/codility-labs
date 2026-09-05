def solution(A):
    B = set()
    for element in A:
        if element not in B:
            B.add(element)
        else:
            B.remove(element)
    return list(B)[0]