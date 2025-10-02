import calendar

# Get user input for the year and month
try:
    year = int(input("Enter the year (e.g., 2025): "))
    month = int(input("Enter the month (1-12): "))

    # Validate the month input
    if not (1 <= month <= 12):
        print("Invalid month. Please enter a number between 1 and 12.")
    else:
        # Display the calendar for the specified month and year
        print(calendar.month(year, month))

except ValueError:
    print("Invalid input. Please enter valid integer values for year and month.")