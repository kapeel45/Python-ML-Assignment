# accept one number and check whether divisible by 3 and 5
def DivisibleBy3And5(no):
    return no % 3 == 0 and no % 5 == 0

def main():
    result = DivisibleBy3And5(int(input("Enter Number to check divisible by 3 and 5: ")))
    if result == True:
        print("Number is Divisible by 3 and 5")
    else:
        print("Number Not Divisible by 3 and 5")

if __name__ == "__main__":
    main()