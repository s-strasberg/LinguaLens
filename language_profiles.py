from collections import Counter
from FinalDataCollectionCode import clean_text

def build_language_profile(text):
    text = clean_text(text)
    counter = Counter(text)
    total = sum(counter.values())
    return {char: freq / total for char, freq in counter.items() if char.isalpha()}
