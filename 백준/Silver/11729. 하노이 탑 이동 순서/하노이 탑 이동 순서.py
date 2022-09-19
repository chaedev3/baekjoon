N = int(input())


def func(n, one, two, three):
    # 1 은 1 -> 3 이니까
    if n == 1:
        print(one, three)
    else:
        # 1 ~ (N-1)의 탑을 1-> 2 로 이동시킴
        func(n-1, one, three, two)
        print(one, three)
        # 2에 있는 걸 3으로 이동시킴
        func(n-1, two, one, three)


if N <= 20:
    print(2**N - 1)
    func(N, 1, 2, 3)