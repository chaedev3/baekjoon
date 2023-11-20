def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        split_arr = sorted(array[i - 1: j])
        answer.append(split_arr[k - 1])
    return answer