# ar = [100000, 1000000, 1998383]


# def Averybigarrsum(ar):
#     sum = 0
#     for i in ar:
#         sum += i
#     print(sum)
#     return sum


# Averybigarrsum(ar)
# import itertools

# arr = [[1, 2, 3], [4, 5, 6], [7, 8, 1]]


# def getdiagdiff(arr):
#     primarysum = []
#     secondarysum = []
#     z = len(arr)
#     for i in range(z):
#         x = arr[i][i]
#         y = arr[i][z - i - 1]
#         primarysum.append(x)
#         secondarysum.append(y)
#         sum1 = 0
#         sum2 = 0
#         for i, j in zip(primarysum, secondarysum):
#             sum1 += i
#             sum2 += j
#             diff = (sum1) - (sum2)
#             if diff < 0:
#                 diff *= -1
#             else:
#                 pass
#     print(diff)
#     return diff


# getdiagdiff(arr)
# arr = [1, 1, 0, -1, -1]


# def getratioofarray(arr):
# a = 0
# b = 0
# c = 0
# x = 0
# y = 0
# z = 0
# n = len(arr)
# for i in arr:
#     if i > 0:
#         x += 1
#     if i < 0:
#         y += 1
#     if i == 0:
#         z += 1
# a = float(x / n)
# b = float(y / n)
# c = float(z / n)
# print("%.6f" % a)
# print("%.6f" % b)
# print("%.6f" % c)

# return (a, b, c)


# def getmaxmnin(arr):
#     listmin = 0
#     listmax = 0
#     arr.sort()
#     for i in range(4):
#         listmin += arr[i]
#     arr.sort(reverse=True)
#     for j in range(4):
#         listmax += arr[j]

#     print(listmin, listmax)
#     return listmin, listmax


# getmaxmnin(arr)candles = [1, 2, 3, 9, 9]

# grades = [38, 67, 69, 70, 74]


# def getgrades(grades):

#     x = 0
#     lista = []
#     for i in grades:
#         if i >= 38:
#             x = i // 5
#             x = x + 1
#             x = x * 5
#             if x - i >= 3:
#                 lista.append(i)

#             else:
#                 lista.append(x)

#         else:
#             lista.append(i)
#     print(lista)
#     return lista


# getgrades(grades)
# import itertools

# s = 7
# t = 11
# a = 5
# b = 15
# apples = [2, -2, 1]
# oranges = [5, -6]


# def getorangeandapple(s, t, a, b, apples, oranges):
#     m = 0
#     n = 0
#     for (i, j) in zip(apples, oranges):
#         if (a + i) >= s and (a + i) <= t:
#             m += 1
#             n += 1
#         print(m)
#         print(n)
#         return m, n


# getorangeandapple(s, t, a, b, apples, oranges)
# x1 = 0
# v1 = 2
# x2 = 5
# v2 = 3


# def kangaroo(x1, v1, x2, v2):
#     if x1 == x2 and v1 == v2:
#         print("YES")
#     elif x1 > x2 and v1 < v2:
#         print("YES")
#     elif x2 > x1 and v2 < v1:
#         print("YES")
#     else:
#         print("NO")


# kangaroo(x1, v1, x2, v2)

# scores = [5, 10, 4, 20, 20, 4, 5, 2, 25, 1]


# def getthetotal(scores):

#     mimscores = scores[0]
#     maxscores = scores[0]
#     n = 0
#     m = 0
#     for x in scores:
#         if x < mimscores:
#             m = m + 1
#             mimscores = x
#         if x > maxscores:
#             n = n + 1
#             maxscores = x
#     print(n, m)
#     return (n, m)


# getthetotal(scores)

# s = [2, 2, 1, 3, 2]
# m = 2
# d = 3


# def lilyisweird(s, d, m):
#     Totalways = 0

#     n = len(s)
#     while n >= m:
#         sum = 0
#         for i in range(m):
#             z = s[i]
#             sum = sum + z
#         if sum == d:
#             Totalways = Totalways + 1
#         s.remove(s[0])
#         n = n - 1

#     print(Totalways)
#     return Totalways


# lilyisweird(s, d, m)
# from collections import Counter

# s = "aaabbb"


# def gameofthrones(s):
#     add = 0
#     for x in Counter(s).values():
#         add += x % 2
#     return "NO" if add > 1 else "YES"


# print(gameofthrones(input())
# bill = [3, 10, 2, 9]
# k = 1
# b = 7


# def bonAppetitt(bill, k, b):
# sum1 = 0
# d = "Bon Appetit"
# bill.pop(k)
# for i in bill:
#     sum1 += i
# Total = int(sum1 / 2)

# if Total == b:
#     print(d)
# if Total != b:
#     a = b - Total
#     print(a)

#     return a


# bonAppetitt(bill, k, b)

# def sockMerchant(n, ar):
# f = 0
# a = ar.sort()
# v = set(ar)
# for x in v:
#     w = 0
#     q = 0
#     for y in ar:
#         if x == y:
#             w += 1
#     q = w // 2
#     f = f + q

# print(f)
# return f


# sockMerchant(n, ar)
# import itertools

# ar = [1, 3, 2, 6, 1, 2]
# n = 6
# k = 3


# def divisionofnum(n, k, ar):

# a = 0
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         sum1 = ar[i] + ar[j]
#         if (sum1) % k == 0:
#             a += 1
#     sum1 = 0

# print(a)
# return a


# divisionofnum(n, k, ar)
# n = int(input("ENter the value:"))

# if n % 2 == 0:
#     if n > 20:
#         print("Weird")
#     if n >= 2 and n <= 5:
#         print("Not Weird")
#     if n >= 6 and n <= 20:
#         print("Weird")
# else:
#     print("Weird")


# def isleap(year):
# leap = False
# leaps = True
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             return leaps
#         else:
#             return leap
#     else:
#         return leaps
# else:
#     return leap


# isleap(1900)

# x = 1
# y = 1
# z = 1
# n = 3
# print(
#     [
#         [i, j, k]
#         for i in range(0, x + 1)
#         for j in range(0, y + 1)
#         for k in range(0, z + 1)
#         if i + j + k != n
#     ]
# )


# arr = [2, 3, 6, 6, 5]
# n = set(arr)
# b = list(n)
# print(b[-2])

# string = "sarjesh"
# position = 3
# character = "v"


# def mutate_string(string, position, character):
#     l = list(string)
#     l[position] = character
#     string = "".join(l)
#     print(string)
#     return string


# mutate_string(string, position, character)


# line = "sarvesh is a bot"


# def split_and_join(line):
#     line = line.split(" ")
#     line = "-".join(line)
#     return line


# split_and_join(line)
# a = "Iam"
# b = "legend"


# def print_full_name(a, b):
#     print("Hello " + a + " " + b + " !You just delved into python.")


# print_full_name(a, b)

# import itertools

# string = "ABCDCDC"
# substring = "CDC"


# def getthestring(string, substring):
#     a = 0
#     for i in range(len(string)):
#         if string[i:].startswith(substring):
#             a += 1
#     print(a)
#     return a


# getthestring(string, substring)
# array = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174]


# def average(array):
#     a = set(array)
#     b = len(a)
#     c = sum(a)
#     average = c / b
#     print(average)

#     return average


# average(array)

# thickness = int(input())  # This must be an odd number
# c = "H"

# # Top Cone
# for i in range(thickness):
#     print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

# # Top Pillars
# for i in range(thickness + 1):
#     print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# # Middle Belt
# for i in range((thickness + 1) // 2):
#     print((c * thickness * 5).center(thickness * 6))

# # Bottom Pillars
# for i in range(thickness + 1):
#     print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# # Bottom Cone
# for i in range(thickness):
#     print(
#         (
#             (c * (thickness - i - 1)).rjust(thickness)
#             + c
#             + (c * (thickness - i - 1)).ljust(thickness)
#         ).rjust(thickness * 6)
#     )
# import textwrap

# string = "WJDEBKPKNFJOsfk"
# max_width = 4


# def wrap(string, max_width):
#     for i in textwrap.wrap(string, width=max_width):

#         return""


# wrap(string, max_width)

# list1 = [1, 2, 3, 5, 5]

# t = tuple(list1)
# print(hash(t))


# lista =[2]
# lista.append(lista.append(3))
# print(lista)

# n = int(input())

# for x in range(1, n + 1):
#     if x % 2 == 0:
#         print(x, "is even")
#     else:
#         print(x, "is odd")


# n = int(input())

# a = 0
# b = 1
# for i in range(n):
#     print(a)
#     c = a + b
#     a = b
#     b = c
#     i += 1


# print("Enter the value of n")
# n = int(input())
# arr = []

# for i in range(n):
#     print("Enter the elements")
#     elements = int(input())
#     arr.append(elements)

# max_element = arr[0]
# for i in range(n):
#     if arr[i] > max_element:
#         max_element = arr[i]
# print("The maximum element is:", max_element)

# min_element = arr[0]
# for j in range(n):
#     if arr[i] < min_element:
#         min_element = arr[i]
# print("The maximum element is:", min_element)

# sum1 = 0
# for x in range(n):
#     sum1 += arr[x]
# print("The sum of array is:", sum1)

# avg = sum1 / n
# print("The Average is:", avg)

# n = int(input())
# if n > 1:
#     for i in range(2, n):
#         if n % i == 0:
#             print("no is not prime")
#             break
#         else:
#             print("no is prime")
# else:
#     print("no is not prime")

# n = int(input())
# for i in range(1, 11):
#     print(n, "x", i, "=", n * i)


# def fib(n):
#     a = 0
#     b = 1
#     while a <= n:
#         print(a, end=" ")
#         c = a + b
#         a = b
#         b = c


# fib(10)


# def Reverse(n):
#     rev = 0
#     while n > 0:
#         remainder = n % 10
#         rev = (rev * 10) + remainder
#         n = n // 10
#     print(rev)


# Reverse(153)


# def fact(n):
#     if n >= 1:
#         x = 1
#         for i in range(1, n + 1):
#             x = x * i
#         print(x)

#     else:
#         print(n)


# fact(5)

# n = int(input())
# for i in range(0, n):
#     for j in range(0, i + 1):
#         print("*", end="")
#     print("")

# n = int(input())
# for i in range(0, n):
#     for j in range(0, i + 1):
#         print("*", end="")
#     print("")

# for i in range(0, n):
#     for j in range(i, n - 1):
#         print("*", end="")
#     print("")

# for i in range(1, 6):
#     for j in range(i, 6):
#         print("", j, end="")
#     print("")

# for i in range(1, 6):
#     for j in range(65, 65 + i):
#         a = chr(j)
#         print("", a, end="")
#     print("")

# num = 65
# for i in range(0, 5):
#     for j in range(i, 5):
#         n = chr(num + i)
#         print("", n, end="")
#     print("")


# n = int(input())

# sum1 = 0
# for i in range(1, n):
#     if n % i == 0:
#         sum1 += i
# if sum1 == n:
#     print("perfect")
# else:
#     print("not perfect")

# n = int(input("Enter Number of commands"))
# list=[]
#     for i in range(N):
#         s=input()
#         x=s.split()
#         if x[0] == "append":
#             z= int(x[1])
#             list.append(z)
#         if x[0] == "print":
#             print(list)
#         if x[0] == "remove":
#             z= int(x[1])
#             list.remove(z)
#         if x[0] == "sort":
#             list.sort()
#         if x[0] == "reverse":
#             list.reverse()
#         if x[0] == "pop":
#             list.pop()
#         if x[0] == "insert":
#             z= int(x[1])
#             y= int(x[2])
#             list.insert(z,y)

# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([15.168, 5.265, 20.901, 26.211, 0.704, 0.000010])
# ypoints = np.array([32.969, 10.6666, 44.581, 56.379, 1.368, 0.000010])
# plt.xlabel("Current")
# plt.ylabel("Power")
# plt.plot(xpoints, ypoints)
# plt.show()

# i = 4
# d = 4.0
# s = "HackerRank "
# a = 0
# b = 0.0
# f = ""
# s = "HackerRank"
# a = int(input())
# b = float(input())
# print(i + a)

# import numpy as np
# from scipy import stats
# N = int(input())
# arr = input()
# I = list(map(int,arr.split("")))
# mean = print((sum(I)/N))
# median  = print(np.median(I))
# mode = print(int(stats.mode(I)[0]))

#  d =z/2
#     a = []
#     b = []
#     if z % 2 != 0:
#         for i in range(0,(d)):
#             a.append(arr[i])
#         Q1  = statistics.median(a)
#         Q2  = arr[z/2]
#         for j in range ((d+1),n):
#             b .append(arr[j])
#         Q3 = statistics.median(b)
#     print(Q1)
#     print(Q2)
#     print(Q3)

# n, m = input().split()
# arr = input().split()
# A  = set(input().split())
# B = set(input().split())
# print(sum(i in A) - sum(i in B ) for i in arr)


# n = int(input())
# s = input().split()
# c = int(input())
# from itertools import combinations

# n = int(input())
# s = input().split()
# c = int(input())
# from itertools import combinations


# x = list(combinations(s, c))
# list1 = []
# for i in x:
#     for j in i:
#         if j == "a":
#             list1.append(j)
#             break
# prob = len(list1) / len(x)
# print(round(prob, 12))


# a = []
# b = []
# c = []
# d = []
# for i in sorted(input()):
#     if i.isalpha():
#         x = a if i.isupper() else b
#     else:
#         x = c if int(i) % 2 == 0 else d
#     x.append(i)
# print("".join(a + b + c + d))


# list1 = []
# for i in arr:
#     a = list1(i)
#     list1.append(a)
#     print(" ".join(list1[::-1])


# V = 4
# arr = [1, 4, 6, 5, 3]


# def introTutorial(V, arr):
#     # Write your code here
#     n = len(arr)
#     print(n)
#     for i in range(n ):
#         if arr[i] == V:
#             print(i)
#         else:
#             pass
#     return i


# introTutorial(V, arr)


# def sss(n, arr):
#     for i in range(1, n):
#         key = arr[i]
#         for j in range(0, n):
#             if arr[j] > key:
#                 key = arr[j+1]
#                 arr[j+1] == arr[j]


#     print(arr)


# sss(5, [5, 4, 2, 3, 1])


# def ss(n, arr):
#     for i in range(1, n):
#         k = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > arr[i]:
#             a = arr[j]
#             arr[j] = arr[i]
#             arr[i] = a
#             j = j - 1
#         print(arr)


# ss(5, [5, 4, 3, 2, 1])
def toString(List):
    return "".join(List)


# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.


def toString(List):
    return "".join(List)


# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
MAX_CHAR =

def factorial(n):

    fact = 1
    for i in range(2, n + 1):
        fact = fact * i
    return fact
def countDistinctPermutations(st):
    length = len(st)
    freq = [0] * MAX_CHAR  
    for i in range(0, length):
        if st[i] >= "a":
            freq[(ord)(st[i]) - 97] = freq[(ord)(st[i]) - 97] + 1
    fact = 1
    for i in range(0, MAX_CHAR):
        fact = fact * factorial(freq[i])
    return factorial(length) / fact
st = "abc"
print(countDistinctPermutations(st))
