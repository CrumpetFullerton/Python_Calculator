def add(n1, n2):
  """Returns the Sum of 2 numbers"""
  return n1+n2
def subtract(n1, n2):
  """Returns the difference of 2 numbers"""
  return n1 - n2
def multiply(n1,n2):
  """Returns the product of 2 numbers"""
  return n1 * n2
def divide(n1, n2):
  """Returns the division of 2 numbers"""
  return n1 / n2


operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide,

}
def calulator():
  """Calculator"""
  end_yet = False
  num1 =float(input("what is the first number?: "))

  for key in operations:
    print(key)
  while not end_yet:
    operator_symbol = input("Pick an Operation: ")
    num2 = float(input("what is the next number?: "))
    Calc_Function = operations[operator_symbol]
    answer = Calc_Function(num1, num2)
    print(f"{num1} {operator_symbol} {num2} = {answer}")
    num1 = answer
    end = input("Type 'Exit' to exit, Type 'New' to start a new calculation, type anything else to continue calculating with {num1}: ")
    if end == "Exit":
      end_yet = True
    elif end == "New":
      end_yet = True
      calulator()
calulator()


