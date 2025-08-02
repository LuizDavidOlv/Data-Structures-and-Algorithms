
from collections import Counter, defaultdict
from typing import Dict, List


class NextWordPredictor:
    def __init__(self, training_data: List[List[str]]):
        """
        Build a frquency table such that 
        table["I"] == Counter({'like': 2 , 'am': 1})
        """
        self._table: Dict[str, Counter] = defaultdict(Counter)

        # walk-through the whole dataset 
        for sentence in training_data:
            """
            zip(a,b) pair the elements at the same position in the two lists
            zip(["I","am","Sam"], ["am","Sam"]) produces:
                ("I", "am") 
                ("am", "Sam")

            This gives every consecutive bigram in the sentence
            If the sentence has N words, it will have N-1 bigrams
            """
            for current, nxt in zip(sentence, sentence[1:]):
                self._table[current.lower()][nxt.lower()] += 1


    def predict(self, word: str):
        counter = self._table.get(word.lower())

        if not counter:
            return None
        
        #`most_common` builds a heap of size 1 while scanning all n items
        # time complexity: O(n)
        result = counter.most_common(1)[0][0]
        
        return result

    
if __name__ == "__main__":
    training_data = [
        ["I", "am", "Sam"],
        ["you", "and", "I", "like", "salmo"],
        ["I", "like", "you"]
    ]

    predictor = NextWordPredictor(training_data)
    
    print(predictor.predict("I"))
    print(predictor.predict("am"))
    print(predictor.predict("you"))
    print(predictor.predict("heard"))



"""
Core idea:
    1. Look at every pair of consecutive words in the training sentences
    2. Count how often each second word follows the first. For "I", "am" appears once and "like" twice
    3. Store those in a dictionary of dictionaries, defaultdict(Counter) in python terms
    4. To predict the next word, we simply retrieve the dictionary of the given word and get
        the follower in highest count

In essence, the predictor is nothing more than a frequency table of bigrams 
"""