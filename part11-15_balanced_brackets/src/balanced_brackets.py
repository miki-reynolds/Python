




def matches(op, ed):
    open = "(["
    close = ")]"
    if(op in open and ed in close):
      return open.index(op) == close.index(ed)
    else:
      return False

def balanced_brackets(string: str):
    r = []
    for letter in string:
        if letter in "()[]":
            r.append(letter)

    if len(r) == 0:
        return True
    if len(r) != 0 and not matches(r[0], r[-1]):
        return False

    # remove first and last character
    return balanced_brackets(r[1:-1])

