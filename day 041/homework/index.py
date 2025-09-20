def vending_machine(products, user_money, selected_index):
    if selected_index < 0 or selected_index >= len(products):
        print("არასწორი არჩევანი.")
        return

    product_name, product_price = products[selected_index]

    if user_money >= product_price:
        print(f"თქვენ შეიძინეთ: {product_name}")
    else:
        print(f"სამწუხაროდ, თანხა არ არის საკმარისი {product_name}-ის შესაძენად.")

products = [
    ("წყალი", 1.0),
    ("კოლა", 1.5),
    ("ჩიფსები", 2.0),
    ("შოკოლადი", 2.5)
]

user_money = 2.0

selected_index = 2

vending_machine(products, user_money, selected_index)