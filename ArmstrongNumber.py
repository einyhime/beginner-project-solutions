def isArmstrong(num):
    digits = len(str(num))
    if sum(int(x)**digits for x in str(num)) == num:
        return "is an Armstrong Number."
    else:
        return "is not an Armstrong Number."

print("-----------------------------------------------")
print("Check if a number is an Armstrong Number or not")
print("-----------------------------------------------")

while True:
    num = int(input("Enter a number: "))
    print(num, isArmstrong(num))
    
    check = input("\nCheck another number? Press Q to quit. ")
    if check == 'q':
        break
