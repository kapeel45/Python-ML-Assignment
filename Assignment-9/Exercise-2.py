def CheckGreater():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number:"))

    if num1 > num2:
        return num1
    else:
        return num2
    
def main():
    result = CheckGreater()
    print("The Greater Number is:",result)

if __name__ == "__main__":
    main()