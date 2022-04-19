a = int(input())
for i in range(a):
    a1, a2, a3 = map(int, input().split())
    c = a2 * 1 + a3 * 2
    if c >= a1:
        print("Qualify")
    else:
        print("NotQualify")
