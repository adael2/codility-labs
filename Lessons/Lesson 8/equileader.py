def solution(A):
    # Implement your solution here
    if not A or len(A) < 2:
        return 0

    dictionary = {}

    for item in A:
        dictionary[item] = dictionary.get(item, 0) + 1

    max_value = max(dictionary, key=dictionary.get)
    leader_count = dictionary[max_value]

    if leader_count <= (len(A) // 2):
        return 0

    count = 0
    leader_left_count = 0
    size = len(A)
    
    for i in range(size - 1):
        if A[i] == max_value:
            leader_left_count += 1

        leader_right_count = leader_count - leader_left_count

        if leader_left_count > (i + 1) // 2 and leader_right_count > (size - i - 1) // 2:
            count += 1
    return count