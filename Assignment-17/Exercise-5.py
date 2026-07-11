
def Prime(No):
    temp = int(No/2)
    for i in range(2, temp):
        if No % i == 0:
            return False;
    return True;

def main():
    print("Enter Number:: ")
    No = int(input())
    iRet = Prime(No)
    if iRet == True:
        print(f"{No} is Prime ")
    else:
        print(f"{No} is Not Prime")

if __name__ == "__main__":
    main()
