#write lambda function which accepts one number and return if even number

CheckDivisibleBy5 = lambda No : No % 5 == 0

def main():
    print("Enter number to Check Divisible by 5: ")
    No = int(input())

    iRet = CheckDivisibleBy5(No)
    if iRet == True:
        print(f"{No} is Divisible by 5")
    else:
        print(f"{No} is Not Divisible by 5")
if __name__ == "__main__":
    main()