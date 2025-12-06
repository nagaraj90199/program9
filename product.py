def product_details(product_name, product_id, price, quantity):
    result = (
        f"Product Name : {product_name}\n"
        f"Product ID   : {product_id}\n"
        f"Price        : {price}\n"
        f"Quantity     : {quantity}\n"
    )
    return result


if __name__ == "__main__":
    # Example campus data
    name = "Laptop"
    pid = "P12345"
    price = "55000"
    qty = "3"
    print(product_details(name, pid, price, qty))
