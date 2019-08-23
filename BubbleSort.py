array = list()
num = int(input("Enter how many elements you want:"))
print('Enter numbers in array: ')
for i in range(int(num)):
    n = int(input("num :"))
    array.append(n)
print('ARRAY: ',array)

# Traverse through all array elements
for i in range(n):
    # Last i elements are already in place
    for j in range(0, n - i - 1):
        # traverse the array from 0 to n-i-1
        # Swap if the element found is greater
        # than the next element
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
# Driver code to test above
print("Sorted array is:")
for i in range(len(array)):
    print("%d" % array[i]),
