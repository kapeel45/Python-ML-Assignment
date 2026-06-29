# write a program which accepts one number and prints count of digits in that number.


def Count(no):
    count = 0
    while no != 0:
        no = int(no/10)
        count = count +1
    return count

def main():
    print("Enter the number:: ")
    result =Count(int(input()))
    print("Count of digits is:", result)

if __name__ == "__main__":
    main()