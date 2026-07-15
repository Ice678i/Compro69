inchar = input(" input one character: ")
if inchar >= 'A' and inchar <= 'Z':
    print("This is an upper case letter" , inchar)
elif inchar >= 'a' and inchar <= 'z' :
    print("You in put Lower case letter" , inchar)
elif inchar >= '0' and inchar <= '9':
    print("You input a Number" , inchar)
else:
    print("You input a Letter or number" , inchar)
    