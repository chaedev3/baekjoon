T = int(input())
for tc in range(1, T+1):
    num = int(input())
    # abced 값 초기화
    a, b, c, d, e = 0, 0, 0, 0, 0
    # 2로 나누어 떨어질 때까지 num을 2로 나눔/ 나눠질 때마다 a에 1씩 더해줌 -> 2,3,5,7,11 똑같이 반복
    while num % 2 == 0:
        num //= 2
        a += 1
    while num % 3 == 0:
        num //= 3
        b += 1
    while num % 5 == 0:
        num //= 5
        c += 1
    while num % 7 == 0:
        num //= 7
        d += 1
    while num % 11 == 0:
        num //= 11
        e += 1

    print(f'#{tc} {a} {b} {c} {d} {e}')