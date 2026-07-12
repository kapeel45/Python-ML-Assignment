def AdditionOfDigit(No):
    Sum = 0
    Temp = 0

    while(No != 0):
        Temp = int(No % 10)
        Sum = Sum + Temp
        No = (No/10)
    return Sum

def main():
    print("Enter pattern size:: ")
    No = int(input())
    iRet = AdditionOfDigit(No)
    print("Sum of Digitis:: ", iRet)


if __name__ == "__main__":
    main()
