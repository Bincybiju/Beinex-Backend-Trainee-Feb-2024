from question20part1 import *
def main():
    name = get_str("Enter your name: ")

    roll_number = get_int("Enter your roll number: ")

    marks = get_float("Enter your total marks: ")

    print("\nName of student:", name)
    print("Roll number:", roll_number)
    print("Total marks:", marks)

if __name__ == "__main__":
    main()
