file = open("Test.txt")

print(file.read())    # read and print all the contents from the Test.txt path
print(file.readline())   # read the single line from test.txt path
print(file.readline())   # read the single line from test.txt path
print(file.read(9))

file.close()

#print line by line using readline method

line = file.readline()
while line!="":
    print(line)
    line = file.readline()

for i in file.readline():
    print(line)
file.close()
#################################################################################################
with open('Test.txt','r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('Test.txt',"w") as writer:
        for line in reversed(content):
            writer.write(line)

#############################################################################################


