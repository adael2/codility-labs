def solution(A):
    # Implement your solution here
    A.sort()
    negative_product = A[0] * A[1] * A[-1]
    positive_product = A[-1] * A[-2] * A[-3]
    return max(negative_product, positive_product)