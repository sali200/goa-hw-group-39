def print_word_by_index():
    words = ["მზე", "წვიმა", "ქარი", "თოვლი", "ღრუბელი"]
    
    try:
        user_input = int(input("შეიყვანეთ რიცხვი 0-დან 4-მდე: "))
        
        if 0 <= user_input < len(words):
            print(f"თქვენ აირჩიეთ სიტყვა: {words[user_input]}")
        else:
            print("რიცხვი არასწორია. სცადეთ თავიდან.")
    
    except ValueError:
        print("გთხოვთ, შეიყვანეთ მხოლოდ რიცხვი.")



print_word_by_index()