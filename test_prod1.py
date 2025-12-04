from prod1 import product_details

def test_product_details():
    expected_output = (
        "Product ID : P1001\n"
        "Product Name : Laptop\n"
        "Quantity : 10\n"
        "Price : 75000"
    )
    assert product_details("P1001", "Laptop", "10", "75000") == expected_output
