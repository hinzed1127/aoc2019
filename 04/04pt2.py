def password_generator(pw_range):
    start, end = [int(n) for n in pw_range.split('-')]

    valid_pws = 0
    curr = start

    while curr <= end:
        if isValidPassword(curr):
            valid_pws += 1
        curr += 1

    return valid_pws


def isValidPassword(num):
    digits = [int(x) for x in str(num)]

    return never_decreasing(digits) and valid_adjacents(digits)


def never_decreasing(digits):
    for i in range(1, len(digits)):
        if digits[i-1] > digits[i]:
            return False
    return True


def valid_adjacents(digits):
    repetitions = []
    curr_rep = 1
    for i in range(0, len(digits) - 1):
        if digits[i] == digits[i + 1]:
            curr_rep += 1
        else:
            repetitions.append(curr_rep)
            curr_rep = 1

    if curr_rep > 1:
        repetitions.append(curr_rep)

    return repetitions.count(2) > 0


INPUT = "245182-790572"
print(password_generator(INPUT))
