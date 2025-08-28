# 1. სამი ქალაქის სახელი
city1 = "თბილისი"
city2 = "ბათუმი"
city3 = "ქუთაისი"
print(city1, city2, city3)

# 2. სახელი და გვარი
name = "ანა"
surname = "გიორგაძე"
full_name = name + " " + surname
print(full_name)

# 3. ორი რიცხვი და მათზე მოქმედებები
a = 10
b = 3
print("ჯამი:", a + b)
print("სხვაობა:", a - b)
print("ნამრავლი:", a * b)
print("განაყოფი:", a / b)

# 4. ერთი ცვლადის მნიშვნელობა მეორეს
x = 5
y = x
print("x =", x)
print("y =", y)

# 5. მომხმარებლის საყვარელი ფერი
favorite_color = input("შეიყვანე შენი საყვარელი ფერი: ")
print("შენი საყვარელი ფერია", favorite_color)

# 6. სტრინგი, მთელი და float
text = "Python"
integer = 42
decimal = 3.14
print(type(text))
print(type(integer))
print(type(decimal))

# 7. float → int
num_float = 7.89
num_int = int(num_float)
print("ორიგინალი:", num_float)
print("მთელი რიცხვი:", num_int)

# 8. მონაცემთა ტიპის შემოწმება
number = 100
print("ტიპი:", type(number))

# 9. არითმეტიკული მოქმედებები ცვლადებში
x = 8
y = 2
sum_result = x + y
diff_result = x - y
prod_result = x * y
div_result = x / y
print("შეკრება:", sum_result)
print("გამოკლება:", diff_result)
print("გამრავლება:", prod_result)
print("გაყოფა:", div_result)

# 10. სამი სტრინგის გაერთიანება
part1 = "მე"
part2 = "ვასწავლი"
part3 = "Python-ს"
sentence = part1 + " " + part2 + " " + part3
print(sentence)



# 11. ორი რიცხვი და შედარებები
num1 = 5
num2 = 10
print(num1 < num2)
print(num1 > num2)
print(num1 <= num2)
print(num1 >= num2)
print(num1 == num2)
print(num1 != num2)

# 12. ასაკების შედარება
age1 = 25
age2 = 30
print("age1 > age2:", age1 > age2)
print("age1 >= age2:", age1 >= age2)

# 13. სამი რიცხვი და შედარებები
a = 3
b = 7
c = 12
print("a < b:", a < b)
print("b < c:", b < c)

# 14. ორი სტრინგის შედარება
str1 = "apple"
str2 = "banana"
print("ტოლობა:", str1 == str2)
print("უტოლობა:", str1 != str2)