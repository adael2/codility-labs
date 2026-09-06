def solution(A):
    sum_total = sum(A)
    
    sum_left = 0
    min_difference = float('inf') 
    
    for i in range(len(A) - 1):
        sum_left += A[i]
        sum_right = sum_total - sum_left
        difference = abs(sum_left - sum_right)
        if difference < min_difference:
            min_difference = difference
    return min_difference