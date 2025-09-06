from datetime import datetime

def divide_numbers(a, b):
    if b != 0:
        result = a / b
        print("განაყოფი არის:", result)
    else:
        print("ნულზე გაყოფა არ შეიძლება.")

def greet_user(name):
    print(f"გამარჯობა, {name}! მიხარია შენი ნახვა.")

def calculate_age(birth_year):
    current_year = datetime.now().year
    age = current_year - birth_year
    print("თქვენი ასაკია:", age)

def multiply_by_five(number):
    result = number * 5
    print("რიცხვი გამრავლებული 5-ზე:", result)

def user_info():
    age = int(input("შეიყვანე ასაკი: "))
    name = input("შეიყვანე სახელი: ")
    print(f"მომხმარებლის სახელი არის {name}, და ის არის {age} წლის.")

