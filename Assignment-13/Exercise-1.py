#Write a program which accepts length and breadth of a rectangle and prints its area.

def AreaOfRectangle(length, breadth):
    area = length * breadth
    return area

def main():
    print("Enter length of the rectangle:: ")
    length = int(input())
    print("Enter breadth of the rectangle:: ")
    breadth = int(input())
    area = AreaOfRectangle(length, breadth)
    print("Area of the rectangle is:: ", area)

if __name__ == "__main__":
    main()