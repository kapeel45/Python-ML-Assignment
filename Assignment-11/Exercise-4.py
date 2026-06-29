# write a program which accepts one number and prints reverse of the number.


def reverse(no):    
    while no != 0:
        print(int(no%10), end=" ")
        no = int(no/10)

def main():
    print("Enter the number:: ")
    result =reverse(int(input()))

if __name__ == "__main__":
    main()