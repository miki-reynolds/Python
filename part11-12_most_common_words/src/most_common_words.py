def most_common_words(filename: str, lower_limit: int):
    words = []
    with open(filename) as file:
        for line in file:
            line = line.replace(".", "")
            line = line.replace(",", "")
            line = line.strip().split()
            for word in line:
                words.append(word)
 
    return {word: words.count(word) for word in words if words.count(word) >= lower_limit}


# most_common_words("comprehensions.txt", 3)