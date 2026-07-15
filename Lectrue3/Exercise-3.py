hours = (input("Enter the number of hours worked: "))
pay_rate = (input("Enter the hourly pay rate: "))
if hours <= 40:
    gross_pay = (40 * pay_rate) + ((hours - 40) * pay_rate * 1.5)
else:
    gross_pay = hours * pay_rate
print(f"gross pay is ${gross_pay}:,.2f")

