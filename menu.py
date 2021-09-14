from time import sleep
import platform
import os


def screen_print(init=True) -> None:
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


def clear_os_type() -> None:
    os_type = platform.system()
    if os_type == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
