# write a program which accepts one number and prints its factor.

def Factors(no):
    print("Factors of", no, "are:")
    for i in range(1,no+1):
        if no % i == 0:
            print(i,end=" ")

def main():
    print("Enter a number:: ")
    num = int(input())
    Factors(num)

if __name__ == "__main__":
    main()