def greedy_selection_sort(arr):
    # Length of the array
    n = len(arr)

    # Greedy approach to sorting
    for i in range(n):
        min_index = i

        # Find the smallest element in the remaining unsorted portion
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the current element
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"Step {i+1}: {arr}")


if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Original Array:", arr)
    greedy_selection_sort(arr)
    print("\nSorted Array:", arr)
