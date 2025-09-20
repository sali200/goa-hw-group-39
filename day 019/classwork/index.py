# 1. ცვლადში შეინახეთ რიცხვი, თუ ეს რიცხვი ნაკლები იქნება 18-ზე, დაპრინტეთ (underage), თუ იქნება 18-ის ტოლი, დაპრინტეთ (teen), თუ იქნება 18-ზე მეტი (adult). 

age = int(input('age: '))

if age < 18:
    print('underage')
elif age ==  18:
    print('teen')
else:
    print('adult')

# 2. მომხარებელს ცვლადში შემოატანინე რიცხვი, თუ ის რიცხვი უარყოფითია დაუპრინტე (negative), თუ დადებითია (positive), თუ ნულია (zero).

number = float(input("შეიყვანეთ რიცხვი: "))

if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")
