N = int(input())

exam = list(map(int, input().split()))
maxV = max(exam)

for idx in range(len(exam)):
    exam[idx] = (exam[idx] / maxV) * 100


print(sum(exam) / len(exam))