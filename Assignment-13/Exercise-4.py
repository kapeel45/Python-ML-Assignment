# Write a program which accepts one number and prints binary equivalent.

def Binary(no):
    for i in range(4):
        print(int(no%2))
        no = no//2

def main():
    print("Enter a number:: ")
    num = int(input())
    Binary(num)
    
if __name__ == "__main__":
    main()