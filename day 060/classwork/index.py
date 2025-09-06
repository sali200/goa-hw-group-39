def reverse_letter(string):
    return ''.join([c for c in reversed(string) if c.isalpha()])


numbers = [5, 12, 7, 3, 8]
total = 0

for num in numbers:
    total += num

print("ელემენტების ჯამი არის:", total)