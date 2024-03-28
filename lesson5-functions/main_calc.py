#sum sub mult divid

import calculator

num1 = int(input())
num2 = int(input())

sum = calculator.add(num1,num2)
subtract = calculator.subtract(num1,num2)
multiply = calculator.multiply(num1,num2)
divide = calculator.divide(num1,num2)

print(f"Сумма: {sum}" )
print(f"Різниця: {subtract}" )
print(f"Множення: {multiply}" )
print(f"Ділення: {divide}" )