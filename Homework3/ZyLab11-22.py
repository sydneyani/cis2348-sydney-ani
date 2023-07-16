#Sydney Ani PID: 1869076

# Get the input list of words
input_list = input().split()

# Create a dictionary to store word frequencies
word_freq = {}

# Count the frequencies of words
for word in input_list:
    # Update the frequency count for the word
    word_freq[word] = word_freq.get(word, 0) + 1

# Print the words and their frequencies
for word in input_list:
    print(word, word_freq[word])
