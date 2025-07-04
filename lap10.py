d = {}
n = int(input("Enter number of key-value pairs: "))
i = 0
while i < n:
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value
    i += 1

print("The dictionary is:", d)
search_key = input("Enter key to search: ")
if search_key in d:
    print("Value:", d[search_key])
else:
    print("Key not found.")
