import Arithmatic

def PatterProg(No):
    for i in range(1,5):
        print("* "*No)

def main():
    print("Enter pattern size:: ")
    No = int(input())
    PatterProg(No)

if __name__ == "__main__":
    main()
