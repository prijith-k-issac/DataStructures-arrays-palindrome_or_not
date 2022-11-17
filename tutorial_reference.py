# solution in tutorial

print("tutorial code")

def palindrome_python(s):
    if s == s[::-1]:
        return True
    return False

if __name__ == "__main__":
    string = "hai"
    print(palindrome_python(string))