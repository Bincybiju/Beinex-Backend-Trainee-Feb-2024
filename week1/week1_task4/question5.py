score = int(input("Enter the score: "))


if score < 0 or score > 100:
    print("Invalid")
elif score >= 90:
    print("Grade: A+")
elif score >= 80:
    print("Grade: A")
elif score >= 70:
    print("Grade: B+")
elif score >= 60:
    print("Grade: B")
elif score >= 50:
    print("Grade: C")
else:
    print("Failed")
