# 1. დაპრინტეთ 10-მდე რიცხვები
for i in range(1, 11):
    print(i)

# 2. დაპრინტეთ 20-მდე რიცხვები
for i in range(1, 21):
    print(i)

# 3. დაპრინტეთ 'GOA Best' 10-ჯერ
for i in range(10):
    print("GOA Best")

# 4. მომხმარებლის სახელის შემოტანა და 5-ჯერ დაბეჭდვა
name = input("შეიყვანე შენი სახელი: ")
for i in range(5):
    print(f"hello {name}")

# 5. 20-მდე რიცხვები, თითოეული გაყოფილი 2-ზე
for i in range(1, 21):
    print(i / 2)

# 6. 15-მდე რიცხვები, თითოეული გამრავლებული 2-ზე
for i in range(1, 16):
    print(i * 2)


# 7. 10-მდე რიცხვების კვადრატი
for i in range(1, 11):
    print(i ** 2)

# 8. 10-მდე რიცხვების ჯამი
sum = 0
for i in range(1, 11):
    sum += i
print("ჯამი:", sum)