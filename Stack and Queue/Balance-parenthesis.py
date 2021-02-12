def BalPar(expr):
  stack=[]
  for char in expr:
    print(char)
    if char in ["(", "{", "["]:
      stack.append(char)
    else:
      if not stack: #if stack is empty
        return False 
      curr_char=stack.pop()
      print(curr_char)
      if curr_char == '(':
        if char != ')':
          return False
      if curr_char == '{':
        if char != '}':
          return False
      if curr_char == '[':
        if char != ']':
          return False
  if stack:
    return False
  return True

expr='[()]{'
BalPar(expr)
