#write lambda function which accepts one number and return if even number

CheckEven = lambda No : No % 2 == 0

def main():
    print("Enter number to Check Even: ")
    No = int(input())

    iRet = CheckEven(No)
    print(f"Check Even of {No}: is {iRet}")

if __name__ == "__main__":
    main()