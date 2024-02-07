def sort(arr: list) -> list:
    n = len(arr)
    middle = n // 2 if n % 2 == 0 else (n // 2) + 1
    if n == 1:
        return arr

    left = arr[0:middle]
    right = arr[middle:n + 1]

    left = sort(left)
    right = sort(right)

    return merge(left, right)


def merge(left, right) -> list:
    i = 0
    k = 0
    arr = []

    while i < len(left) and k < len(right):
        if left[i] < right[k]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[k])
            k += 1

    while i < len(left):
        arr.append(left[i])
        i += 1
    while k < len(right):
        arr.append(right[k])
        k += 1

    return arr
