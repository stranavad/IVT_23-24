def get_user_input(message: str, input_type: str = "text") -> str | int | float:
    user_input = input(message)

    if input_type != 'text':
        try:

            if input_type == 'number':
                return float(user_input)  # Accept all numbers
            return int(user_input)  # Accept only integers
        except ValueError:
            print("Your shall enter only int or float")
            return get_user_input(input_type)

    return user_input