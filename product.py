def product_details(product_id, name, quantity, price):
    return (
        f"Product ID   : {product_id}\n"
        f"Product Name : {name}\n"
        f"Quantity     : {quantity}\n"
        f"Price        : {price}"
    )


if _name_ == "_main_":
    pid = "P101"
    pname = "Laptop"
    qty = 5
    pr = 55000

    print(product_details(pid, pname, qty, pr))
