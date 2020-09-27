x = 99
bottle = "bottles"

while x > 0:
    print(f"{x} {bottle} of beer on the wall, {x} {bottle} of beer.")
    print("Take one down, pass it around,")
    
    x -= 1
    if x == 1:
        bottle = "bottle"
    
    print(f"{x} {bottle} of beer on the wall\n")

print("No more bottles of beer on the wall, no more bottles of beer.")
print("Go to the store and buy some more, 99 bottles of beer on the wall...")
