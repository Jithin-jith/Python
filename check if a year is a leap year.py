def is_leap_year(year):
    # A year is a leap year if:
    # 1. It's divisible by 4, AND
    # 2. Not divisible by 100, UNLESS it's also divisible by 400
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

# Ask the user for input
year = int(input("Enter a year to check if it is a leap year: "))

# Call the function and print the result
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")