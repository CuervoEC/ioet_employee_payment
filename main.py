import employee_mapper
import loader
import salary_calculator
import menu


def show_result(f_name):
    data_list = loader.load_file(f_name)
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


if __name__ == '__main__':
    menu.clear_os_type()
    menu.screen_print()
    while True:
        menu.clear_os_type()
        menu.screen_print(False)
        user_input = input('Please, write "q" ')
        file_name = input('Put the directory and file name: ')
        show_result(file_name)
        break

