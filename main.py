import addition # contains add function that returns sum of two numbers
import mod # contains mod function
import Multiplication
import subtraction
import division # contains division function
first = 99
second = 63

print(f"{first} + {second} = {addition.add(first,second)}")
print(f"{first} + {second} = {subtraction.subtraction(first, second)}")
print(f"{first} % {second} = {mod.mod(first,second)}")

print(f"{first} * {second} = {Multiplication.Multiplication(first,second)}")

print(f"{first} / {second} = {division.division(first,second)}")

