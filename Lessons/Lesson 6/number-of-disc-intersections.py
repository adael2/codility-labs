def solution(A):
    # Implement your solution here
    start = []
    end = []

    for i, r in enumerate(A):
        start.append(i - r)
        end.append(i + r)
    start.sort()
    end.sort()
    j = 0
    intersections = 0
    disc = 0
    for i in range(len(A)):
        while j < len(A) and start[i] > end[j]:
            disc -= 1
            j += 1
        intersections += disc

        if intersections > 10000000 :
            return -1
        disc += 1
    return intersections