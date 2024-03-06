# Write a Python program input and add two integers only and handle the 
# exceptions.
# RUN 1:
# Enter First Value: 10
# Enter Second Value: 20
# 0.5

def divide_two_integers():
    try:
        first_number = int(input("Enter First Value: "))

        second_number = int(input("Enter Second Value: "))

        if second_number == 0:
            raise ValueError("Second Number Should Not Be Zero")

        result = first_number / second_number
        print(result)

    except ValueError as ve:
        print(f"Pls Input Integer Only {ve}")
    except ZeroDivisionError as zde:
        print(f"Second Number Should Not Be Zero {zde}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

divide_two_integers()
