a= int(input("Enter the first number: "))
b = int(input("Enter the Second number: "))
l=[]
for i in range(a):
    l.append(1)
for i in range(b):
    l.append(1)
print(f"sum of {a} and {b} : {len(l)}")
           or
def addition (a,b):
    print(f"the sum of {a} and {b} is" , sum({a,b}))
addition(20,30)

