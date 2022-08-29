#interactive calculator
import operator
operations = { "+": operator.add, "-": operator.sub }
class FormulaError(Exception):
    pass
print("Enter value as a expression . Eg. 1+1")

def calculator(expr):
    split_value = [*expr]

    try:
        if(len(split_value) != 3):
            raise FormulaError
        elif(split_value[1] != "+" and split_value[1] != "-"):
            raise FormulaError

    except FormulaError:
        print("Please enter valid expression")
    if(split_value[1] == "+"):
        print(operations["+"](int(split_value[0]),int(split_value[2])))
    elif(split_value[1] == "-"):
        print(operations["-"](int(split_value[0]),int(split_value[2])))

while True:
  user_input = input('-> ')
  if user_input == 'quit':
    break
  calculator((user_input))