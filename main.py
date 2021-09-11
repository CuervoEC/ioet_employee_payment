def decipher(text):

    week_days = ['MO', 'TU', 'WE', 'TH', 'FR']
    weekend_days = ['SA', 'SU']

    mon_fri_dict = {25: [0, 540],       # 00:01 - 09:00
                    15: [540, 1080],    # 09:01 - 18:00
                    20: [1080, 1440]}   # 18:01 - 00:00

    sat_sun_dict = {30: [0, 540],       # 00:01 - 09:00
                    20: [540, 1080],    # 09:01 - 18:00
                    25: [1080, 1440]}   # 18:01 - 00:00

    name, schedule = text.split('=')[0], text.split('=')[1]

    for day in schedule.split(','):
        code_day, hours = day[0:2], day[2:].split('-')
        for i in range(len(hours)):
            (h, m) = hours[i].split(':')
            hours[i] = int(h)*60 + int(m)

        if hours[0] > 1 and hours[1] == 0:
            hours[1] = 1440

        return name, code_day, hours


test_a = 'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00'
print(decipher(test_a))
test_b = 'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-00:00'
decipher(test_b)
