l1=[1,2,3,4,5,6,7,8,9]
l2=[5,10,15,20,25,30]
set1 = set(l1)
set2 = set(l2)
intersection = []
print(f"list 1 is {l1}")
print(f"list 2 is {l2}")
for i in set1:
    if i in set2:
        intersection.append(i)
print("Common elements:", intersection)