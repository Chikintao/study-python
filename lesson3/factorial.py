# Завдання: Обчислити факторіал заданого числа.


user_input = int(input())
factorial = 1

for i in range (2, user_input + 1):
    factorial *= i

print(factorial)