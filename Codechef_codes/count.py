a = int(input())
for i in range(a):
    a1, a2, a3, a4, a5 = map(int, input().split())
    c = a1 + a2 + a3 + a4 + a5
    if c == 0:
        print("Beginner")
    elif c == 1:
        print("Junior Developer")
    elif c == 2:
        print("Middle Developer")
    elif c == 3:
        print("Senior Developer")
    elif c == 4:
        print("Hacker")
    else:
        print("Jeff Dean")
