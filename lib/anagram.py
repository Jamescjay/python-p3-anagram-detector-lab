# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def is_anagram(self, candidate):
        return sorted(self.word) == sorted(candidate.lower()) and self.word != candidate.lower()

    def match(self, word_list):
        return [candidate for candidate in word_list if self.is_anagram(candidate)]


listen = Anagram("listen")
result = listen.match(['enlists', 'google', 'inlets', 'banana'])
print(result)
