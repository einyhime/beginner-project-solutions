def isPrime(num):
    x = num - 1
    while x > 1:
        if num % x == 0: return False
        x -= 1
    return True

def no1Or7(num):
    return '1' not in str(num) and '7' not in str(num)

def sumDigits(num):
    return sum(int(x) for x in str(num)) <= 10

def firstTwo(num):
    return (int(str(num)[0]) + int(str(num)[1])) % 2 != 0

def secondToLast(num):
    x = int(str(num)[-2])
    return x % 2 == 0 and x > 1

def lastDigits(num):
    return int(str(num)[-1]) == len(str(num))

print("----------------")
print("WHAT'S MY NUMBER")
print("----------------")
print(
    """
Between 1 and 1000, there is only 1 number that meets the following criteria:

    The number has two or more digits.
    The number is prime.
    The number does NOT contain a 1 or 7 in it.
    The sum of all of the digits is less than or equal to 10.
    The first two digits add up to be odd.
    The second to last digit is even and greater than 1.
    The last digit is equal to how many digits are in the number.
    """
)

for num in range(10, 1001):
    if isPrime(num) and no1Or7(num) and sumDigits(num) and firstTwo(num) and secondToLast(num) and lastDigits(num):
        print("The number is:", num)
        break
    
