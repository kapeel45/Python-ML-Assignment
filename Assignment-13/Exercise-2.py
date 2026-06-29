#Write a program which accepts radius of a circle and prints its area of circle.

def AreaOfCircle(radius):
    area = 2 * 3.14 * radius * radius
    return area

def main():
    print("Enter radius of the circle:: ")
    radius = int(input())
    area = AreaOfCircle(radius)
    print("Area of the circle is:: ", area)

if __name__ == "__main__":
    main()