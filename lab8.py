names = []
n = int(input("Enter how many names you want to input: "))
for i in range(n):
    name = input("Enter name: ")
    names.append(name)

name_count = {}

for name in names:
    if name in name_count:
        name_count[name] += 1
    else:
        name_count[name] = 1

print("Name Counts:")
for name in name_count:
    print(f"{name}: {name_count[name]}")
