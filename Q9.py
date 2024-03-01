from datetime import datetime, timedelta


def days_since_birthday(birthday_str):
    # Parse the birthday string to a datetime object
    birthday = datetime.strptime(birthday_str, "%d-%m-%Y")

    # Get today's date
    today = datetime.now()

    # Calculate the first and last day to be considered for the calculation
    first_day = datetime(birthday.year + 1, 1, 1)
    last_day = datetime(today.year, 1, 1)

    # Calculate the difference in days between the two dates, excluding the birth year and the current year
    days_diff = (last_day - first_day).days

    return days_diff


# Example usage
birthday_str = "09-06-2004"
print(days_since_birthday(birthday_str))
