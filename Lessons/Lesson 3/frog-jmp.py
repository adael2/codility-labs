import math

def solution(X, Y, D):
    # Implement your solution here
    count = math.ceil((Y - X) / D)
    return count