# 1. ფუნქცია: რიცხვზე 5-ის დამატება
def add_five(number):
    return number + 5

# 2. ფუნქცია: ორი integer-ის ნამრავლი
def multiply(a, b):
    return a * b

# 3. ფუნქცია: string-ის სიგრძე
def string_length(text):
    return len(text)

# 4. ფუნქცია: string-ების სიგრძეების list
def lengths_of_strings(string_list):
    return [len(s) for s in string_list]

# 5. ფუნქცია: Palindrome შემოწმება
def is_palindrome(word):
    return word == word[::-1]

# 6. ფუნქცია: string-ის გადაყვანა uppercase-ში
def to_uppercase(text):
    return text.upper()
