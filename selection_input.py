def greedy_selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"Step {i + 1}: {arr}")


if __name__ == "__main__":
    user_input = input("Enter the elements of the array separated by spaces: ")
    arr = list(map(int, user_input.strip().split()))

    print("\nOriginal Array:", arr)
    greedy_selection_sort(arr)
    print("\nSorted Array:", arr)
