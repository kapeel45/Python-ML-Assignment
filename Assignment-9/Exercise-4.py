# accept one number and prints cube of that number
def Cube(no):
    return no * no * no

def main():
    result = Cube(int(input("Enter Number to Cube: ")))
    print("Cube of Number is:",result)

if __name__ == "__main__":
    main()