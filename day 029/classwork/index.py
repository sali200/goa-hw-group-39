list1 = [1, 2, 3]
list2 = ["a", "b"]
list3 = [True, False, True, False]
list4 = [10.5, 20.7, 30.9, 40.1, 50.3]

print("List1 length:", len(list1))
print("List2 length:", len(list2))
print("List3 length:", len(list3))
print("List4 length:", len(list4))

fruits = []
colors = []

fruits.append("apple")
fruits.append("banana")
fruits.append("cherry")

colors.append("red")
colors.append("green")
colors.append("blue")

print("Fruits:", fruits)
print("Colors:", colors)

list_a = ["x", "y", "z", "w"]
list_b = ["dog", "cat", "bird", "fish"]

list_a.insert(4, "inserted_at_5")
list_a.insert(1, "inserted_at_2")

list_b.insert(2, "inserted_at_3")
list_b.insert(3, "inserted_at_4")

print("List A:", list_a)
print("List B:", list_b)

numbers = [10, 20, 30, 40, 50]
letters = ["a", "b", "c", "d", "e"]

numbers.pop(0)
numbers.pop(2)

letters.pop(1)
letters.pop()

print("Numbers after pop:", numbers)
print("Letters after pop:", letters)


data = []
data.append("goal")
data.append("oriented")
data.append("academy")
data.insert(1, "python")
data.pop(2)

print("Data:", data)
print("Length of data:", len(data))
print("Find 'a' in last item:", data[-1].find("a"))

name = "Giorgi"
hobby = "Programming"
city = "Tbilisi"

print("Length of name:", len(name))
print("Length of hobby:", len(hobby))
print("Length of city:", len(city))