a = int(input())
for i in range(a):
    a1, a2 = map(int, input().split())
    c = a1 + a2
    b = str(c)
    A = 1
    result = []
    for i in range(0, len(b), A):
        result.append(int(b[i : i + A]))
        final = []
