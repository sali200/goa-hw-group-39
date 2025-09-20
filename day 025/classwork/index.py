my_list = ["თამარი", "ნიკო", "მარიამი", "გიორგი", "ანა"]

print("მესამე ელემენტი:", my_list[2])  
print("მეოთხე ელემენტი:", my_list[3])  


numbers = [10, 25, 30, 45, 60]

user_input = int(input("შეიყვანე რიცხვი სიიდან: "))

if user_input in numbers:
    index = numbers.index(user_input)
    print(f"რიცხვი {user_input} არის ინდექსზე: {index}")
else:
    print("ეს რიცხვი სიაში არ მოიძებნა.")