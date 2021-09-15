import re
from calculator.ndays import Day


def _validate_schedule_format(name, schedule):
    """Validate specific schedule format"""
    r = re.compile('[A-Z]{2}\d{2}:\d{2}-\d{2}:\d{2}')
    if r.match(schedule) is None:
        raise ValueError(f'Invalid schedule format for {name}')


def _validate_day(day):
    valid_days = [day.name for day in Day]
    if day not in valid_days:
        raise ValueError('Invalid day.')


def _validate_init_format(split_text):
    if len(split_text) != 2:
        raise ValueError('Invalid text was provided.')


def _validate_init_name_schedule(name, schedule):
    if not name or not schedule:
        raise ValueError('Name or schedule is empty.')


def unwrap_info(text):
    """Unravel input string to valid data"""
    split_text = text.split('=')
    _validate_init_format(split_text)

    name, schedule = split_text[0], split_text[1]
    _validate_init_name_schedule(name, schedule)

    day_hours = []
    day = ''
    for worked_schedule in schedule.split(','):
        _validate_schedule_format(name, worked_schedule)
        for d in Day:
            if d.value == worked_schedule[:2]:
                day = d.name
        _validate_day(day)
        hour = worked_schedule[2:].split('-')
        for i in range(len(hour)):
            (h, m) = hour[i].split(':')
            hour[i] = int(h) * 60 + int(m)
        if hour[0] > 1 and hour[1] == 0:
            hour[1] = 1440
        if hour[1] < hour[0]:
            raise ValueError('Incorrect schedule values. Final working hour is greater than initial.')
        # This data was changed from a dictionary to a list including each day, even it is repeated.
        day_hours.append([day, tuple(hour)])

    return name, day_hours
