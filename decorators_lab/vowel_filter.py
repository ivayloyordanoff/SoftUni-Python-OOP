def vowel_filter(function):
    def wrapper():
        letters = function()
        vowels = ["a", "e", "i", "o", "u"]

        return [l for l in letters if l in vowels]

    return wrapper
