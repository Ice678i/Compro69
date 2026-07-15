num_employees = int(input("Please input number of employees: "))
if num_employees < 50:
    print("This is a small company")
elif num_employees < 250:
    print("This is a medium company")
elif num_employees < 1000:
    print("This is a large company")
    