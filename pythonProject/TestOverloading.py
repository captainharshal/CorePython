from multipledispatch import dispatch

#passing one parameter
@dispatch(int,int)
def product(first,second):
    result = first*second
    print(result)

#passing two parameters
@dispatch(int,int,int)
def product(first,second,third):
    result = first * second * third
    print(result)

#you can also pass data type of any value as per requirement
@dispatch(float,float,float)
def product(first,second,third):
    result = first * second * third
    print(result)


#calling product method with 2 arguments
product(5,3) #this will give output of 15
product(2,3,2) #this will give output of 12
product(2.2,3.4,2.3) # this will give output of 17.985999999999997





# from multipledispatch import dispatch
#
# @dispatch(int, int)
# def policz(a, b):
#   return a + b
# @dispatch(str, int)
# def policz(a, b):
#   return a * b
# @dispatch(float, float)
# def policz(a, b):
#   return a * b
#
# def main(args):
#   print(policz(2, 2))
#   print(policz('a', 4))
#   print(policz(2.0, 2.3))
#   print("\nKoniec programu")
#
# if __name__ == '__main__':
#   import sys
#   sys.exit(main(sys.argv))