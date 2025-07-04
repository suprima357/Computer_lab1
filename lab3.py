i=int(input("how many numbers do you want to enter: "))
a=[]
for n in range(i):
    num=int(input("enter numbers: "))
    a.append(num)
even = [num for num in a if (num % 2 == 0)]
print("Even numbers: ", even)