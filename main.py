import employee_mapper
import loader
import salary_calculator
import platform
import os
from time import sleep


def clear_os_type():
    os_type = platform.system()
    if os_type == 'Windows':
        os.system('cls')
    elif os_type == 'Linux':
        os.system('clear')


def screen_print(init=True):
    intro_text = '- IOET EMPLOYEE PAYMENT CALCULATOR -'
    center_values = '*' * ((80 - len(intro_text)) // 2)
    print('*' * 80)
    print(center_values + intro_text + center_values)
    print('*' * 80)
    if not init:
        pass
    else:
        print('Initializing')
        for i in range(1, 4):
            sleep(1)
            print('.' * i)
        print('Succeed')
        sleep(1)


if __name__ == '__main__':
    clear_os_type()
    screen_print()
    while True:
        clear_os_type()
        screen_print(False)
        file_name = input('Put the directory and file name: ')
        data_list = loader.loader(file_name)
        for i, data in enumerate(data_list):
            try:
                employee_name, schedule = employee_mapper.unwrap_info(data)
            except ValueError:
                print(f'Error in dataset {i + 1}.')
                pass
            else:
                payment = salary_calculator.calculate_salary(schedule)
                formatted_payment = "${:,.2f}".format(payment)
                print(f'The amount to pay to {employee_name} is: {formatted_payment}')
        break
