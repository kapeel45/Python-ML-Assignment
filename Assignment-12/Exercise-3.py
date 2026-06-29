# write a program which accepts 2 numbers and prints Addition, Subtraction, Multiplication and Division.

def Division(no1, no2):
    if no2 == 0:
        print("Division by zero is not allowed.")
    else:
        print("Division of", no1, "and", no2, "is:", no1 / no2)

def Multiplication(no1, no2):
    print("Multiplication of", no1, "and", no2, "is:", no1 * no2)

def Subtraction(no1, no2):
    print("Subtraction of", no1, "and", no2, "is:", no1 - no2)

def Addition(no1, no2):
    print("Addition of", no1, "and", no2, "is:", no1 + no2)

def main():
    print("Enter first number:: ")
    num1 = int(input())

    print("Enter second number:: ")
    num2 = int(input())
    
    Addition(num1,num2)
    Subtraction(num1,num2)
    Multiplication(num1,num2)
    Division(num1,num2)

if __name__ == "__main__":
    main()