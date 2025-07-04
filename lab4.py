string = input("Enter a string: ")
count = {}
for c in string:
    if c in count:
        count[c] += 1  
    else:
        count[c] = 1   
print("Character counts:")
for c, count in count.items():
    print(f"'{c}': {count}")