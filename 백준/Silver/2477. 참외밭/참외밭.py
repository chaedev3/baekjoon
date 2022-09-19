
K = int(input())
k_melon = [list(map(int, input().split())) for _ in range(6)]

width = 0
height = 0
for i in range(len(k_melon)):
    if k_melon[i][0] == 4:
        width += k_melon[i][1]
    elif k_melon[i][0] == 1:
        height += k_melon[i][1]

s_width = 0
s_height = 0
for idx in range(1, len(k_melon)-1):
    if k_melon[idx][0] == 3 or k_melon[idx][0] == 4:
        if k_melon[idx][1] < width:
            if k_melon[idx+1][1] < height and k_melon[idx-1][1] < height:
                s_width = k_melon[idx][1]

    elif k_melon[idx][0] == 1 or k_melon[idx][0] == 2:
        if k_melon[idx][1] < height:
            if k_melon[idx+1][1] < width and k_melon[idx-1][1] < width:
                s_height = k_melon[idx][1]

if k_melon[0][0] == 3 or k_melon[0][0] == 4:
    if k_melon[0][1] < width:
        if k_melon[1][1] < height and k_melon[-1][1] < height:
            s_width = k_melon[0][1]
elif k_melon[0][0] == 1 or k_melon[0][0] == 2:
    if k_melon[0][1] < height:
        if k_melon[1][1] < width and k_melon[-1][1] < width:
            s_height = k_melon[0][1]


if k_melon[-1][0] == 3 or k_melon[-1][0] == 4:
    if k_melon[-1][1] < width:
        if k_melon[0][1] < height and k_melon[-2][1] < height:
            s_width = k_melon[-1][1]
elif k_melon[-1][0] == 1 or k_melon[-1][0] == 2:
    if k_melon[-1][1] < height:
        if k_melon[0][1] < width and k_melon[-2][1] < width:
            s_height = k_melon[-1][1]

total = (width * height) - (s_width * s_height)

print(total * K)