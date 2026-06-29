# Write a program which accepts one number and check if it is perfect number or not.

def Factors(no):
    sum = 0
    for i in range(1,no):
        if no % i == 0:
            sum = sum + i
    return sum

def main():
    print("Enter a number:: ")
    num = int(input())
    result = Factors(num)
    print("Sum of factors is:", result)
    if(result == num):
        print(num, "is a perfect number")
    else:
        print(num, "is not a perfect number")

if __name__ == "__main__":
    main()