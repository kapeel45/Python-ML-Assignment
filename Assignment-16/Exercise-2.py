
def ChkNum(iNo):
    if iNo % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

if __name__ == "__main__":
    print("Enter Number:: ")
    No = int(input())
    ChkNum(No)
