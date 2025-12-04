import pytest

def product_details(product_name, product_id, category, price):
    result = (
        f"Product Name : {product_name}\n"
        f"Product ID : {product_id}\n"
        f"Category : {category}\n"
        f"Price : {price}"
    )
    return result

if __name__ == "__main__":
    # Sample input
    product_name = "Laptop"
    product_id = "P1001"
    category = "Electronics"
    price = 75000

    print(product_details(product_name, product_id, category, price))
