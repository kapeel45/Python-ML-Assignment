def LengthOfDigit(No):
    Count = 0
    while(No != 0):
        Count = Count + 1;
        No = int(No/10)
    return Count

def main():
    print("Enter pattern size:: ")
    No = int(input())
    iRet = LengthOfDigit(No)
    print("Length of Digits:: ", iRet)


if __name__ == "__main__":
    main()
