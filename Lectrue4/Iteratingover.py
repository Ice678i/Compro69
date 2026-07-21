input_string = input("Enter a string")
Modified_string = ""
vowels = "aeiouAEIOU"
for char in input_string:
    upper_char = char.upper()
    if upper_char in vowels:
        Modified_string += "*"
    else:
        Modified_string += upper_char

print("Modified string :" , Modified_string)
