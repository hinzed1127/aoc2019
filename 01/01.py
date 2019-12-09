# import math

# fuel = 0
# file = open('masses.txt')
# for line in file:
# 	fuel += math.floor(int(line)/3) - 2

# print(fuel)

#part one
print(sum((int(line) // 3) - 2 for line in open('masses.txt')))


# part 2

def fuel(mass):
	fuel_mass = (mass // 3) - 2
	if fuel_mass <= 0:
		return 0
	else:
		return fuel_mass + fuel(fuel_mass)

print(sum(fuel(line) for line in open('masses.txt')))