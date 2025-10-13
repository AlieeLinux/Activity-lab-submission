"""
Author: AlieeLinux
"""

try:
    inches = input("enter a number of inches: ")
    inches = int(inches)
    feet = inches // 12
    remaining_inches = inches % 12
    print(f"{inches} inches is equal to {feet} feet and {remaining_inches} inches.")
except Exception:
    print("Please only enter a number and try again")