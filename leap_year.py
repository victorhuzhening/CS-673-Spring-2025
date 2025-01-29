def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

try:
    year = int(input("Please input a year:"))
    if is_leap(year):
        print("This is a leap year!")
    else:
        print("This is not a leap year!")

except Exception as e:
    print(f"ERROR: {e}")