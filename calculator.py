num1=int(input("Enter frist number : "))
num2=float(input("Enter Second number : "))

Ajay=(input("Choose the operation (+,-,*,/,^): "))
if Ajay == '+':
    result = num1 + num2

elif Ajay== '-':
    result = num1 - num2

elif Ajay== '*':
    result = num1 * num2

elif Ajay== '/':
    result = num1 / num2  

elif Ajay== '^':
    result = num1 ** num2
else:
    print("Invaild input ")

print(f"The result is {result}")   