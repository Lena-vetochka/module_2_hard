import random
from dataclasses import replace

numbers_1 = random.randint(3, 20)
password = []

print(numbers_1)
a = numbers_1
for i in range(1, a // 2 + 1):
    for j in range(2, a):
        if a % (i + j) == 0 and i != j:
            password.append(i)
            password.append(j)

print('пароль: ', *password, sep='')
