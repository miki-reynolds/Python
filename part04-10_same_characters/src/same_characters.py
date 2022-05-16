def same_chars(word, i1, i2):
    if i1 < len(word) and i2 < len(word):
        if word[i1] == word[i2]:
            return True
        else:
            return False
    else:
        return False


# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))