def greet():
    return "hello world!"

def add_five(num):
    return num + 5

def make_negative(number):
    return -abs(number)

def find_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def check_alive(health):
    return health > 0
