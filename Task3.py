# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
max = a
if b > max:
    max = b
if c > max:
    max = c
if d > max:
    max = d
if e > max:
    max = e
print(max)