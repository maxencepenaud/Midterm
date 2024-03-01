file_name = "text"
fd = open(file_name) # r is implicit
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
fd.close()