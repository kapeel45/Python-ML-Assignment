# write a program which accepts one number and checks wheter it is prime or not
# def Prime(no):
#     i = 2
#     while i <  int(no/2):
#         if no % i == 0:
#             return False
#         i = i + 1
#     return True

def Prime(no):
    for i in range(2,int(no/2), 2):
        if no % i == 0:
            return False
    return True

def main():
    result = Prime(int(input("Enter no to check Prime :")))
    if result == True:
        print("Given Number is Prime")
    else:
        print("Given Number is Not Prime")

if __name__ == "__main__":
    main()

