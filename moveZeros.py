
n = int(input("Enter the number of elements (N): "))


array = []
print(f"Enter {n} integers:")
for i in range(n):
    element = int(input(f"Element {i+1}: "))
    array.append(element)


insert_pos = 0


for i in range(len(array)):
    if array[i] != 0:
        array[insert_pos] = array[i]
        insert_pos += 1


while insert_pos < len(array):
    array[insert_pos] = 0
    insert_pos += 1


print(f"\nRearranged Array: {array}")
