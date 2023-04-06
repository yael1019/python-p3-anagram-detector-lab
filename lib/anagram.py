class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, anagrams):
        result = []
        list_of_letters = list(self.word)
        list_of_letters.sort()
        # print(list_of_letters)
        for word in anagrams:
            anagram = list(word)
            anagram.sort()
            # print(anagram)
            if list_of_letters == anagram:
               result.append(word)
        
        return result



# Anagram("word")
# Anagram("olleh").match(["hello", "goodbye"])