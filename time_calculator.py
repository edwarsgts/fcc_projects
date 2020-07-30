#Scientific Computing with Python Projects - Time Calculator
#https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator

"""
README 

### Assignment

Write a function named `add_time` that takes in two required parameters and one optional parameter:
* a start time in the 12-hour clock format (ending in AM or PM) 
* a duration time that indicates the number of hours and minutes
* (optional) a starting day of the week, case insensitive

The function should add the duration time to the start time and return the result.

If the result will be the next day, it should show `(next day)` after the time. If the result will be more than one day later, it should show `(n days later)` after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.

Below are some examples of different cases the function should handle. Pay close attention to the spacing and punctuation of the results.
```py
add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
```

Do not import any Python libraries. Assume that the start times are valid times. The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number.

### Development

Write your code in `time_calculator.py`. For development, you can use `main.py` to test your `time_calculator()` function. Click the "run" button and `main.py` will run.

### Testing 

The unit tests for this project are in `test_module.py`. We imported the tests from `test_module.py` to `main.py` for your convenience. The tests will run automatically whenever you hit the "run" button.

### Submitting

Copy your project's URL and submit it to freeCodeCamp.
"""

DAY_WEEK = {1: "Monday", 2: "Tuesday", 3: "Wednesday",
            4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}


def add_time(start, duration, day=None):

    # Handling start time and duration time
    start_hour, start_minute = parse_time_12_to_24(start)
    duration_hour, duration_minute = duration.split(":")

    # add minutes and handle if minutes over 60
    extra_hour, final_minute = divmod((start_minute+int(duration_minute)), 60)
    final_hour = start_hour + extra_hour + int(duration_hour)

    # handle if hour overflow
    elapsed_day, final_hour = divmod(final_hour, 24)

    # ready time and day passed string
    new_time = parse_time_24_to_12(final_hour, final_minute)
    if elapsed_day:
        day_passed = day_printer(elapsed_day)

    current_day_idx = 0
    # handle day of the week
    if isinstance(day, str):
        handled_day = day.capitalize()
        for idx, day in DAY_WEEK.items():
            if day == handled_day:
                current_day_idx = idx
                break

    if current_day_idx:
        new_day_idx = elapsed_day + current_day_idx
        while new_day_idx > 7:
            new_day_idx -= 7
        if not elapsed_day:
            return new_time + ", " + handled_day
        new_day = DAY_WEEK.get(new_day_idx)
        return new_time+", "+new_day + day_passed

    if elapsed_day:
        return new_time + day_passed

    return new_time


def day_printer(elapsed_day):
    return f" ({elapsed_day} days later)" if elapsed_day > 1 else f" (next day)"


def parse_time_12_to_24(time):
    # input is string, example: 11:30 AM
    # takes 12-hour clock format and changes it into 24 hour format    return
    # returns an integer for downstream calculation
    temp_time, period = time.split(" ")
    hour, minutes = temp_time.split(":")
    hour = int(hour)
    if hour != 12 and period == "PM":
        hour += 12

    if hour == 12 and period == "AM":
        hour = 0
    return hour, int(minutes)


def parse_time_24_to_12(hour, minutes):
    if minutes < 10:
        minutes = '0' + str(minutes)
    if hour == 0:
        return f"12:{minutes} AM"
    if hour == 12:
        return f"12:{minutes} PM"
    if hour > 12:
        hour -= 12
        return f"{hour}:{minutes} PM"
    return f"{hour}:{minutes} AM"
