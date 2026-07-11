import Arithmatic

def main():
    print("Enter Number 1: ")
    No1 = int(input())
    print("Enter Number 2: ")
    No2 = int(input())
    
    print("Addition Result:: ",Arithmatic.Add(No1,No2))
    print("Subtraction Result:: ",Arithmatic.Sub(No1,No2))
    print("Multiplication Result:: ",Arithmatic.Mult(No1,No2))
    print("Division Result:: ",Arithmatic.Division(No1,No2))

if __name__ == "__main__":
    main()
