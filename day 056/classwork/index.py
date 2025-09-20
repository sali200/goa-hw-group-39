def remainder(a, b):
    if a == 0 or b == 0:
        return -1
    larger = max(a, b)
    smaller = min(a, b)
    return larger % smaller

def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"


def is_uppercase(s):
    return s == s.upper()

