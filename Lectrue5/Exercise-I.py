def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    total = 0
    for digit in num_str:
        total += int(digit) ** num_digits

    if total == number:
        return True
    else:
        return False

print(is_armstrong(153))
print(is_armstrong(9474))
print(is_armstrong(123))
