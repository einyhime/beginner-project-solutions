def isPhytagoreanTriple(a, b , c):
    sides = sorted([a, b, c])
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return "is Phytagorean Triple."
    else:
        return "is not Phytagorean Triple."

print("---------------------------")
print("PHYTAGOREAN TRIPLES CHECKER")
print("---------------------------")

while True:
    try:
        a = int(input("Enter side 1: "))
        b = int(input("Enter side 2: "))
        c = int(input("Enter side 3: "))
        print(f"{a}, {b} and {c} {isPhytagoreanTriple(a, b, c)}")
    except:
        print("Invalid input")
        
    check = input("\nCheck another triple? Press Q to quit. ")
    if check == 'q':
        break
    print()
