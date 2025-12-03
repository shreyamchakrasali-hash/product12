def format_product_info(product_id, name, quantity, price):



   

    return (

        f"Product Information:\n"

        f"ID: {product_id}\n"

        f"Name: {name}\n"

        f"Quantity: {quantity}\n"

        f"Price: ${price:.2f}"

    )





if __name__ == "__main__":

    print(format_product_info(101, "Laptop", 5, 799.99))