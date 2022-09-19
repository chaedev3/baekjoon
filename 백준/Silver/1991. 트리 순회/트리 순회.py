def preorder(n):
    if n > 0:
        print(chr(n + 64), end='')
        preorder(ch1[n])
        preorder(ch2[n])


def inorder(n):
    if n > 0:
        inorder(ch1[n])
        print(chr(n + 64), end='')
        inorder(ch2[n])


def postorder(n):
    if n > 0:
        postorder(ch1[n])
        postorder(ch2[n])
        print(chr(n+64), end='')


N = int(input())
ch1 = [0] * (N + 1)
ch2 = [0] * (N + 1)
for _ in range(N):
    a, b, c = map(str, input().split())
    if b != ".":
        ch1[ord(a) - 64] = ord(b) - 64
    if c != ".":
        ch2[ord(a) - 64] = ord(c) - 64

preorder(1)
print()
inorder(1)
print()
postorder(1)
