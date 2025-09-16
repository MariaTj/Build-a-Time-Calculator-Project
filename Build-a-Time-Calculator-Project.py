def add_time(start, duration, day=None):
    # Split start time into hour, minutes, and AM/PM
    start_hour = int(start.split(':')[0])
    start_min = int(start.split(':')[1].split(' ')[0])
    start_pmam = start[-2:]

    # Convert start time to total minutes since 00:00
    total_min = start_hour * 60 + start_min
    if start_pmam == 'AM' and start_hour == 12:
        total_min = 0 + start_min
    elif start_pmam == 'PM' and start_hour != 12:
        total_min = (start_hour + 12) * 60 + start_min

    # Split duration into hours and minutes and convert to total minutes
    duration_hour = int(duration.split(':')[0])
    duration_min = int(duration.split(':')[1])
    duration_total_min = duration_hour * 60 + duration_min

    # Add duration to start time
    end_total_min = total_min + duration_total_min

    # Calculate number of days later and minutes into the final day
    days_later = end_total_min // 1440
    end_min_in_day = end_total_min % 1440
    
    # Convert total minutes back to hours and minutes
    end_hour = end_min_in_day // 60
    end_min = end_min_in_day % 60

    # Convert 24-hour time to 12-hour time with AM/PM
    if end_hour == 0:
        final_hour = 12
        period = "AM"
    elif 1 <= end_hour <= 11:
        final_hour = end_hour
        period = "AM"
    elif end_hour == 12:
        final_hour = 12
        period = "PM"
    elif 13 <= end_hour <= 23:
        final_hour = end_hour - 12
        period = "PM" 
        
    # Format minutes with leading zero if needed 
    if end_min < 10:
        formatted_min = "0" + str(end_min)
    else:
        formatted_min = str(end_min)

    # Prepare day later string (next day / n days later)
    if days_later == 0:
        day_string = ""
    elif days_later == 1:
        day_string = " (next day)"
    elif days_later > 1:
        day_string = f" ({days_later} days later)"
    
    # Handle optional weekday input
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if day is not None:
        day_input = day.capitalize()
        day_index = weekdays.index(day_input)
        end_day_index = (day_index + days_later) % 7
        end_day = weekdays[end_day_index]
        day_string = f", {end_day}{day_string}"
    else:
        day_string = day_string
    
    # Build final time string    
    new_time = f"{final_hour}:{formatted_min} {period}{day_string}"


    return new_time
print(add_time('10:10 PM', '3:30'))

# Example
print(add_time('10:10 PM', '3:30'))           # without day
print(add_time('3:30 PM', '2:12', 'Monday'))  # with day
print(add_time('11:43 PM', '24:20', 'tuesday')) # with day and more days later

"""
Should print:
1:40 AM (next day)
1:40 AM (next day)
5:42 PM, Monday
12:03 AM, Thursday (2 days later)
"""