def shop_from_grocery_list(budget, grocery_list, *products):
    purchased_products = set()
    total_cost = 0

    for product_name, price in products:
        if product_name not in grocery_list:
            continue

        if product_name in purchased_products:
            continue

        if budget < price:
            break

        purchased_products.add(product_name)
        total_cost += price
        budget -= price

    if purchased_products == set(grocery_list):
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        missing_products = set(grocery_list) - purchased_products
        missing_products_str = ', '.join(missing_products)
        return f"You did not buy all the products. Missing products: {missing_products_str}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))
