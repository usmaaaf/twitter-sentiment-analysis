import nltk
from nltk.tokenize import TweetTokenizer

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        self.positives = []
        self.negatives = []

        with open(positives) as lines:
            for line in lines:
               if not line.startswith(";"):
                     self.positives.append(line.rstrip("\n"))

        with open(negatives) as lines:
            for line in lines:
               if not line.startswith(";"):
                    self.negatives.append(line.rstrip("\n"))


    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        value = 0
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)
        for token in tokens:
                if token.lower() in self.positives:
                    value += 1
                elif token.lower() in self.negatives:
                    value -= 1
                else:
                    continue
        return value
