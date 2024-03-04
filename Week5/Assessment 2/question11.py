"""Write a Python function called calculate_discounted_price that takes the 
original price of an item and a discount percentage as input. The function 
should return the discounted price after applying the discount. Ensure that 
the function handles the case where the discount percentage is negative 
and raises a custom exception called InvalidDiscountError with an 
appropriate error message. """

class InvalidDiscountError(Exception):
    pass

class InvalidPriceError(Exception):
    pass

def discount_price(original_price, discount_percentage):
    if discount_percentage < 0:
        raise InvalidDiscountError("Discount percentage must be positive")
    discounted_price = original_price - (original_price * discount_percentage / 100)
    return discounted_price


try:
    original_price = float(input("Enter original price: "))
    if original_price <= 0:
        raise InvalidPriceError("Original price must be positive")
    
    discount_percentage = float(input("Enter the discount percentage: "))
    discounted_price = discount_price(original_price, discount_percentage)
    print("Discounted price:", discounted_price)
except ValueError:
    print("Please enter valid numeric values for original price and discount percentage.")
except InvalidPriceError as e:
    print(e)
except InvalidDiscountError as e:
    print(e)
