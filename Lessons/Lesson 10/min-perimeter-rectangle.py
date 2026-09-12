import math

def solution(N):
    # Implement your solution here
    start = int(math.sqrt(N))
    for i in range(start, 0, -1):
        if N % i == 0:
            return 2 * (i + N // i)