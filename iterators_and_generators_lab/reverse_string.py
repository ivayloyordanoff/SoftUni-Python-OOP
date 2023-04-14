def reverse_text(string: str):
    for char in reversed(string):
        yield char
