# write a program which accepts one character and check whether its vowel or not.

def CheckVowels(ch):
    if ch in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False
def main():
    print("Enter a character:: ")
    ch = input()
    if CheckVowels(ch):
        print("Given character is a vowel")
    else:
        print("Given character is not a vowel")

if __name__ == "__main__":
    main()