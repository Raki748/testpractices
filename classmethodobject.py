# C = [1, 2, 3, 4, 5, 6, 7]
# print(len(C))
#
# class employeesdb:
#     employeename = "rakesh"
#     employeesal = 10000
#     employeeid = "avthjt"
#
#     def emplyeesdatabase(self):
#         print("Employeesdb details in class")
#
# obj = employeesdb()
# obj.emplyeesdatabase()
# print(obj.employeename)
# print(obj.employeesal)
# print(obj.employeeid)

class calculator:
    num = 100

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def inputdata(self):
        print("i am executing the method as class")

    def summation(self):
        return self.a + self.b + calculator.num

obj = calculator(20,50)
obj.inputdata()
obj.summation()
print(obj.summation())
print(obj.inputdata())
print(obj.num)
