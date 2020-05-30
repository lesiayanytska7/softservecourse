#first approach by characters
def my_function(st):
  return st[::-1]
sentense = my_function("Hello World")
print(sentense)

#second approach by characters
str = 'Hello World'
reversed=''.join(reversed(str))
print(reversed)

#approach by words
string = "Hello World"
words = string.split()
words = list(reversed(words))
print(" ".join(words))
