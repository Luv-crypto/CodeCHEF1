a = int(input())
for i in range(a):
    b = int(input())
    c = b % 4
    if c == 0:
        print("North")
    elif c == 3:
        print("West")
    elif c == 2:
        print("South")
    else:
        print("East")
