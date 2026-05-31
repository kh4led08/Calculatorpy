def startupcalculator():

    n1 = input("Enter first number: ")
    oper = input("Enter operation (+, -, *, /, ^, r): ")
    n2 = input("Enter second number: ")
   
    try:
        num1 = round(float(n1), 10)
        num2 = round(float(n2), 10)
    except ValueError:
        print("Error: Both inputs must be numbers.")
        startupcalculator()
        return


    if oper == "+": # Addition
        print(float(num1) + float(num2))   
        continuescript = input("Do you want to do a new calculation? (y/n): ")
        if continuescript == "y":
         startupcalculator()
    elif oper == "-": # Substraction
        print(float(num1) - float(num2))  
        continuescript = input("Do you want to do a new calculation? (y/n): ")
        if continuescript == "y":
            startupcalculator()
    elif oper == "*": # Multiplication
     print(float(num1) * float(num2))
     continuescript = input("Do you want to do a new calculation? (y/n): ")
     if continuescript == "y":
            startupcalculator()
    elif oper == "/": # Division
        if float(num2) == 0:
            print("Error: Division by zero is not allowed.")
            startupcalculator()
            return
        else:
          print(float(num1) / float(num2))   
          if continuescript == "y":
            startupcalculator()
    elif oper == "^": # Exponentiation
        if float(num1) == 0 and float(num2) == 0:
          print("Error: 0 to the power of 0 is not allowed.")
          startupcalculator()
          return
        else:
          print(float(num1) ** float(num2))
          continuescript = input("Do you want to do a new calculation? (y/n): ")
        if continuescript == "y":
           startupcalculator()
    elif oper == "r": # Roots
       if num1 == 0:
          print("Cannot take the zeroth root of a number.")
          startupcalculator()
          return
       else:
          rootresult = (num2 ** (1 / num1))
          if isinstance(rootresult, complex):
             print("Cannot take operations handling the imaginary unit.")
             startupcalculator()
             return
          else:
             print(rootresult)
             continuescript = input("Do you want to do a new calculation? (y/n): ")
             if continuescript == "y":
              startupcalculator()
    else:
     print("Invalid operation. Please enter one of the following: +, -, *, /, ^, r.")
     startupcalculator()
    

startupcalculator()
