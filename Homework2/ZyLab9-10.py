# Sydney Ani PID: 1869076
import csv

if __name__ == '__main__':
    filename = input()

    word_freq = {}

    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            for word in row:
                word = word.strip()
                if word not in word_freq:
                    word_freq[word] = 1
                else:
                    word_freq[word] += 1

    for word, freq in word_freq.items():
        print(word, freq)
