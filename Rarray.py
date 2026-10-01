
n = int(input("Enter the number of elements (N): "))


array = []
print(f"Enter {n} integers:")
for i in range(n):
    element = int(input(f"Element {i+1}: "))
    array.append(element)


print("\nElements in reverse order:")


for index in range(len(array) - 1, -1, -1):
    print(array[index], end=" ")


