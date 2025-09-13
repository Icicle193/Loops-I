string = input("Enter a word ")

string2 = ('')

for i in string:
    string2 = i + string2

print("\nOriginal word = ", string)
print("Reversed word = ", string2)