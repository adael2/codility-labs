def solution(S):
    # Implement your solution here
    stack = []
    partners = {')': '(', ']': '[', '}': '{'}
    for s in S:
        if s in {'(', '[', '{'}:
            stack.append(s)
        else:
            if not stack:
                return 0
            partner = stack.pop()
            if partner != partners[s]:
                return 0
    if not stack:
        return 1
    else:
        return 0