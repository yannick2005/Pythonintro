first_num = int(input("Enter the first number. "))
second_num = int(input("Enter the second number. "))
arithmetic_operation = input("Enter the arithmetic operation +,-,*,/ ")

if arithmetic_operation == "+":
    print(first_num + second_num )
elif arithmetic_operation == "-":
    print(first_num - second_num )
elif arithmetic_operation == "*":
    print(first_num * second_num )
elif arithmetic_operation == "/":
    print(first_num / second_num )
else:
    print("Invalid operation ")