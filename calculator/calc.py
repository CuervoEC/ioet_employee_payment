from calculator import Day

# DATA AND GAME RULES
weekdays = [day.name for day in Day][:5]
weekend_days = [day.name for day in Day][5:]
weekdays_dict = {       # hour_ranges ref:
    25: [0, 540],       # 00:01 - 09:00     [0][0] - [0][1]
    15: [540, 1080],    # 09:01 - 18:00     [1][0] - [1][1]
    20: [1080, 1440]    # 18:01 - 00:00     [2][0] - [2][1]
}
weekend_dict = {
    30: [0, 540],       # 00:01 - 09:00     [0][0] - [0][1]
    20: [540, 1080],    # 09:01 - 18:00     [1][0] - [1][1]
    25: [1080, 1440]    # 18:01 - 00:00     [2][0] - [2][1]
}


def _cases_comparator(start: int, finish: int, payment_dict: dict) -> float:
    """Compares all possible schedules and return the calculated salary for that input"""
    payment_value = [key for key in payment_dict.keys()]
    hour_ranges = [value for value in payment_dict.values()]
    if start > hour_ranges[0][0] and finish <= hour_ranges[0][1]:
        return (finish - start) * payment_value[0] / 60

    elif hour_ranges[0][0] < start <= hour_ranges[0][1] and finish <= hour_ranges[1][1]:
        return ((hour_ranges[0][1] - start) * payment_value[0] +
                (finish - hour_ranges[1][0]) * payment_value[1]) / 60

    elif hour_ranges[0][0] < start <= hour_ranges[0][1] and finish <= hour_ranges[2][1]:
        return ((hour_ranges[0][1] - start) * payment_value[0] +
                (hour_ranges[1][1] - hour_ranges[1][0]) * payment_value[1] +
                (finish - hour_ranges[2][0]) * payment_value[2]) / 60

    elif hour_ranges[1][0] < start and finish <= hour_ranges[1][1]:
        return (finish - start) * payment_value[1] / 60

    elif hour_ranges[1][0] < start <= hour_ranges[1][1] and finish <= hour_ranges[2][1]:
        return ((hour_ranges[1][1] - start) * payment_value[1] +
                (finish - hour_ranges[2][0]) * payment_value[2]) / 60

    else:
        return (finish - start) * payment_value[2] / 60


def calculate_salary(schedule) -> float:
    """Returns the salary of an input employee"""
    # Salary initialization
    salary = 0
    for value in schedule:
        # Unpacking
        day = value[0]
        worked_schedule = value[1]
        start_time = worked_schedule[0]
        finish_time = worked_schedule[1]
        if day in weekdays:
            salary += _cases_comparator(start_time, finish_time, weekdays_dict)
        elif day in weekend_days:
            salary += _cases_comparator(start_time, finish_time, weekend_dict)

    return round(salary, 2)
