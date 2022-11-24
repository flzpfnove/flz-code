# flz-code
Programming language created by PFnove on YouTube

-

[value]s are always binary, unless otherwise specified

How to program in FLZcode:

1.    VALUES

1.1.1 Use C + [value] to use a specified value as input to the function you are executing

2.    VARIABLES

2.1   READING

2.1.1 Use R + [variable id (decimal)] to use a variable as input to the function you are executing

2.1.2 (2.2 and earlier) Use I + [input id (0 or 1)] to use one of the user inputs as input to the function you are executing


2.2   WRITING

2.2.1 Use -out to write the output of the executed function to the output (output is printed at the end of the code)

2.2.2 Use > + [variable id (decimal)] to write the output of the executed function to a variable

3.    FUNCTIONS

3.1   INPUT

3.1.2 (2.2) Use INPUT to make user input a number (binary), returns user input, invalid input = make user input a number again

3.1.2 (2.3 and above) Use INPUT + [default value] to make user input a number (binary), returns user input or default value (in case of invalid input)


3.2   OUTPUT

3.2.1 Use DEBUG + [value] to output a value to the terminal

3.2.2 (2.2 and above) Use ASCII + [value] + [newline (0 = newline, anything else = no newline)] to output an ASCII character to the terminal


3.3   IF

3.3.1 (2.1 and above) Use IF + [value] + [condition (=, >, <, >=, <=)] + [value] to execute a function only if the specified condition is met


3.4   GOTO

3.4.1 (2.1 and above) Use GOTO + [value] to jump to a specific line, doesn't return any value


3.5   ADD

3.5.1 Use ADD [value] [value] to add two values, returns sum of inputs


3.6   INVERT

3.6.1 (1.0) Use SUB+0 [value] to invert bits of a specified value, returns value with inverted bits

3.6.2 (1.0) Use SUB+1 [value] to multiply value by -1, returns VALUE x -1

3.6.3 (1.1 and above) Use INV+0 [value] to invert bits of a specified value, returns value with inverted bits

3.6.4 (1.1 and above) Use INV+1 [value] to multiply value by -1, returns VALUE x -1


3.7   TIMER

3.7.1 (2.3 and above) Use TIMER-START to start the software execution timer

4.    CONSOLE COMMANDS (2.2 and above)

4.1   EXIT

4.1.1 Use STOP to exit console mode

4.2   DUMP MEMORY

4.2.1 Use MEM-DUMP to see a dump of all reserved memory
