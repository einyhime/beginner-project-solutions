heads = 35
legs = 94
chicken = heads - 1
rabbit = 1

print(f"Heads: {heads}, Legs: {legs}\n")

for _ in range(heads):
    if chicken * 2 + rabbit * 4 == legs:
	    print(f"Chickens: {chicken}\nRabbits: {rabbit}")
	    break
    chicken -= 1
    rabbit += 1