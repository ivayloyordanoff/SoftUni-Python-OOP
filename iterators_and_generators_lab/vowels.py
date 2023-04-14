class vowels:
    vowels_list = ["a", "e", "i", "u", "y", "o"]

    def __init__(self, string: str):
        self.string = string
        self.result = [el for el in self.string if el.lower() in vowels.vowels_list]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.result):
            raise StopIteration

        self.index += 1

        return self.result[self.index - 1]
