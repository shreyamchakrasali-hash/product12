from product import product_details

def test_product_details_output():
    result = product_details("P101", "Laptop", 5, 55000)
    expected = (
        "Product ID   : P101\n"
        "Product Name : Laptop\n"
        "Quantity     : 5\n"
        "Price        : 55000"
    )
    assert result == expected
