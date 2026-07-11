# Write a program which accepts marks and display Grades.

def Grades(marks):
    if marks >= 75 and marks < 100:
        print("Distinction")
    elif marks >= 60 and marks <= 75:
        print("First Class")
    elif marks >=50 and marks <= 60:
        print("Second Class")
    elif marks < 50:
        print("Fail")
    else: 
        print("Enter Valid Number")

def main():
    print("Enter Marks Here:: ")
    num = int(input())
    Grades(num)
    
if __name__ == "__main__":
    main()