# Sydney Ani PID: 1869076
def is_palindrome(word):
    # Remove spaces from the word
    word = word.replace(" ", "")

    # Convert the word to lowercase
    word = word.lower()

    # Check if the word is equal to its reverse
    if word == word[::-1]:
        return True
    else:
        return False


if __name__ == '__main__':
    input_word = input()

    if is_palindrome(input_word):
        print(input_word, "is a palindrome")
    else:
        print(input_word, "is not a palindrome")
