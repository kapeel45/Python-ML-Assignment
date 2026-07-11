
def Factorial(No):
    fact = 1
    for i in range(1,No+1):
        fact = fact * i
    return fact

def main():
    print("Enter Number:: ")
    No = int(input())
    iRet = Factorial(No)
    print("Factorial is:: ", iRet)

if __name__ == "__main__":
    main()
