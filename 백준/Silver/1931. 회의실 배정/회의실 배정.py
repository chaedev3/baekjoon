N = int(input())

conference_time = [list(map(int, input().split())) for _ in range(N)]

sorted_conference_time = sorted(conference_time, key=lambda x: (x[1], x[0]))

cnt = 1
stack = [sorted_conference_time[0][1]]
for idx in range(1, len(sorted_conference_time)):
    if stack[-1] <= sorted_conference_time[idx][0]:
        cnt += 1
        stack.append(sorted_conference_time[idx][1])
print(cnt)


