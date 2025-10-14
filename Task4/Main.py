"""
Author: AlieeLinux
"""


try:
    Base_Price = 12
    age = int(input("Enter your age: "))
    is_student = input("Are you an Student?(true/false)")

    if is_student.upper() == "TRUE":
        is_student = True
    elif is_student.upper() == "FALSE":
        is_student = False
    else:
        raise Exception()

    if age <= 12:
        FinalPrice = Base_Price - 3
        print("Your ticket price is", FinalPrice)

    if is_student and not age >=65 and not age <=12:
        FinalPrice = Base_Price - 2
        print("Your ticket price is", FinalPrice)

    if not is_student and age >=65:
        FinalPrice = Base_Price - 4
        print("Your ticket price is", FinalPrice)

    if not is_student and not age >= 65 and not age <=12:
        print("Your ticket price is", Base_Price)

except Exception:
    print("Enter the valid requests")