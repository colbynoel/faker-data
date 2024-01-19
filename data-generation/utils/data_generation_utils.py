import random

def generate_random_upc():
    """
    Generate a random UPC (Universal Product Code) number.
    UPC is a 12-digit barcode symbol consisting of a number system digit,
    five manufacturer code digits, five product code digits, and a check digit.
    """

    # Generate 11 random digits (excluding the check digit)
    upc_base = "".join([str(random.randint(0, 9)) for _ in range(11)])

    # Calculate the check digit
    check_digit = calculate_upc_check_digit(upc_base)

    # Combine base UPC and check digit
    upc = upc_base + str(check_digit)

    return upc

def calculate_upc_check_digit(upc_base):
    """
    Calculate the check digit for a UPC code.
    """

    digits = list(map(int, list(upc_base)))

    odd_sum = sum(digits[::2])
    even_sum = sum(digits[1::2])
    total = (odd_sum * 3) + even_sum
    check_digit = (10 - (total % 10)) % 10

    return check_digit

def get_random_product_size(ran_num: int) -> str:
    """
    Grabs a random product size
    """
    sizes = ["xxs", "xs", "s", "m", "l", "xl", "xxl", "xxxl", "xxxxl"]

    return sizes[ran_num]

def time_worked() -> str:
    return f"{random.randint(0, 47)}Y{random.randint(0, 11)}M{random.randint(0,31)}D"
