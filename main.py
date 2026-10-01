from restaurant import Restaurant

STORE_NAME = "STEPHEN FOOD RESTAURANT"

MENU = {
    "Burgers": {"Cheeseburger": 89.00, "Beef Burger": 129.00, "Chicken Burger": 99.00},
    "Sides": {"French Fries": 49.00, "Onion Rings": 55.00},
    "Drinks": {"Soft Drink": 39.00, "Iced Tea": 45.00, "Bottled Water": 25.00},
}

if __name__ == "__main__":
    Restaurant(STORE_NAME, MENU).run()
