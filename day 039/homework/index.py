# 1. მაქსიმალური რიცხვი თითოეული list-დან
list1 = [12, 45, 67, 23, 89]
list2 = [34, 78, 90, 21, 56]
list3 = [5, 9, 3, 7, 2]

print("1. მაქსიმალური მნიშვნელობები:")
print("List1:", max(list1))
print("List2:", max(list2))
print("List3:", max(list3))

# 2. მინიმალური რიცხვი თითოეული list-დან
print("\n2. მინიმალური მნიშვნელობები:")
print("List1:", min(list1))
print("List2:", min(list2))
print("List3:", min(list3))

# 3. list-ის სიგრძე
list4 = ["a", "b", "c", "d", "e"]
list5 = [1, 2, 3, 4, 5, 6]
list6 = ["apple", "banana", "cherry", "date", "fig", "grape"]

print("\n3. სიგრძეები:")
print("List4:", len(list4))
print("List5:", len(list5))
print("List6:", len(list6))

# 4. ჯამი თითოეული list-დან
list7 = [10, 20, 30, 40, 50]
list8 = [5, 15, 25, 35, 45]
list9 = [1, 2, 3, 4, 5]

print("\n4. ჯამები:")
print("List7:", sum(list7))
print("List8:", sum(list8))
print("List9:", sum(list9))

# 5. ინდექსირება და ციკლები
list10 = [1,2,3,4,5,6,7,8,9,10]
list11 = [11,12,13,14,15,16,17,18,19,20]
list12 = [21,22,23,24,25,26,27,28,29,30]
list13 = [31,32,33,34,35,36,37,38,39,40]

print("\n5. ინდექსირება და ციკლები:")

# 1) პირველიდან მეოთხე ელემენტამდე
print("List10 (0-3):", list10[0:4])

# 2) მეოთხედან მერვემდე for ციკლით
print("List11 (3-7):")
for i in range(3, 8):
    print(list11[i], end=" ")
print()

# 3) მეცხრედან მეექვსემდე უკუღმა (უარყოფითი ინდექსებით)
print("List12 (9-6):", list12[-1:-5:-1])  # ანუ 30, 29, 28, 27

# 4) while ციკლით ყველა ელემენტი
print("List13 (while loop):")
i = 0
while i < len(list13):
    print(list13[i], end=" ")
    i += 1
print()

# 6. Boss Level ფუნქცია
def analyze_list(user_list):
    print("\n6. List ანალიზი:")
    print("👉 მაქსიმალური:", max(user_list))
    print("👉 მინიმალური:", min(user_list))
    print("👉 ჯამი:", sum(user_list))
    print("👉 სიგრძე:", len(user_list))

# ფუნქციის ტესტი
sample_list = [14, 27, 33, 8, 19, 41]
analyze_list(sample_list)