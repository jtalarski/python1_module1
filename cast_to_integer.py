"""
Program: cast_to_integer.py
Author: Jim Talarski
Last date modified: 09/20/22

The purpose of this program is to accept any input,
convert to an integer type and output the integer.
"""

my_input0 = 30
my_input1 = 30.5
my_input2 = (6 * 5)
my_input3 = (30 % 1)
my_input4 = "red"

print('Evaluated 30', 'expected to see output of 30 and got', (int(my_input0)))
print('Evaluated 30.5', 'expected to see output of 30 and got', (int(my_input1)))
print('Evaluated (6*5)', 'expected to see output of 30 and got', (int(my_input2)))
print('Evaluated (30%1)', 'expected to see output of 0 and got', (int(my_input3)))
print("Evaluated 'red' ", 'expected to see an error and got', (int(my_input4)))

"""
When the program is run the expected output is returned. 
Curious to me is that the error related to the my_input4 variable is 
returned first before the other results.

Recapping in the assignment comment format:
  Input         Expected Output     Actual Output
0 30            30                  30
1 30.5          30                  30
2 (6*5)         30                  30
3 (30%1)        0                   0
4 'red'         error               error
"""
