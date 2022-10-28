cart = 0

if cart !=2: #raise Exception("count of cart is not matching")
    pass

assert (cart ==0)
print("there is no assertion error")

assert (cart ==2)
print("there is no assertion error")

try:
    with open("Test.txt") as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("cleaning up the resources")




