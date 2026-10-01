from menu import MENU, build_item_lookup
from display import display_menu
from receipt import print_receipt
from user_input import ask_yes_no, take_orders
from discount import compute_totals


def main():
    lookup = build_item_lookup(MENU)

    while True:
        display_menu(lookup)

        if not ask_yes_no("Order now? (y/n): "):
            print("Goodbye!")
            break

        orders = take_orders(lookup)
        is_senior = ask_yes_no("Senior Citizen/PWD? (y/n): ")
        subtotal, discount, label, total = compute_totals(orders, is_senior)
        print_receipt(orders, subtotal, discount, label, total)

        if not ask_yes_no("Would you like to order again? (y/n): "):
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()