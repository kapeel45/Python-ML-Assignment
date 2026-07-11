#write lambda function which accepts three numbers and return Largest No

Max = lambda No1, No2, No3 : No1 > No2 and No1 > No3 or No2 > No1 and No2 >No3 or No3 > No1 and No3 > No2

def main():
    print("Enter the first number: ")
    No1 = int(input())
    print("Enter the second number: ")
    No2 = int(input())
    print("Enter the third number: ")
    No3 = int(input())
    
    iRet = Max(No1, No2, No3)
    
if __name__ == "__main__":
    main()