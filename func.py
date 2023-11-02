def my_function():
 x=10 #x is local
 print(x)
my_function()


x=10 #global variable
def my_function():
 print(x)
my_function()