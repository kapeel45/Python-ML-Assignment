# accept one number and print even numbers till N number.
def AllEven(no):
    i = 2
    while i < no+1:
        if i % 2 == 0:
            print(i, end=" ")
        i = i + 1

def main():
    result = AllEven(int(input("Enter Number to get all even till that number : ")))

if __name__ == "__main__":
    main()