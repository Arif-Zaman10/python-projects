## Simple Python Calculator

This is a small command-line calculator written in Python. It lets you perform basic arithmetic operations (+, –, *, /) on two numbers and either continue calculating with the result, start a new calculation, or exit.

## How It Works
- When you run the script, it asks for the first number.
- It shows the available operations: +  -  *  /.
- You pick an operation, then enter the next number.
- It prints the result in the format: number operation next_number = result.
- After each calculation you can:
  * Type `y` to continue calculating with the current result.
  * Type `n` to start a new calculation with a new first number.
  * Type anything else to quit the program.


## Notes
- The script uses float input so you can work with decimal numbers.  
- Division by zero will raise an error — be careful when dividing.  
- The calculator() function is currently defined inside the loop for simplicity, but it can be moved outside for efficiency.


