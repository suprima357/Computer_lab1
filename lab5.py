prime = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}
n = int(input("Enter a number: "))
if n in prime:
    print(f"{n} is in set.")
else:
    print(f"{n}  is not in set.")