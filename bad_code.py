import random
import os

password = os.getenv("APP_PASSWORD")

a = 10
b = 0

try:
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")

for i in range(10):
    print("Hello")

x = 5
y = 10
z = x + y

count = 0
while count < 3:
    print(count)
    count += 1

numbers = [1, 2, 3, 4, 5]
random,shuffle(numbers)

print(numbers)
