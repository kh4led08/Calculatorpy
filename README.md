Calculator.py



Calculator.py is my first repository on GitHub. It consists of a Python file that runs directly in your terminal to perform calculations.



How It Works



When you run the script, you will be prompted with the following inputs:


Enter first number: 

Enter operation (+, -, \\\*, /, ^, r): 

Enter second number: 




Once submitted, the script will calculate and return the answer to your math equation.


| Operator | Operation      | Example Layout |

| -------- | -------------- | -------------- |

|  +       | Addition       |  5 + 3         |

|  -       | Subtraction    |  10 - 4        |

|  *       | Multiplication |  2.5 * 4       |

|  /       | Division       |  9 / 3         |

|  ^       | Exponentiation |  2 ^ 3         |

|  r       | N-th Root      |  2 r 4         |


UPDATE LOG

v1.0.1: Fixed a bug that threw an error when continuing script after a division and added a special condition to prevent you from doing a useless equation involving a number one does not mention.

v1.0.0: Release update (more detailed information coming soon)

|
|
|


Important Notes

Update 1.1.0 is in development. The update will have more equations, including sine, cosine, and tangent and all alike.

|

About Roots: First enter the degree (index), select r as your operation, and then enter the radicand.

About Complex Numbers: Although Python natively supports complex calculations, complex/imaginary number outputs have been disabled on this calculator to prevent floating-point precision errors.

Illogical math equations (like 1/0, 0^0, etc.) have also been disabled.

Also, don't think of setting every input to "67"...

Calculatorpy was made with light assistance from AI.

