#write lambda function which accepts one number and return if Odd number

CheckOdd = lambda No : No % 2 != 0

def main():
    print("Enter number to Check Odd: ")
    No = int(input())

    iRet = CheckOdd(No)
    print(f"Check Odd of {No}: is {iRet}")

if __name__ == "__main__":
    main()