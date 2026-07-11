
def PatternProg(No):
    temp = 1
    for i in range(1,No+1):
        for j in range(1, i+1):      
            print(f"{j} ",end =" ")
        print()

def main():
    print("Enter pattern size:: ")
    No = int(input())
    PatternProg(No)

if __name__ == "__main__":
    main()
