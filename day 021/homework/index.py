numbers = [3, 7, 12, 5, 9]
result = numbers[0] * numbers[3]
print("ნამრავლი არის:", result)


words = ["ვაშლი", "მსხალი", "ბანანი", "ატამი", "კივი", "ალუბალი", "გრეიფრუტი"]
middle = words[len(words) // 2]  
print("შუა სტრინგი არის:", middle)



text = "პითონი"
second_letter = text[1]
print("მეორე ასო არის:", second_letter)



products = ["წყალი", "კოკა-კოლა", "წვენი", "შოკოლადი", "ჩიფსები"]

print("🎯 ვენდინგ მანქანა")
print("აირჩიე პროდუქტი რიცხვის მიხედვით:")
for i in range(len(products)):
    print(f"{i + 1}. {products[i]}")

choice = int(input("შეიყვანე რიცხვი (1-5): "))

if 1 <= choice <= len(products):
    print("თქვენ აირჩიეთ:", products[choice - 1])
else:
    print("არასწორი არჩევანი!")






