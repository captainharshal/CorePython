# Python example to show the working of multiple
# inheritance


class Base1(object):
    def __init__(self, str1):
        self.str1 = str1
        print(self.str1)


class Base2(object):
    def __init__(self,str2):
        self.str2 = str2
        print(self.str2)


class Derived(Base1, Base2):
    def __init__(self,str1,str2,str3):
        # Calling constructors of Base1
        # and Base2 classes

        Base1.__init__(self,str1)
        Base2.__init__(self,str2)

        self.str3 = str3
        print(self.str3)

    def printStrs(self):
        print(self.str1,self.str2,self.str3)


ob = Derived("Base1","Base2","Derived")
ob.printStrs()

# it prints the lookup order
print(Derived.__mro__)
print(Derived.mro())





# # Python example to show the working of multilevel
# # inheritance
#
# class Base(object):
#
# 	# Constructor
# 	def __init__(self, name):
# 		self.name = name
#
# 	# To get name
# 	def getName(self):
# 		return self.name
#
#
# # Inherited or Sub class (Note Person in bracket)
# class Child(Base):
#
# 	# Constructor
# 	def __init__(self, name, age):
#
# 		#Base.__init__(self, name)
# 		super().__init__(name)
#
# 		self.age = age
#
# 	# To get name
# 	def getAge(self):
# 		return self.age
#
# # Inherited or Sub class (Note Person in bracket)
#
#
# class GrandChild(Child):
#
# 	# Constructor
# 	def __init__(self, name, age, address):
#
# 		#Child.__init__(self, name, age)
# 		super().__init__(name, age)
#
# 		self.address = address
#
# 	# To get address
# 	def getAddress(self):
# 		return self.address
#
#
# # Driver code
# g = GrandChild("Geek1", 23, "Noida")
# print(g.getName(), g.getAge(), g.getAddress())




# # Python program to demonstrate
# # Hierarchical inheritance
#
# # Base class
# class Parent:
#     def func1(self):
#         print("This function is in parent class.")
#
# # Derived class1
#
#
# class Child1(Parent):
#     def func2(self):
#         print("This function is in child 1.")
#
# # Derivied class2
#
#
# class Child2(Parent):
#     def func3(self):
#         print("This function is in child 2.")
#
#
# # Driver's code
# object1 = Child1()
# object2 = Child2()
# object1.func1()
# object1.func2()
# object2.func1()
# object2.func3()
#
#
#
#
# # Python program to demonstrate
# # hybrid inheritance
#
#
# class School:
#     def func1(self):
#         print("This function is in school.")
#
#
# class Student1(School):
#     def func2(self):
#         print("This function is in student 1. ")
#
#
# class Student2(School):
#     def func3(self):
#         print("This function is in student 2.")
#
#
# class Student3(Student1, School):
#     def func4(self):
#         print("This function is in student 3.")
#
#
# # Driver's code
# object = Student3()
# object.func1()
# object.func2()




# # Python program to demonstrate
# # single inheritance
#
# # Base class
# class Parent:
#     def func1(self):
#         print("This function is in parent class.")
#
# # Derived class
#
#
# class Child(Parent):
#     def func2(self):
#         print("This function is in child class.")
#
#
# # Driver's code
# object = Child()
# object.func1()
# object.func2()