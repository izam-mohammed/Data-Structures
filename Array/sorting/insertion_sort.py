def sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == "__main__":
    a = [4, 1, 4, 7, 4, 2, 5, 19, 8]
    sort(a)
    print(a)
