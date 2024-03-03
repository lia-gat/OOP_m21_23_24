class MinMaxWordFinder:
    def __init__(self):
        self.words_by_length = {}
        self.shortest_length = float('inf')
        self.longest_length = float('-inf')

    def add_sentence(self, sentence):
        words = sentence.split()
        for word in words:
            word = word.strip()
            if word:
                length = len(word)
                if length not in self.words_by_length:
                    self.words_by_length[length] = []
                self.words_by_length[length].append(word)
                self.shortest_length = min(self.shortest_length, length)
                self.longest_length = max(self.longest_length, length)

    def shortest_words(self):
        return sorted(self.words_by_length[self.shortest_length])

    def longest_words(self):
        return sorted(set(self.words_by_length[self.longest_length]))
     
# Ваш код

finder = MinMaxWordFinder()
finder.add_sentence('hello abc world')
finder.add_sentence('def asdf qwert')
print(' '.join(finder.shortest_words()))
print(' '.join(finder.longest_words()))

print('***')

# Ваш код

finder = MinMaxWordFinder()
finder.add_sentence('hello')
finder.add_sentence('abc')
finder.add_sentence('world')
finder.add_sentence('def')
finder.add_sentence('asdf')
finder.add_sentence('qwert')
print(' '.join(finder.shortest_words()))
print(' '.join(finder.longest_words()))

print('***')

# Ваш код

finder = MinMaxWordFinder()
finder.add_sentence('hello')
finder.add_sentence('  abc     def    ')
finder.add_sentence('world')
finder.add_sentence('            abc          ')
finder.add_sentence('asdf')
finder.add_sentence('qwert')
print(' '.join(finder.shortest_words()))
print(' '.join(finder.longest_words()))