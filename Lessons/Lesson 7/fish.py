def solution(A, B):
    # Implement your solution here
    stack = []
    fish_count = 0

    for i in range(len(A)):
        if B[i] == 1:
            stack.append(A[i])
        else:
            while stack and stack[-1] < A[i]:
                stack.pop()
            if not stack:
                fish_count += 1
    return fish_count + len(stack)