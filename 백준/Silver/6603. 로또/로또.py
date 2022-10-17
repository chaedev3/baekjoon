'''
input
7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0

조건
1. 1 - 49 중 6개를 고름
2. 49 가지 중 k 개 (k > 6) 개의 수를 골라 집합 S를 만든 후 그 수만 가지고 번호를 선택함
3. S, k 가 주어졌을 때 수를 고르는 모든 방법을 구하는 프로그램 작성해라 (숫자는 오름차순 정렬해서 출력)
'''


def recursion(depth, smallest):
    if depth == 6:
        print(*result)
        return

    for i in range(smallest, k):
        result.append(S[i])
        recursion(depth + 1, i + 1)
        result.pop()


# 0 이 나오면 멈춰야 하니까 while 문으로 작성
while True:
    # input 받기 - list 전체로 받아주고 맨 앞 pop (k)
    S = list(map(int, input().split()))
    k = S.pop(0)

    # 마지막 줄에 0만 받았다면 pop을 했으니 남은 게 없는 상황 -> break
    if not S:
        break

    # 결과를 담을 result
    result = []

    recursion(0, 0)
    print()