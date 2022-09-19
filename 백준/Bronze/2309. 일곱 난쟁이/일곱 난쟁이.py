height = []
for _ in range(9):
     height.append(int(input()))

gap = sum(height) - 100
a_list = []
b_list = []
for a in range(9):
    for b in range(9):
        if a != b:
            if height[a] + height[b] == gap:
                a_list.append(height[a])
                b_list.append(height[b])


height.remove(a_list[0])
height.remove(b_list[0])


for i in range(7):
    print(sorted(height)[i])