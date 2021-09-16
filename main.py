from calculator import mapper
from calculator import reader
from calculator import calc
from calculator import menu
import os
from time import sleep


def show_result(f_name):
    data_list = reader.read_file(f_name)
    for i, data in enumerate(data_list):
        try:
            employee_name, schedule = mapper.unwrap_info(data)
        except ValueError:
            print(f'Error in dataset {i + 1}.')
            pass
        else:
            payment = calc.calculate_salary(schedule)
            formatted_payment = f"${payment:,.2f}"
            print(f'The amount to pay to {employee_name} is: {formatted_payment}')


if __name__ == '__main__':
    menu.clear_os_type()
    menu.screen_print()
    # app options and exit
    while True:
        menu.clear_os_type()
        menu.screen_print(False)
        user_input = input('Press Enter to load a file, or enter "q" to exit: ')
        if user_input == 'q':
            menu.clear_os_type()
            break
        elif len(user_input) == 0:
            file_name = input('Put the directory and file name: ')
            if os.path.isdir(file_name) or os.path.isfile(file_name):
                if file_name.endswith('.txt'):
                    print("\nLoading...")
                    sleep(2)
                    show_result(file_name)
                    user_input = input('Do you need to analyze another file? Press "enter" to continue or "q" to exit: ')
                    if user_input == 'q':
                        menu.clear_os_type()
                        break
                else:
                    print('Wrong file extension')
            else:
                print('No such file or directory')
                sleep(1)
        else:
            print('Try again!')
            sleep(1)
