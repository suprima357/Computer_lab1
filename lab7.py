dict1={'x': 10,'y':30,'z':50}
dict2={'u': 30,'v':20,'z':75}
print(f"disctionary1: {dict1}")
print(f"disctionary1: {dict2}")
merge={}
for key in dict1:
    merge[key] = dict1[key]

for key in dict2:
    if key in merge:
        merge[key] += dict2[key]
    else:
        merge[key]= dict2[key]
print("Merged list :", merge)