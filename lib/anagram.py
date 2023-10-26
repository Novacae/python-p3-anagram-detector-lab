# your code goes here!
class Anagram :
    def __init__(self,word):
        self.word = word.lower()

    
    def match(self, candidates):
        matches = []
        sorted_word = sorted(self.word)

        for candidate in candidates:
            sorted_candidate = sorted(candidate.lower())

            if sorted_candidate == sorted_word and candidate.lower() != self.word:
                matches.append(candidate)

        return matches


   #def match():
        f#rom collections import Counter
        #if Counter(self.word) == Counter(self):
         #   return self
        #else:
        #    return []
