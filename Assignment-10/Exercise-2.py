# accept one number and print sum of first N natural number.
def SumOfN(no):
    i = 1
    sum =0
    while i < no:
        sum = sum + i
        i = i + 1
    return sum

def main():
    result = SumOfN(int(input("Enter Number to get sum of first N : ")))
    print("Sum of N is :", result)
    
if __name__ == "__main__":
    main()