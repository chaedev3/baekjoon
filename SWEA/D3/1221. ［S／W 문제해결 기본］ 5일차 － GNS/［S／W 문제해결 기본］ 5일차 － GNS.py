T = int(input())


for t in range(1, T+1):
    tc, len_num = input().split()
    num_list = list(map(str, input().split()))
    zro_to_nin = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    a = ''

    for i in range(len(zro_to_nin)):
        for j in range(len(num_list)):
            if num_list[j] == zro_to_nin[i]:
                a += zro_to_nin[i] + ' '
    print(tc)
    print(a)