#write lambda function which accepts one number and return square of that number

Square = lambda No: No * No

def main():
    print("Enter number to square: ")
    No = int(input())
    iRet = Square(No)
    print(f"Square of No: {No} is {iRet}")

if __name__ == "__main__":
    main()