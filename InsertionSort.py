array = list()
num = int(input("Enter how many elements you want:"))
print('Enter numbers in array: ')
for i in range(int(num)):
    n = int(input("num :"))
    array.append(n)
print('ARRAY: ',array)
for i in range(1,len(array)):
    key= array[i]
    j = i
    while j>0 and array[j-1]> key:
        array[j]=array[j-1]
        j = j-1
    array[j]= key
print(array)
