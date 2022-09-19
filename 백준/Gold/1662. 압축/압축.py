import sys

string = sys.stdin.readline().rstrip()
rep = []
chs = [0]
n = len(string)
i = 0

while i < n-1:
    if string[i].isdigit() and string[i+1].isdigit(): chs[-1] += 1
    elif string[i].isdigit() and string[i+1] == ')': chs[-1] += 1
    elif string[i].isdigit() and string[i+1] == '(':
        chs.append(0)
        rep.append(int(string[i])) 
    
    elif string[i] == ')':
        x = chs.pop() * rep.pop()
        if chs: x = chs.pop() + x
        chs.append(x)

    i += 1

if string[-1].isdigit(): chs[-1] += 1
else:
    x = chs.pop() * rep.pop()
    if chs: x = chs.pop() + x
    chs.append(x)

print(chs[0])