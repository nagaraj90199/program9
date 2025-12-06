from product import product_details

def test_product_details():
    expected_output = (
        "Product Name : Laptop\n"
        "Product ID   : P12345\n"
        "Price        : 55000\n"
        "Quantity     : 3\n"
    )
    assert product_details("Laptop", "P12345", "55000", "3") == expected_output
    print("Test Passed!")

# Run the test
test_product_details()
