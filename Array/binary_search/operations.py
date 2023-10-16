def binary_search(arr, value):
    arr.sort()
    left = 0
    right = len(arr)-1
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] == value:
            return mid
        elif value < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

arr = [i+13 for i in range(100)]
res = binary_search(arr, 44)

if res == -1:
    print('value not found')
else:
    print(f'value found at {res}')