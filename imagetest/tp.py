# print("Enter the value:")
# n = int(input())
# for i in range(0, n):
#     for j in range(0, i + 1):
#         print("*", end="")
#     print("")
# for i in range(2, n + 1):
#     for j in range(0, i  -1):
#         print("*", end="")
#     print("")

x = 65
for i in range(0, 5):
    for j in range(i, 5):
        a = chr(x + i)
        print(a, "", end="")
    print()