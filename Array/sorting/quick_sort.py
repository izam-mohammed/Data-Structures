def sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [i for i in arr if i < pivot]
    mid = [i for i in arr if i == pivot]
    right = [i for i in arr if i > pivot]

    return sort(left) + mid + sort(right)


if __name__ == "__main__":
    a = [6, 7, 2, 6, 1, 9, 34, 7]
    print(sort(a))
