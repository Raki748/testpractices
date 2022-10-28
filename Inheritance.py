# from classmethodobject import calculator
#
#
# class childclass(calculator):
#     number = 100
#
#     def __init__(self):
#         calculator.__init__(self, 5, 6)
#
#     def completed(self):
#         return self.number + self.num + self.summation()
#
#
# obj = childclass()
# print(obj.completed())


str = " Rakesh is good boy "
str1 = "Rajesh also good boy"
str2 = "Rakesh"

print(str[7])
print(str[9:15])

Concat = str + str1
print(Concat)

print(str1.split('o'))
print(str1.split(' '))
print(str.strip())
print(str.lstrip())
print(str.rstrip())

print(str.replace(str,str1))

print(str2 in str)

tuple = ("Rakesh","is","iko","boy")
tuple1 = " " .join(tuple)
print(tuple1)

tuple = ("Rakesh","is","iko","okij")
tuple1 = ' '.join(tuple)
print(tuple1)

a,b,c = ("raj",6,4.5)
print("{} {}".format("the value of b is",b))




