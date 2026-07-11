#write lambda function which accepts two number and return Minimum number

Min = lambda No1, No2: No1 < No2

def main():
    print("Enter number to Max: ")
    No1 = int(input())
    No2 = int(input())

    iRet = Min(No1,No2)
    if iRet == True:
        print(f"Minimum among No: {No1} and {No2} is {No1}")
    else:
        print(f"Minimum among No: {No1} and {No2} is {No2}")

if __name__ == "__main__":
    main()