try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("Invaild input! Plese enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")

print("End of program")
