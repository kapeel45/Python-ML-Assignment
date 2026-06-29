# write a program which accepts one number and prints sum of digits of that number.


def SumOfDigit(no):
    sum = 0
    while no != 0:
        sum = sum + no%10
        no = int(no/10)
    return sum

def main():
    print("Enter the number:: ")
    result = SumOfDigit(int(input()))
    print("Sum of digits is:", result)

if __name__ == "__main__":
    main()