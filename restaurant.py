import datetime
from dataclasses import dataclass


@dataclass(frozen=True)
class MenuItem:
    number: int
    name: str
    price: float
    category: str


@dataclass
class OrderLine:
    item: MenuItem
    quantity: int

    @property
    def line_total(self):
        return self.item.price * self.quantity


class Menu:
    """Holds the menu items and numbers them automatically."""

    def __init__(self, data):
        self._items = {}
        number = 1
        for category, items in data.items():
            for name, price in items.items():
                self._items[number] = MenuItem(number, name, price, category)
                number += 1

    def get(self, number):
        return self._items.get(number)

    def __contains__(self, number):
        return number in self._items

    def __iter__(self):
        return iter(self._items.values())


class Order:
    """A customer's order: lines, senior/PWD flag, and totals."""

    SENIOR_RATE = 0.20
    BULK_QTY = 5
    BULK_RATE = 0.05

    def __init__(self):
        self.lines = []
        self.is_senior = False

    def add(self, item, quantity):
        self.lines.append(OrderLine(item, quantity))

    @property
    def total_quantity(self):
        return sum(line.quantity for line in self.lines)

    @property
    def subtotal(self):
        return sum(line.line_total for line in self.lines)

    @property
    def discount_label(self):
        if self.is_senior:
            return f"Senior/PWD Discount ({self.SENIOR_RATE:.0%})"
        if self.total_quantity >= self.BULK_QTY:
            return f"Discount ({self.BULK_RATE:.0%})"
        return None

    @property
    def discount(self):
        if self.is_senior:
            return self.subtotal * self.SENIOR_RATE
        if self.total_quantity >= self.BULK_QTY:
            return self.subtotal * self.BULK_RATE
        return 0.0

    @property
    def total(self):
        return self.subtotal - self.discount


class Display:
    """Handles all printing (menu and receipt)."""

    def __init__(self, store_name, width=40):
        self.store_name = store_name
        self.width = width

    def show_menu(self, menu):
        w = self.width
        print("=" * w)
        print(self.store_name.center(w))
        print("=" * w)
        for item in menu:
            print(f"{item.number:>2}. {item.name:<20} PHP {item.price:>6.2f}")
        print("=" * w)

    def show_receipt(self, order):
        w = self.width
        stamp = datetime.datetime.now().strftime("%b %d, %Y %I:%M %p")
        print("\n" + "=" * w)
        print(self.store_name.center(w))
        print(stamp.center(w))
        print("-" * w)
        for line in order.lines:
            print(f"{line.item.name:<16}{line.quantity:>3} x "
                  f"{line.item.price:>6.2f} = {line.line_total:>7.2f}")
        print("-" * w)
        print(f"{'SUBTOTAL':<25}{order.subtotal:>15.2f}")
        if order.discount_label:
            print(f"{order.discount_label:<25}{-order.discount:>15.2f}")
        print(f"{'TOTAL':<25}{order.total:>15.2f}")
        print("=" * w)
        print("Thank you, come again!".center(w))
        print("=" * w + "\n")


class InputHandler:
    """Handles validated user input."""

    def __init__(self, menu):
        self.menu = menu

    @staticmethod
    def ask_yes_no(prompt):
        while True:
            answer = input(prompt).strip().lower()
            if answer in ("y", "yes"):
                return True
            if answer in ("n", "no"):
                return False
            print("  Invalid choice! Please enter 'y' or 'n'.")

    def ask_item(self):
        while True:
            raw = input("Item number: ").strip()
            if raw.isdigit() and int(raw) in self.menu:
                return self.menu.get(int(raw))
            print("  Invalid item number.")

    @staticmethod
    def ask_quantity():
        while True:
            raw = input("Quantity: ").strip()
            if raw.isdigit() and int(raw) > 0:
                return int(raw)
            print("  Invalid quantity.")


class Restaurant:
    """Main class: connects the menu, input, order and display."""

    def __init__(self, store_name, menu_data):
        self.menu = Menu(menu_data)
        self.display = Display(store_name)
        self.input = InputHandler(self.menu)

    def take_order(self):
        order = Order()
        while True:
            item = self.input.ask_item()
            qty = self.input.ask_quantity()
            order.add(item, qty)
            if not self.input.ask_yes_no("Order another item? (y/n): "):
                break
        order.is_senior = self.input.ask_yes_no("Senior Citizen/PWD? (y/n): ")
        return order

    def run(self):
        while True:
            self.display.show_menu(self.menu)

            if not self.input.ask_yes_no("Order now? (y/n): "):
                print("Goodbye!")
                break

            order = self.take_order()
            self.display.show_receipt(order)

            if not self.input.ask_yes_no("Would you like to order again? (y/n): "):
                print("Goodbye!")
                break