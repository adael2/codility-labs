def solution(S, P, Q):
    # Implement your solution here
    impact = { 
        "A": 1, 
        "C": 2, 
        "G": 3, 
        "T": 4, 
    }
    result = []
    for i in range(len(P)):
        sub = S[P[i]:Q[i]+1]
        for w in impact:
            if w in sub:
                result.append(impact[w])
                break
    return result