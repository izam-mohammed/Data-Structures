def binary_search(arr, target, low=None, high=None) -> int:
    if not low:
        low = 0
    if not high:
        high = len(arr) - 1

    if low > high:
        return -1

    mid = (high + low) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)


arr = [i for i in range(3, 13)]
target = 8
print(binary_search(arr, target))
