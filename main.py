import employee_mapper
import loader
import salary_calculator


if __name__ == '__main__':

    while True:
        file_name = input('Put the directory and file name: ')
        data_list = loader.loader(file_name)
        for data in data_list:
            employee_name, schedule = employee_mapper.unwrap_info(data)
            payment = salary_calculator.calculate_salary(schedule)
            print(employee_name, payment)
        break
