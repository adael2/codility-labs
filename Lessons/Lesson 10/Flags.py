def solution(A):
    # Implement your solution here
    peaks = []
    for i in range(1, len(A) - 1):
        if A[i] > A[i - 1] and A[i] > A[i + 1]:
            peaks.append(i)
    if len(peaks) <= 1:
        return len(peaks)
    flags = int((len(A))**0.5) + 1

    for k in range(flags, 0, -1):
        flag_counter = 1
        last_peak_with_flag = peaks[0]

        for i in range(1, len(peaks)):
            if peaks[i] - last_peak_with_flag >= k:
                flag_counter += 1
                last_peak_with_flag = peaks[i]
                if flag_counter == k:
                    break
        if flag_counter >= k:
            return k
    return 0