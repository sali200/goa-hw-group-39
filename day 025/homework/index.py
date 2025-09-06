text = "Python"
print(text[1])  

a = 5
b = 7
print(a + b) 

first = "Hello"
second = "World"
print(first + " " + second) 



x = 10
y = 4
result = x / y
print(result)  

print(5 == 5)   
print(5 != 3)   
print(5 > 3)   
print(5 < 10)  
print(5 >= 5)   
print(3 <= 4)   


print(5 + 5 == 8 + 2)  

print(True and True)    
print(True and False)   
print(False and True)   
print(False and False)  

print(True or True)      # True
print(True or False)     # True
print(False or True)     # True
print(False or False)    # False

# 8. ლოგიკური + შედარების ოპერატორები
print(5 > 3 and 2 < 4)       # True
print(10 == 10 or 5 != 5)    # True
print(7 < 2 and 3 > 1)       # False
print(8 >= 8 or 1 == 0)      # True
print(not (4 == 4))          # False

# 9. for loop — 1-დან 10-მდე
for i in range(1, 11):
    print(i)

# 10. list-ის ელემენტების ჯამი
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(total)  # 15

# 11. სტრინგის თითოეული სიმბოლოს დაბეჭდვა
text = "Hello, World!"
for char in text:
    print(char)

# 12. while loop — 1-დან 10-მდე
i = 1
while i <= 10:
    print(i)
    i += 1

# 13. while loop — გამოტოვება 50-60
i = 1
while i <= 100:
    if 50 <= i <= 60:
        i += 1
        continue
    print(i)
    i += 1

# 14. while loop — ჯამი 50-მდე
i = 1
total = 0
while total < 50:
    total += i
    i += 1
print("ჯამი:", total)