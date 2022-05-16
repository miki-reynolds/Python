def find_words(search_term: str):
    dictionary = []
    with open("words.txt") as file:
        for line in file:
            line = line.replace("\n", "")
            dictionary.append(line)
    found = []   
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for item in dictionary: 

        if search_term.lower() == item:
            found.append(item)

        elif search_term[0] == "*" and search_term[1:].lower() == item[-len(search_term[1:]):]:
            found.append(item) 

        elif search_term[-1] == "*" and search_term[:-1].lower() == item[:len(search_term)-1]:
            found.append(item) 

        elif "." in search_term and len(search_term) == len(item):
            for i in search_term:
                if i == ".":
                    for letter in alphabet:
                        i == letter
                        found
            


                


       

    print(found)

find_words("ca.")

        