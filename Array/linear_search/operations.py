arr = [i + 43 for i in range(100)]


def linear_search(arr, value):
    for idx, i in enumerate(arr):
        if i == value:
            return idx
    return -1


value_to_find = 76
res = linear_search(arr, value_to_find)

if res == -1:
    print("value not found")
else:
    print(f"value {value_to_find} in index {res}")
