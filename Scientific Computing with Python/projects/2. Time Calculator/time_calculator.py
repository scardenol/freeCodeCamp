def add_time(start, duration, day=None):
    # Split start into time and AM/PM abbreviation
    start_time, am_pm = start.split()
    # Split start time into hours and minutes with colon ":" as the delimiter
    start_hour, start_min = start_time.split(":")
    # Split duration into hours and minutes with colon ":" as the delimiter
    duration_hour, duration_min = duration.split(":")
    # Convert time strings into integers
    start_hour, start_min = int(start_hour), int(start_min)
    duration_hour, duration_min = int(duration_hour), int(duration_min)
    # Convert start hour into 24 hour format. Use lower() to make sure it's not case sensitive
    if am_pm.lower() == "pm":
        start_hour += 12
    # Add hours
    end_hour = start_hour + duration_hour
    # Add minutes
    end_min = start_min + duration_min
    # If end_min is greater than 60, add end_min//60 to end_hour and set end_min to end_min%60
    if end_min >= 60:
        end_hour += end_min // 60
        end_min = end_min % 60
    # Calculate days later
    days_later = end_hour // 24
    # Convert end_hour to 24 hour format
    end_hour = end_hour % 24
    # Set end_am_pm with the appropriate AM/PM abbreviation
    if end_hour >= 12:
        end_am_pm = "PM"
        if end_hour > 12:
            end_hour -= 12
    else:
        if end_hour == 0:
            end_hour = 12
        end_am_pm = "AM"
    # Initialize days_later_str to empty string
    days_later_str = ""
    # If days_later is greater than 1, set days_later to "(n days later)"
    if days_later > 1:
        days_later_str = f"({days_later} days later)"
    # If days_later is 1 or the am_pm and start am_pm are different, set days_later to "(next day)"
    elif days_later == 1 or (am_pm == "PM" and end_am_pm == "AM"):
        days_later_str = "(next day)"
    # Convert end hour and end minute into strings
    end_hour, end_min = str(end_hour), str(end_min)
    # Add leading 0 to end minute if it's less than 10
    if len(end_min) < 2:
        end_min = "0" + end_min
    # List of days of the week in lower case due to day being case insensitive when passed as an argument
    days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    # Check if day is passed as an argument and is a valid day of the week
    if day and day.lower() in days_of_week:
        # Get index of day in days_of_week list
        day_index = days_of_week.index(day.lower())
        # Calculate new day index by adding days_later to day_index and getting the modulo of 7
        new_day_index = (day_index + days_later) % 7
        # Get new day of the week from days_of_week list and capitalize it
        new_day = days_of_week[new_day_index].capitalize()
        # Format output string
        new_time = f"{end_hour}:{end_min} {end_am_pm}, {new_day}"
    else:
        # Format output string
        new_time = f"{end_hour}:{end_min} {end_am_pm}"
    # If days_later_str is not empty, add it to the output string
    if days_later_str:
        new_time += f" {days_later_str}"
    return new_time


# Test cases
# print(add_time("3:30 PM", "2:12"))
# print(add_time("11:55 AM", "3:12"))
# print(add_time("9:15 PM", "5:30"))
# print(add_time("11:40 AM", "0:25"))
# print(add_time("2:59 AM", "24:00"))
# print(add_time("11:59 PM", "24:05"))
# print(add_time("8:16 PM", "466:02"))
# print(add_time("5:01 AM", "0:00"))
# print(add_time("3:30 PM", "2:12", "Monday"))
# print(add_time("2:59 AM", "24:00", "saturDay"))
# print(add_time("11:59 PM", "24:05", "Wednesday"))
# print(add_time("8:16 PM", "466:02", "tuesday"))
