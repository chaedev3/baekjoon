def solution(s):
    answer = len(s)
    
    for step in range(1, (len(s) // 2) + 1):
        compressed = ''
        count = 1
        prev = s[0:step]
        
        for j in range(step, len(s) + 1, step):
            if prev == s[j:j+step]:
                count += 1
            else:
                if count >= 2:
                    compressed += str(count) + prev
                else:
                    compressed += prev
                count = 1 
                prev = s[j:j+step]
        if count >= 2:
            compressed += str(count) + prev
        else:
            compressed += prev
        answer = min(answer, len(compressed))
    return answer