
n = int(input("Enter the number of elements (N): "))


array = []
print(f"Enter {n} integers:")
for i in range(n):
    element = int(input(f"Element {i+1}: "))
    array.append(element)


target = int(input("Enter the number to search for: "))


found = False
position = -1

for index in range(len(array)):
    if array[index] == target:
        found = True
        position = index + 1  
        break  


if found:
    print(f"\nSuccess: The number {target} is present in the array.")
    print(f"Position: {position}")
else:
    print(f"\nResult: The number {target} is not present in the array.")


