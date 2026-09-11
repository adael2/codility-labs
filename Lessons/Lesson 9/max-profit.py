def solution(A):
    # Implement your solution here
    if len(A) < 2:
        return 0

    max_profit = 0
    min_price = A[0]

    for a in A:
        if a < min_price:
            min_price = a
        today_profit = a - min_price
        if today_profit > max_profit:
            max_profit = today_profit

    return max_profit