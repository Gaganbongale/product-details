from product import product_details

def test_product_details():
    expected_output = (
        "Product Name : Laptop\n"
        "Product ID : P1001\n"
        "Category : Electronics\n"
        "Price : 75000"
    )
    assert product_details("Laptop", "P1001", "Electronics", 75000) == expected_output
