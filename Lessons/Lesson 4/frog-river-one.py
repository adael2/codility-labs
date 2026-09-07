def solution(X, A):
    # Implement your solution here
    positions = set()
    for sec, item in enumerate(A):
        if item <= X:
            positions.add(item)
        
        if len(positions) == X:
            return sec
    return -1