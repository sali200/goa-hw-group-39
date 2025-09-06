def two_highest(arg1):
    return sorted(set(arg1), reverse=True)[:2]

def combine_names(first, last):
    return f"{first} {last}"

def generate_range(min_val, max_val, step):
    return list(range(min_val, max_val + 1, step))

def multiple_of_index(arr):
    return [val for idx, val in enumerate(arr) if idx != 0 and val % idx == 0]

def problem(a):
    return a * 50 + 6 if isinstance(a, (int, float)) else "Error"
