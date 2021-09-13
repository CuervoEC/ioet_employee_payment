from ndays import Day

# DATA AND GAME RULES
weekdays = [day.value for day in Day][:5]
weekend_days = [day.value for day in Day][5:]
weekdays_dict = {
    25: [0, 540],       # 00:01 - 09:00
    15: [540, 1080],    # 09:01 - 18:00
    20: [1080, 1440]    # 18:01 - 00:00
}
weekend_dict = {
    30: [0, 540],  # 00:01 - 09:00 { init_time: 0, finish_time: 540  }
    20: [540, 1080],    # 09:01 - 18:00
    25: [1080, 1440]    # 18:01 - 00:00
}


# Need improvement with dictionary over dictionary reference instead of list
def _cases_comparator(start: int, finish: int, payment_dict: dict) -> float:
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
    # Salary initialization
    salary = 0
    for value in schedule:
        # Unpacking
        code_day = value[0]
        worked_schedule = value[1]
        start_time = worked_schedule[0]
        finish_time = worked_schedule[1]

        if code_day in weekdays:
            salary += _cases_comparator(start_time, finish_time, weekdays_dict)
        elif code_day in weekend_days:
            salary += _cases_comparator(start_time, finish_time, weekend_dict)

    return round(salary, 2)
