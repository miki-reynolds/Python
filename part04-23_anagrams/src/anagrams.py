def anagrams(word1, word2):
    list1 = []
    for n in word1:
        list1.append(n)
    list1.sort()

    list2 = []
    for n in word2:
        list2.append(n)
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False





    

