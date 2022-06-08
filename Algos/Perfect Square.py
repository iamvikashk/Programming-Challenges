def perfect_square(num):
    last_digits = ['1', '4', '9', '6', '5', '0']  # A perfect square will have these as its last digits
    if str(num)[-1] in last_digits:
        if num % 4 in [0, 1]:  # A perfect square has a quotient of either 0 or 1 when divided by 4
            num_half = num // 2
            for i in range(num_half + 1):
                if i * i == num:    # Check if the number is a square of any number less than it until half of that number
                    return True
            out = False
        else:
            out = False
    else:
        out = False
    return out
