def get_protein(order):
    protein = order[3]
    if protein == 'chicken' or protein == 'veggies':
        return 2.5
    elif protein == 'steak' or protein == 'barbacoa':
        return 3.5
    elif protein == 'carnitas':
        return 3.0
    else:  # empty string or unrecognized
        return 0


def get_rice(order):
    rice = order[4]
    if rice == 'white':
        return 2.5
    elif rice == 'brown':
        return 3.5
    else:  # empty string or unrecognized
        return 0

def get_beans(order):
    beans = order[5]
    if beans == 'black' or beans == 'pinto':
        return 2.5
    else:  # empty string or anything else
        return 0
    
def get_burrito(order):
    if order[6]:   # order[6] is a boolean: True for burrito, False for bowl
        return 2.0
    else:
        return 0

def get_toppings(order):
    topping_prices = {
        'guacamole': 2.75,
        'tomato salsa': 2.5,
        'chili corn salsa': 1.75,
        'tomatillo green chili salsa': 2.0,
        'sour cream': 2.5,
        'fajita veggies': 2.5,
        'cheese': 2.0,
        'queso blanco': 2.75
    }
    protein = order[3]
    total = 0
    # Toppings start from index 7 onward
    for topping in order[7:]:
        if topping == '':
            continue
        # Free if protein is veggies and topping is guacamole or fajita veggies
        if protein == 'veggies' and (topping == 'guacamole' or topping == 'fajita veggies'):
            continue
        total += topping_prices.get(topping, 0)
    return total

def apply_discount(order, total):
    code = order[2]  # Discount code
    if code == 'MAGIC':
        return total * 0.95
    elif code == 'SUNDAYFUNDAY':
        return total * 0.90
    elif code == 'FLAT3':
        return total - 3
    else:  # No code or unrecognized code
        return total

def approximate_time(order):
    location_times = {
        'amherst': 15,
        'north amherst': 15,
        'south amherst': 15,
        'hadley': 15,
        'northampton': 30,
        'south hadley': 30,
        'belchertown': 30,
        'sunderland': 30,
        'holyoke': 45,
        'greenfield': 45,
        'deerfield': 45,
        'springfield': 45
    }
    location = order[1]
    return location_times.get(location, 45)  # Default to 45 if not found

def generate_invoice(order):
    # Assume you have these functions already defined:
    # get_protein, get_rice, get_beans, get_burrito, get_toppings, apply_discount, approximate_time

    customer_name = order[0]
    discount_code = order[2]
    protein = order[3]
    rice = order[4]
    beans = order[5]
    burrito = order[6]
    toppings_list = [t for t in order[7:] if t != '']

    protein_price = get_protein(order)
    rice_price = get_rice(order)
    beans_price = get_beans(order)
    burrito_price = get_burrito(order)
    toppings_price = get_toppings(order)

    total_price = protein_price + rice_price + beans_price + burrito_price + toppings_price
    price_after_discount = apply_discount(order, total_price)
    money_saved = total_price - price_after_discount
    approx_time = approximate_time(order)

    # Yes/No for Burrito (True means Yes)
    burrito_text = "Yes" if burrito else "No"

    # Comma-separated toppings string
    toppings_str = ', '.join(toppings_list)

    print(f"Welcome to Chipotle Mexican Grill Hadley, {customer_name}.")
    print("Your invoice is displayed below:")
    print(f"Protein: {protein} - ${protein_price:.2f}")
    print(f"Rice: {rice} rice - ${rice_price:.2f}")
    print(f"Beans: {beans} beans - ${beans_price:.2f}")
    print(f"Burrito: {burrito_text} - ${burrito_price:.2f}")
    print(f"Toppings: {toppings_str} - ${toppings_price:.2f}")
    print(f"")
    print(f"Subtotal: ${total_price:.2f}")
    print(f"Discount Code: {discount_code}")
    print(f"Total: ${price_after_discount:.2f}")
    print(f"You Save: ${money_saved:.2f}")
    print(f"Your order will be ready in {approx_time} minutes.")
    print("Enjoy your meal and have a good day!")

def take_order():
    print("Welcome to Chipotle Ordering!")
    name = input("Enter your name: ")
    location = input("Enter your delivery location: ").lower()  # match dictionary
    discount_code = input("Enter discount code (leave blank if none): ").upper()
    protein = input("Enter protein (chicken, steak, barbacoa, carnitas, veggies, or leave blank): ").lower()
    rice = input("Enter rice (white, brown, or leave blank): ").lower()
    beans = input("Enter beans (black, pinto, or leave blank): ").lower()
    burrito_input = input("Is this a burrito? (y/n): ").lower()
    burrito = True if burrito_input == 'y' else False

    # Ask for toppings (can be variable number, comma separated)
    toppings_raw = input("Enter toppings separated by commas (leave blank if none): ")
    toppings = [t.strip().lower() for t in toppings_raw.split(",") if t.strip() != ""]

    # tuple should have the first 7 entries (including True/False for burrito) plus toppings
    return (name, location, discount_code, protein, rice, beans, burrito, *toppings)

# Usage
order = take_order()
generate_invoice(order)
