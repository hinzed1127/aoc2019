# orbits = [line for line in open('input.txt').read().strip().split('\n')]
# orbits = [str(line).strip() for line in open('input.txt')]


#reverse the orbits while parsing, that way we can use a dictionary to add up orbits
reversed_orbits = dict(line.strip().split(')')[::-1] for line in open('input.txt'))

# part 1
total_orbits = 0

for orbit in reversed_orbits.values():
    current_orbit = orbit
    while current_orbit != None:
        current_orbit = reversed_orbits.get(current_orbit)
        total_orbits +=1

print(total_orbits)

# part 2

def gather_orbits(start):
    current_orbit = reversed_orbits.get(start)
    steps = 0
    path = {}

    while current_orbit != None:
        current_orbit = reversed_orbits.get(current_orbit)
        steps += 1
        path[current_orbit] = steps
    
    return path
        
you_path = gather_orbits('YOU')
san_path = gather_orbits('SAN')
shared_path = (set(you_path.keys()).intersection(san_path.keys()))

min_transfers = 999999
for val in shared_path:
    transfers = you_path.get(val) + san_path.get(val)
    if transfers < min_transfers:
        min_transfers = transfers

print(min_transfers)
