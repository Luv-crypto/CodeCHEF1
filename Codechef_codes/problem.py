from random import randrange


a = int(input())
for i in range(a):
    a1, a2, a3 = map(int, input().split())
    if a2 < a1 and a2 < a3:
        print("Bob")
    elif a3 < a1 and a3 < a2:
        print("Alice")
    else:
        print("Draw")
