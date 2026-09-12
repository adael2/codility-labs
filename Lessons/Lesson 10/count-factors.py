def solution(N):
    # Implement your solution here
    count = 0
    i = 1
    while i * i <= N:
        if N % i == 0:
            count += 1
            if i != N // i:
                count += 1
        i += 1
    return count