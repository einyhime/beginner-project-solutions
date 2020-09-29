def fib(n):
    if n < 3: 
        return 1
    elif n <= 0:
        return 0
    else: 
        return fib(n-1) + fib(n-2)

print("-------------------")
print("FIBONACCI SEQUENCE")
print("-------------------")

lst = [1, 1]
print("The first 10 numbers are:")
for i in range(2, 10):
    lst.append(lst[i-1] + lst[i-2])
print(lst)

while True:
    try:
        num = int(input("Enter a number: "))
    except:
        num = 0
        print("Invalid number.")

    print(f"{num}\t: {fib(num)}")

    check = input("Try again? Press Q to quit. ")
    if check == 'q':
        break