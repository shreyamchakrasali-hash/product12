from product import format_product_info

def test_format_product_info():
    product_id = 101
    name = "Laptop"
    quantity = 5
    price = 799.99

    expected_output = (
        "Product Information:\n"
        "ID: 101\n"
        "Name: Laptop\n"
        "Quantity: 5\n"
        "Price: $799.99"
    )

    assert format_product_info(product_id, name, quantity, price) == expected_output