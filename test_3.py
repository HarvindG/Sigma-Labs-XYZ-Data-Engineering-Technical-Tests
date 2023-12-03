# The below function doesn't work correctly. It should sum all the numbers at the
# current time. For example, 01:02:03 should return 6. Improve and fix the function,
# and write unit test(s) for it. Use any testing framework you're familiar with.


# [TODO]: fix the function

def sum_current_time(time_str: str) -> int:
    """Expects data in the format HH:MM:SS"""

    if time_str:
        if (int(time_str[:2]) in range(0, 25)) and (int(time_str[3:5]) in range(0, 60)) and (int(time_str[6:8]) in range(0, 60)):
            return sum(int(num) for num in time_str.split(":"))

    return "Invalid time input"
