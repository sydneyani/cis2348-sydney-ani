#Sydney Ani PID:1869076

def selection_sort_descend_trace(num_list):
    size = len(num_list)
    for i in range(size - 1):
        max_index = i
        for j in range(i + 1, size):
            if num_list[j] > num_list[max_index]:
                max_index = j
        num_list[i], num_list[max_index] = num_list[max_index], num_list[i]
        print(' '.join(map(str, num_list)), end=' ')
        print()

if __name__ == "__main__":
    num_list = list(map(int, input().split()))
    selection_sort_descend_trace(num_list)
