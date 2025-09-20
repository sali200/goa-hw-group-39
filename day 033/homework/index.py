def join_strings(str1, str2):
    result = str1 + str2
    print("შეერთებული სტრინგი:", result)

def sum_elements(numbers):
    if len(numbers) >= 5:
        result = numbers[2] + numbers[3]
        print("მე-3 და მე-4 ელემენტის ჯამი:", result)
    else:
        print("სია უნდა შეიცავდეს მინიმუმ 5 ელემენტს.")

def km_to_meters(km):
    meters = km * 1000
    print(f"{km} კმ = {meters} მეტრი")

def max_number(a, b):
    bigger = max(a, b)
    print("უფრო დიდი რიცხვია:", bigger)

def reverse_string(text):
    reversed_text = text[::-1]
    print("შებრუნებული სტრინგი:", reversed_text)

join_strings("Goal", "-Oriented")              
sum_elements([10, 20, 30, 40, 50])             
km_to_meters(5)                               
max_number(12, 8)                              
reverse_string("Academy")                    