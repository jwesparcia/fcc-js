def validate_isbn(isbn, length):
    # Check the length of the ISBN
    if len(isbn) != length:
        print(f"ISBN-{length} code should be {length} digits long.")
        return

    # Separate the main digits and check digit
    main_digits = isbn[:-1]
    given_check_digit = isbn[-1]

    # Convert the main digits to integers
    try:
        main_digits_list = [int(digit) for digit in main_digits]
    except ValueError:
        print("Invalid character was found.")
        return

    # Calculate the expected check digit
    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)

    # Compare check digits
    if given_check_digit.upper() == expected_check_digit:
        print("Valid ISBN Code.")
    else:
        print("Invalid ISBN Code.")


def calculate_check_digit_10(main_digits_list):
    digits_sum = 0

    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)

    result = 11 - digits_sum % 11

    if result == 11:
        return "0"
    elif result == 10:
        return "X"
    else:
        return str(result)


def calculate_check_digit_13(main_digits_list):
    digits_sum = 0

    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit
        else:
            digits_sum += digit * 3

    result = 10 - digits_sum % 10

    if result == 10:
        return "0"
    else:
        return str(result)


def main():
    user_input = input("Enter ISBN and length: ")

    values = user_input.split(",")

    # Validate comma-separated input
    if len(values) != 2:
        print("Enter comma-separated values.")
        return

    isbn = values[0].strip()

    # Validate length input
    try:
        length = int(values[1].strip())
    except ValueError:
        print("Length must be a number.")
        return

    # Validate supported lengths
    if length not in (10, 13):
        print("Length should be 10 or 13.")
        return

    # Validate ISBN
    validate_isbn(isbn, length)


#main()
