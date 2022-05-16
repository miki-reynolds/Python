def filter_forbidden(string: str, forbidden: str):
    return "".join([letter for letter in string if letter not in forbidden])



# sentence = "Once! upon, a time: there was a python!??!?!"
# filtered = filter_forbidden(sentence, "!?:,.")
# print(filtered)
