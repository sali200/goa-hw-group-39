i = 1
while i <= 5:
    print(i)
    i += 1


password = ""
while password != "salome123":
    password = input("შეიყვანე პაროლი: ")
print("პაროლი სწორია!")



total = 0
num = 1
while total <= 100:
    total += num
    num += 1
print("ჯამი:", total)




n = 5
result = 1
while n > 0:
    result *= n
    n -= 1
print("ფაქტორიალი:", result)