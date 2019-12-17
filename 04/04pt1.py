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
    similar_adjacents = False

    for i in range(1, len(digits)):
        if digits[i-1] == digits[i]:
            similar_adjacents = True
        if digits[i-1] > digits[i]:
            return False

    return similar_adjacents


INPUT = "245182-790572"
print(password_generator(INPUT))
