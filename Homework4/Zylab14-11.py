#Sydney Ani PID:1869076

# Function to perform selection sort in descending order and trace the steps
def selection_sort_descend_trace(num_list):
    size = len(num_list)  # Get the size of the input list
    for i in range(size - 1):
        max_index = i  # Assume the current index is the maximum index
        for j in range(i + 1, size):
            # Loop through the remaining elements to find the actual maximum index
            if num_list[j] > num_list[max_index]:
                max_index = j  # Update the maximum index if a larger element is found

        # Swap the elements at 'i' and 'max_index' to move the maximum element to its correct position
        num_list[i], num_list[max_index] = num_list[max_index], num_list[i]

        # Print the current state of the list after the swap
        print(' '.join(map(str, num_list)), end=' ')
        print()

if __name__ == "__main__":
    # Prompt the user to input a list of numbers separated by spaces and convert them to integers
    num_list = list(map(int, input().split()))

    # Call the selection_sort_descend_trace function with the input list to sort it in descending order
    selection_sort_descend_trace(num_list)
