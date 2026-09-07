def solution(H):
    # Implement your solution here
    stack = []
    count = 0
    for height in H:
        while stack and stack[-1] > height:
            stack.pop()

        if not stack or stack[-1] < height:
            stack.append(height)
            count += 1
    return count