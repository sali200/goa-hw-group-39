# 1. ფუნქცია, რომელიც აბრუნებს რიცხვზე 5'ით მეტს
def add_five(number):
    return number + 5

# 2. ფუნქცია, რომელიც აბრუნებს ორ რიცხვს შორის ნამრავლს
def multiply(a, b):
    return a * b

# 3. ფუნქცია, რომელიც აბრუნებს სტრინგის სიგრძეს
def string_length(text):
    return len(text)

# 4. ფუნქცია, რომელიც აბრუნებს სტრინგების სიგრძეების სიას
def list_of_lengths(strings):
    return [len(s) for s in strings]

# 5. ფუნქცია, რომელიც ამოწმებს არის თუ არა სტრინგი პალინდრომი
def is_palindrome(text):
    return text == text[::-1]

# 6. ფუნქცია, რომელიც სტრინგს გარდაქმნის uppercase-ში
def to_uppercase(text):
    return text.upper()