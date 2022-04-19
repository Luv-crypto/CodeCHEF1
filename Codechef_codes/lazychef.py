a = int(input())
for i in range(a):
    a1, a2, a3 = map(int, input().split())
    b = a1 * a2
    c = a1 + a3
    print(min(b, c))
