# IOET Employee Payment Exercise - README
## Solution Overview

ioet_employee_payment is a project developed for a job apply. It is a Console App that shows the amount to be paid to an employee based on an given schedule.
This project could be written in any programming language. Python was used because its legibility, multi-paradigm support and simple usage, however.
The exercise asked to return a salary based on worked hours in a schedule, for an employee. The next example was given:

>**Case 1**:
>
>INPUT:
>
>RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
>
>OUTPUT:
>
>The amount to pay RENE is: 215 USD
>
>**Case 2**:
>
>INPUT:
>
>ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
>
>OUTPUT:
>
>The amount to pay ASTRID is: 85 USD

So, in this case, the first approach was to translate the given input into valid data to work with. To do that, an Employee Mapper was developed. This mapper validates and unwrapps each data set provided.
Next, some game-rules were given, as shown below:

>Monday - Friday
>
>00:01 - 09:00 25 USD
>
>09:01 - 18:00 15 USD
>
>18:01 - 00:00 20 USD
>
>Saturday and Sunday
>
>00:01 - 09:00 30 USD
>
>09:01 - 18:00 20 USD
>
>18:01 - 00:00 25 USD

This means that an employee payment depends on the days worked and the hours beetween them. For that, a calculator was developed.
The calculator analyze the given data by the mapper, compares days and schedules to return the amount of money to be paid to a certain employee.

Finally, a .txt file containing all data is the absolute input. This file contains all data sets to be analized. To read the data, a loader was developed. This loader reads and extracts all datasets from the file and returns a list containing the data.

## Architecture

The project has some modules:
- Main app ([main.py](main.py))
- File Reader ([reader.py](./calculator/reader.py))
- Employee Mapper ([mapper.py](./calculator/mapper.py))
- Salary Calculator ([calc.py](./calculator/calc.py))

Each of these modules are related between themselves as the image shown below:

![Product flow chart](product_flow_chart.png)

The numbers between connectors indicate different processes happening in the modules. These processes are:
1. A .txt file is used as input to provide the necesary data for the salary calculation.
2. Main calls File Reader to open and extract the data inside .txt file. File Reader returns a list with the data sets.
3. Main calls Employee Mapper to unwrapp the list, validates and returns the converted data lists into processable data usable by Salary Calculator.
4. Main calls Salary Calculator to process data returned from Employee Mapper. Then Salary Calculator returns the amount to be paid to an employee.
5. Main shows the info into the console and screen (employee & amount to be paid), providing as well any error in datasets inside the .txt file.

## Compile and execution instructions:
There are two options to compile and execute this project:

1. Using the 'main.exe' file from 'dist' folder.
2. Clone or download all the repository. This option needa to install Python in your computer. Use 3.9.7 version. [[link here]](https://www.python.org/downloads/release/python-397/)

### 1. Executable file option:
- Download the 'main.exe' file from 'dist' folder.
- Open a terminal or console.
- Execute via command 'main.exe', this will initialize the app.
- Press enter to proceed to load a file into the app. If you have a .txt file in the same directory of 'main.exe', you just need to write the file name and extension, for example: 'data.txt'. Otherwise, you will need to write a valid directory and file name like this: 'main/pc/Downloads/data.txt'.
- The .txt file must have valid data to analize, for example: 'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00'; otherwise, it will shows an error. 

### 2. Clone or download repository option:
- Download and install Python from the link given above. Check your operating system and select the right choice.
- Clone the repository in a directory of your computer via git commands or download directly as a zip file. If you downloaded the repository, unzip it.
- Now you can run the app via terminal or console.
- Open a terminal or console.
- Go via `cd` command to the folder containing all the files containing the app.
- Write `python main.py` in the console to run the app.
- As the executable file option, press 'enter' to proceed to load a file into the app. If you have a .txt file in the same directory of the app, you just need to write the file name and extension, for example: 'data.txt'. Otherwise, you will need to write a valid directory and file name like this: '/home/pc/Downloads/data.txt'.
- You can try to write and enter 'data.txt' to the app for seeing an example.


