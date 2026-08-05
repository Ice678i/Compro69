NUM_EMPLOYEES = 6
def main():
    houres = [0] * NUM_EMPLOYEES
    for index in range(NUM_EMPLOYEES):
        print('Enter the houes worked by employees', \
              index + 1, ': ', sep='', end='')
        houres[index] = float(())
        pay_rate = float(input("Enter the hourly pa rate"))

        for index in range(NUM_EMPLOYEES):
            gross_pay = houres(index) * pay_rate
            print('Gross pay for employees', index + 1, ':$', \
                  format(gross_pay, ',.2f'), sep='')
            