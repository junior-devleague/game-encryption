def changeChar(string, x, y):
  if len(string) == 0:
    return string
  char = string[0]
  if char == x:
    return y + changeChar(string[1:], x, y)
  return char + changeChar(string[1:], x, y)