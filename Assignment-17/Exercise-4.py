
def FactorialAddition(No):
    sum = 0
    for i in range(1,No):
        if No % i == 0:
            sum = sum + i
    return sum

def main():
    print("Enter Number:: ")
    No = int(input())
    iRet = FactorialAddition(No)
    print("Factorial Addition is:: ", iRet)

if __name__ == "__main__":
    main()
