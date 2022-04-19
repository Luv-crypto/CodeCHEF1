a1, a2, a3 = map(int, input().split())
for i in range(a1):
    b1, b2, b3, b4, b5 = map(int, input().split())
    if b1 + b2 + b3 + b4 >= 8 and b5 <= 10:
        sum = 0
        sum += 1
print(sum)
