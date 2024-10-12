def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            return iterations, arr[mid]

        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    return iterations, upper_bound

sorted_arr = [1.1, 2.3, 3.5, 4.8, 6.7, 8.9, 10.2]
targ = 5.0

iter, up_bound = binary_search(sorted_arr, targ)
print(f"Кількість ітерацій: {iter}")
print(f"Верхня межа: {up_bound}")
