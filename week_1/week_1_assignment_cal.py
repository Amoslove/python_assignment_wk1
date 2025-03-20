# A simple calculator that ask the user to perform a little calculation
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("enter an operator(+,-,*,/): ").strip()

# performing the operation
if operator =="+":
  print("Debug: addition block entered")
  result = num1+num2
elif operator =="-":
  print("Debug: subtraction block")
  result = num1-num2
elif operator =="*":
  print("Debug: multiplication block entered")
  result = num1*num2
elif operator =="/":
  if num2 != 0:
    result = num1/num2
  else:
    result = "division by 0 is not allowed try a a different number."
else:
  result = "invalid operator!"





print(f"Debug: the result is {result}")
print(f"final result is: {num1} {operator} {num2} = {result}")