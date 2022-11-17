# Interview Question #2
#
# "A palindrome is a string that reads the same forward and backward"
#
# For example: radar or madam
#
# Our task is to design an optimal algorithm for checking whether a given string is palindrome or not!

print("my code")
def palindrome_verifier(array):
    # setting start position
    start_index = 0
    end_index = len(array) - 1

    # checking dual sides.

    while end_index > start_index:
        if array[start_index] != array[end_index]:
            return False
        start_index += 1
        end_index -= 1
        return True


string = "malayalam"

palindrome = palindrome_verifier(string)
print(f"{palindrome}")





