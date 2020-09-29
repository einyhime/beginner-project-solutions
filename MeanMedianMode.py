import statistics

def meanFunc(lst, decimalPlace):
    if decimalPlace == 0:
        return sum(lst) / len(lst)
    else:
        return round(sum(lst) / len(lst), decimalPlace)

def medianFunc(lst):
    lst = sorted(lst)
    if len(lst) % 2:
        return lst[len(lst) // 2]
    else:
        return [lst[len(lst) // 2 - 1], lst[len(lst) // 2]]

def modeFunc(lst):
    
    setLst = list(set(lst))
    temp = [setLst[0]]
    for i in range(1, len(setLst)):
        if lst.count(setLst[i]) > lst.count(temp[0]):
            temp = [setLst[i]]
        elif lst.count(setLst[i]) == lst.count(temp[0]):
            temp.append(setLst[i])
    if len(temp) > 1:
        return temp
    else:
        return temp[0]

print("----------------------")
print("MEAN, MEDIAN AND MODE")
print("----------------------")

while True:
    lst, decimalPlace = [], 0
    user_input = input("Enter your list: ")
    dec_place = input("For mean func, how many decimal places you want the answer to be rounded to: ")
    
    lst = [int(x) for x in user_input if x.isdigit()]
    if dec_place.isdigit():
        dec_place = int(dec_place)

    print("Using the built in functions:")
    print(statistics.mean(lst))
    print(statistics.median(lst))
    print(statistics.mode(lst))

    print("\nUsing our functions: ")
    print(meanFunc(lst, dec_place))
    print(medianFunc(lst))
    print(modeFunc(lst))

    check = input("Calculate another list? Press Q to quit. ")
    if check == 'q':
        break