from __future__ import print_function

__author__ = 'kristof'

print("for loop")
for x in range(10, 20):
    if x % 2:
        continue
    print(x**2, end=' ')

print("\nwhile loop")
x = 10
while x < 20:
    print(x*x, end=' ')
    x+=1

print("\n")