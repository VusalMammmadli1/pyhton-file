#Task 1: check if number is greater than 7
number=int(input("Enter a number: "))
if number>7:
    print("Hello")

#Task 2: check if the entered name is John
name=input("Enter a name: ")
if name=="John":
    print("Hello John")
else:
    print("There is no such a name")
#Task 3: check if numbers in list that are multiples of 3
numbers=[1,3,7,9,10,12]
print("Multiples of 3 in numbers:")
for num in numbers:
    if num % 3 == 0:
        print(num)
#Task 4: check if this bracket is valid
example="[((())()(())]]"
print("Is the bracket valid?")
stack = []
for char in example:
    if char in "([":
        stack.append(char)
    elif char in ")]":
        if not stack:
            break
        stack.pop()
if stack:
    print("Not valid.")
else:
    print("Valid.")


