from TestClosure1 import Addition

class Demo:
    obj = Addition(1000, 2000)

    # display result
    Result = obj.display()
    Result()

    del Addition.display

    Result()
    Addition.display()



# def print_msg(msg):
#     # This is the outer enclosing function
#
#     def printer() -> object:
#         # This is the nested function
#         print(msg)
#
#     return printer  # returns the nested function
#
#
# # Now let's try calling this function.
# # Output: Hello
# another = print_msg("Hello")
# another()
#
# del print_msg
#
# another()
# print_msg("Hello")



# def make_multiplier_of(n):
#     def multiplier(x):
#         return x * n
#     return multiplier
#
#
# # Multiplier of 3
# times3 = make_multiplier_of(3)
#
# # Multiplier of 5
# times5 = make_multiplier_of(5)
#
# # Output: 27
# print(times3(9))
#
# # Output: 15
# print(times5(3))
#
# # Output: 30
# print(times5(times3(2)))