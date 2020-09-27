def isPalindrome(num):
    if str(num) == str(num)[::-1]:
        return "is a Palindrome"
    return "is not a Palindrome"

print("-----------------------------------------")
print("Checking if a number is palindrome or not")
print("-----------------------------------------")
while True:
    num = int(input("Enter a number: "))
    print(num, isPalindrome(num))

    print()
    check = input("Check another number? (yes/no) ")
    if check == "no":
        break
    print()
