# IOET Employee Payment Exercise - README
## Solution Overview

ioet_employee_payment is a project developed for a job apply. It shows the amount to be paid to an employee based on an given schedule.
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
Finally, a .txt file containing all data is the absolute input. This file contains all data sets to be analized. To extract the info, a loader was developed. This loader extracts all datasets from the file and returns a list containing this data.

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

