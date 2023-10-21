def sort(arr):
    for i in range(len(arr) - 1):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        if i != min:
            # swapping
            arr[i], arr[min] = arr[min], arr[i]


if __name__ == "__main__":
    a = [1, 5, 2, 6, 3, 10, 3, 4, 6]
    sort(a)
    print(a)
