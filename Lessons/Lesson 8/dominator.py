def solution(A):
    # Implement your solution here
    if not A:
        return -1
    
    dictionary = {}

    for index, item in enumerate(A):
        if item in dictionary:
            dictionary[item]['count'] += 1
        else:
            dictionary[item] = {'count': 1, 'index': index}

    max_value = max(dictionary, key=lambda x: dictionary[x]['count'])

    if dictionary[max_value]['count'] > (len(A) // 2):
        return dictionary[max_value]['index']
    else:
        return -1