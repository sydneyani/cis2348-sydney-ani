#Sydney Ani PID:1869076

# Assign a global variable
num_calls = 0

def partition(user_ids, i, k):
    # Pick the middle element as the pivot
    pivot_index = (i + k) // 2
    pivot_value = user_ids[pivot_index]

    # Initialize low and high index variables
    l = i
    h = k

    # Loop until low and high index cross each other
    while True:
        # Find element on left side that should be on right side
        while user_ids[l] < pivot_value:
            l += 1

        # Find an element on the right side that should be on the left side
        while user_ids[h] > pivot_value:
            h -= 1

        # If the low and high index have crossed, the partition is complete
        if l >= h:
            return h

        # Swap the elements at low and high index
        user_ids[l], user_ids[h] = user_ids[h], user_ids[l]

        # Move to the next indices
        l += 1
        h -= 1

def quicksort(user_ids, i, k):
    # Get num_calls variable
    global num_calls
    num_calls += 1

    if i >= k:
        return

    # Get pivot index
    pivot_index = partition(user_ids, i, k)

    # Sort the left and right partitions
    quicksort(user_ids, i, pivot_index)
    quicksort(user_ids, pivot_index + 1, k)


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    # Initial call to quicksort
    quicksort(user_ids, 0, len(user_ids) - 1)

    # Print number of calls to quicksort
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)
