def  search(products: list, criterion=lambda x: True):
    r = []
    for item in products:
        if criterion(item):
            r.append(item)
    return r

