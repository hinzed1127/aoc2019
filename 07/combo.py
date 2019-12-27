import itertools

phase_settings = [0, 1, 2, 3, 4]

# different syntax, same result
combos = [x for x in itertools.permutations(list(range(5)), 5)]
combos2 = list(itertools.permutations(phase_settings, 5))
print(len(combos))
print(len(combos))

for combo in combos:
    print(combo)
