STORE_NAME = "STEPHEN FOOD RESTAURANT"

MENU = {
    "Burgers": {"Cheeseburger": 89.00, "Beef Burger": 129.00, "Chicken Burger": 99.00},
    "Sides": {"French Fries": 49.00, "Onion Rings": 55.00},
    "Drinks": {"Soft Drink": 39.00, "Iced Tea": 45.00, "Bottled Water": 25.00},
}


def build_item_lookup(menu):
    lookup = {}
    number = 1
    for category in menu:
        for item in menu[category]:
            lookup[number] = (item, menu[category][item])
            number += 1
    return lookup