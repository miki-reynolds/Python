def formatted(numbers: list):
    new = []
    for item in numbers:
        item = f"{item:.2f}"
        new.append(item)
    return new