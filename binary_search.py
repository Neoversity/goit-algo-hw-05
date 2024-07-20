def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (high + low) // 2
        mid_val = arr[mid]

        if mid_val < x:
            low = mid + 1
        elif mid_val > x:
            high = mid - 1
            upper_bound = mid_val
        else:
            return (iterations, mid_val)

    if low < len(arr):
        upper_bound = arr[low]
    else:
        upper_bound = None

    return (iterations, upper_bound)

def main():
    arr = [1.2, 2.4, 3.6, 4.8, 6.0, 7.2, 8.4, 9.6]
    x = 5.0

    result = binary_search(arr, x)
    print(result)  # Виведе: (3, 6.0)

if __name__ == "__main__":
    main()
