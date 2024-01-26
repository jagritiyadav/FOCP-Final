def get_positive_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a positive integer!")
        except ValueError:
            print("Please enter a number!")

def get_yes_no_input(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer == 'y' or answer == 'n':
            return answer
        else:
            print('Please answer "Y" or "N".')

def calculate_total_price(num_pizzas, is_delivery, is_tuesday, used_app):
    pizza_price = 12
    delivery_cost = 2.5
    discount_percentage = 0.25
    tuesday_discount_percentage = 0.5

    total_pizza_price = num_pizzas * pizza_price

    if is_tuesday:
        total_pizza_price *= (1 - tuesday_discount_percentage)

    if is_delivery:
        if num_pizzas >= 5:
            delivery_cost = 0
        total_pizza_price += delivery_cost

    if used_app:
        total_pizza_price *= (1 - discount_percentage)

    return round(total_pizza_price, 2)

def main():
    print("BPP Pizza Price Calculator")
    print("==========================")

    num_pizzas = get_positive_integer_input("How many pizzas ordered? ")

    is_delivery = get_yes_no_input("Is delivery required? (Y/N) ")
    is_delivery = is_delivery == 'y'

    is_tuesday = get_yes_no_input("Is it Tuesday? (Y/N) ")
    is_tuesday = is_tuesday == 'y'

    used_app = get_yes_no_input("Did the customer use the app? (Y/N) ")
    used_app = used_app == 'y'

    total_price = calculate_total_price(num_pizzas, is_delivery, is_tuesday, used_app)

    print(f"\nTotal Price: £{total_price:.2f}.")

if __name__ == "__main__":
    main()
