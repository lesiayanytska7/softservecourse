def solution(number):
  '''finish the solution of multiple below 10'''
  return sum(x for x in range(number)
  if x % 3 == 0 or x % 5 == 0)