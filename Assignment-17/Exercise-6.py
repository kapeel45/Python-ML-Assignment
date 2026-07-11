import Arithmatic

def PatterProg(No):
    for i in range(1,No+1):
        print("* "*No)
        No = No - 1

def main():
    print("Enter pattern size:: ")
    No = int(input())
    PatterProg(No)

if __name__ == "__main__":
    main()
