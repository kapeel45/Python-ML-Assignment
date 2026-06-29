# write a program which accepts one number and prints that many numbers starting from 1.

def PrintFromOne(no):
    for i in range(1,no+1):
        print(i,end=" ")

def main():
    print("Enter a number:: ")
    num = int(input())
    
    PrintFromOne(num)

if __name__ == "__main__":
    main()