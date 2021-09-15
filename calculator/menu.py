from time import sleep
import platform
import os


def screen_print(loader=True) -> None:
    """Print title screen with a simple toggle loader"""
    intro_text = '- IOET EMPLOYEE PAYMENT CALCULATOR -'
    center_values = '*' * ((80 - len(intro_text)) // 2)
    print('*' * 80)
    print(center_values + intro_text + center_values)
    print('*' * 80)
    if not loader:
        pass
    else:
        print('Initializing')
        for i in range(1, 4):
            sleep(1)
            print('.' * i)
        print('Succeed')
        sleep(1)


def clear_os_type() -> None:
    """Checks the current operating system for executing the right clear command to console"""
    os_type = platform.system()
    if os_type == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
