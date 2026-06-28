# accept one number and print factorial of N number.
def Factorial(no):
    i = 1
    mult = 1
    while i < no+1:
        mult = mult * i
        i = i + 1
    return mult

def main():
    result = Factorial(int(input("Enter Number to get Factorial of : ")))
    print("Factorial of N is :", result)

if __name__ == "__main__":
    main()