
n = int(input("Enter the number of elements (N): "))


array = []
print(f"Enter {n} integers:")
for i in range(n):
    element = int(input(f"Element {i+1}: "))
    array.append(element)


unique_array = []


for element in array:
    if element not in unique_array:
        unique_array.append(element)


print(f"\nOriginal Array: {array}")
print(f"New Array (Unique Elements Only): {unique_array}")

