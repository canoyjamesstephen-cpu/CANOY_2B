from menu import STORE_NAME

WIDTH = 40


def display_menu(lookup):
    print("=" * WIDTH)
    print(STORE_NAME.center(WIDTH))
    print("=" * WIDTH)
    for number in lookup:
        name, price = lookup[number]
        print(f"{number:>2}. {name:<20} PHP {price:>6.2f}")
    print("=" * WIDTH)