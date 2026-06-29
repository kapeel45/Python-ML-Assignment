# write a program which accepts one number and prints that many numbers in reverse order.

print("+"*40)
print("+ Input: 5")
print("+ Output: 5 4 3 2 1")
print("+"*40)

def PrintReverseTillOne(no):
    for i in range(no,0, -1):
        print(i,end=" ")

def main():
    print("Enter a number:: ")
    num = int(input())
    
    PrintReverseTillOne(num)

if __name__ == "__main__":
    main()