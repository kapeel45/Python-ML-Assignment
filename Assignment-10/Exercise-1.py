# accept one number and print multiplication table of that number
def MultiplicationTable(no):
    i = 1
    while i < 11:
        print(no * i, end=" ")
        i = i + 1

def main():
    MultiplicationTable(int(input("Enter Number to get multiple table: ")))
    
if __name__ == "__main__":
    main()