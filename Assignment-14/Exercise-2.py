#write lambda function which accepts one number and return Cube of that number

Cube = lambda No: No * No

def main():
    print("Enter number to cube: ")
    No = int(input())
    iRet = Cube(No)
    print(f"Cube of No: {No} is {iRet}")

if __name__ == "__main__":
    main()