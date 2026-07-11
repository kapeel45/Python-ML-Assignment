
def isPositiveOrNegative(No):
        if No > 1:
            print("No is Positive")
        elif No < 0:
            print("no is Negative")
        else:
            print("No is Zero")

def main():
    no = int(input("Enter Number: "))
    isPositiveOrNegative(no)

if __name__ == "__main__":
    main()