# Build-a-Time-Calculator-Project

Second project from  FreeCodeCamp.org in the Scientific Computing with Python curriculum.

## The rules of the project (Copy from FreeCodeCamp.org)

Write a function named add_time that takes in two required parameters and one optional parameter:

a start time in the 12-hour clock format (ending in AM or PM)
a duration time that indicates the number of hours and minutes
(optional) a starting day of the week, case insensitive
The function should add the duration time to the start time and return the result.

If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.

Below are some examples of different cases the function should handle. Pay close attention to the spacing and punctuation of the results.

## Example

```python
from project_module import add_time

print(add_time("3:00 PM", "3:10"))
# 6:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# 12:03 PM

print(add_time("10:10 PM", "3:30"))
# 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tueSday"))
# 12:03 AM, Thursday (2 days later)
