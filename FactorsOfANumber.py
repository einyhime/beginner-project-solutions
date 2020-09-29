def factors(n):
    x = abs(n)
    lst = [num for num in range(1, x+1) if not x % num]
    if n == 0:
        return "0"
    elif n < 0:
        lst = [-num for num in lst]
    
    if len(lst) < 3:
        return str(n) + " is a prime number."
    return f"Factors of {n} are: " + makeString(lst)

def makeString(lst):
    string = ", ".join(str(i) for i in lst)
    return string


while True:
    try:
        num = int(input("Enter a number: "))
    except:
        num = 0
        print("Invalid number")
            
    print(factors(num))

    check = input("Try again? Press Q to quit. ")
    if check == 'q':
        break