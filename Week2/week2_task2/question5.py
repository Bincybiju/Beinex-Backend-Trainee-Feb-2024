number = lambda s: s.isdigit()

given_string = "12345"
if number(given_string):
    print(f"The string '{given_string}' is a number.")
else:
    print(f"The string '{given_string}' is not a number.")
