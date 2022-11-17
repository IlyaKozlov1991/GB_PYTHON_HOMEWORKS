Overview of complex numbers calculator by Kozlov Ilia

This method includes several  stages described in submethods which are internally processed:

Stage 1 

Initial Stage. Recieve a list including numbers and symbol representing operation to do. Input list is sorted to define the operation (submethod - find_operation)and then splited into two separate list which represent two complex numbers given by User (submethod - split_list).

Stage 2

Computational Stage. Once mathematical operation is difined and input numbers are prepared for further processing, the operation is performed. There are four kinds of operations described in the relevant submethods: addition, subtraction, multiplication and division. Each submethod is based on relevant algebraic formula.

Stage 3

Result Stage. Once the operation is completed, the Result is returned.