
Greetings = "GoodMorning"
# if 6 > 3:
if Greetings == "GoodMorning":
    print("This is correct Statement")
else:
    print("This is not a correct Statement")
print("Entered above statement is correct")

List = [1,2,3,4,5,]
for i in List:
    print(i*2)
summation = 0
for i in range (100,10000):
    summation = summation+i
print(summation)

print("**************************************")
for k in range (1,50): # range should be 1 to 50 and difference of each number is 25 ans: 1, 26
    print(k)

print("**************************************")
for k in range (1,50,25): # range should be 1 to 50 and difference of each number is 25 ans: 1, 26
    print(k)

print("**************************************")
for k in range (50): # range should be 0 to 50 and difference of each number  ans :is 1 : 1 2 3 4 5
    print(k)


a = 5

while a > 1:
    if a != 3:
        print(a)
    a = a - 1
print("while loop execution is done")

a = 100

while a > 1:
    if a == 98:
        break
    print(a)
    a = a - 1
print("while loop execution is done")

a = 10

while a > 3:
    if a==8:
        a = a-1
        continue
    if a == 7:
        break
    print(a)
    a = a - 1
print("while loop execution is done")
G = [1,2,3,5,6,8,9,"raki",3.6]
print(len(G))

