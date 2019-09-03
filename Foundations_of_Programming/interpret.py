# zip()
def interpret(value, commands, args):
  for command, arg in zip(commands, args):
    if command not in ["+","-","*"]:
      return -1
    if command == "+":
      value += arg
    if command == "-":
      value -= arg
    if command == "*":
      value *= arg
  
  return value
