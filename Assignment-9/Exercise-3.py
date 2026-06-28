# accept one number and prints square of that number
def Square(no):
    return no * no

def main():
    result = Square(int(input("Enter Number to Square: ")))
    print("Square of Number is:",result)

if __name__ == "__main__":
    main()