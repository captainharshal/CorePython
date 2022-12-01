from MaxNumber1 import numswap as N1
from MaxNumber2 import numswap as N2

N1(20, 30)
N2(50, 10)



# l1 = [1,2,3,4,5]
# l2 = l1 [:]
# l2.pop(2)
#
# print (*l1)
# print (*l2)


# inputList = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
#
# print(*inputList)
# inputList[2][2].insert(2, 7000)
# print(*inputList)



# Print without newline in Python 3.x without using for loop

# l=[1,2,3,4,5,6]
#
# # using * symbol prints the list
# # elements in a single line
# print(*l)



# List = [[2,3,4],[1, 4, 16, 64],[3, 6, 9, 12]]
#
# # Sort each sublist
# sortList = lambda x: (sorted(i) for i in x)
#
# # Get the second largest element
# secondLargest = lambda x, f : [y[len(y)-2] for y in f(x)]
# res = secondLargest(List, sortList)
#
# print(res)