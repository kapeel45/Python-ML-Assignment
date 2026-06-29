# write a program which accepts one number and check whether its pallindrome or not.


def CheckPallindrome(no):    
    mult = 0
    while no != 0:
        mult = mult * 10 + no %10
        no = int(no/10)
    return mult

def main():
    print("Enter the number:: ")
    value = int(input())
    result = CheckPallindrome(value)
    if result == value:
        print("Given Number is Pallindrome")
    else:
        print("Given Number is Not Pallindrome")

if __name__ == "__main__":
    main()