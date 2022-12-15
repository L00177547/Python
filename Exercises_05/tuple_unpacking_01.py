def most_expensive(price_list):
    """
    Iterate through a list and find the most expensive item
    """
    # Set up the variables
    max_price = 0
    max_price_item = ""
    stock_level = ""
    # Iterate, unpacking the tuple
    for description, price, stock_availability in price_list:
        # If this is the maximum price, record that in our variables
        if price > max_price:
            max_price = price
            max_price_item = description
            stock_level = stock_availability
        # If it is not the maximum price, do nothing
    else:
        pass
    # Return the maximum prices item and its price
    return max_price_item, max_price, stock_level


# Provide the data
price_list = [("Pineapple", 1.0, "In Stock"), ("Apples", .5, "Out of Stock"), ("Pears", .7, "In Stock"),
              ("Peaches", .8, "In Stock")]
# Call the function and unpack its return values
product, price, availability = most_expensive(price_list)
print(product, price, availability)
