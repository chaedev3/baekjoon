h, m = map(int, input().split())
min = int(input())
total_min = h * 60 + m 
oven_min = total_min + min 

if oven_min >= 1440:
    oven_min = oven_min - 1440 

print(oven_min // 60, oven_min % 60)