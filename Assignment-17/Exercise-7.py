import Arithmatic

def PatterProg(No):
    temp = No
    for i in range(1,No):
        for j in range(1, No +1):
            print(f"{j} ", end =" ")
        print()

def main():
    print("Enter pattern size:: ")
    No = int(input())
    PatterProg(No)

if __name__ == "__main__":
    main()
