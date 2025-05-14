from collections import Counter
from FinalDataCollectionCode import clean_text

def extract_letter_frequencies(text):
    """
    Cleans input text and returns a normalized frequency dictionary of characters (excluding spaces).
    
    Args:
        text (str): Raw input text
    
    Returns:
        dict: {character: normalized frequency}
    """
    cleaned = clean_text(text)
    characters_only = cleaned.replace(" ", "")
    counts = Counter(characters_only)
    total = sum(counts.values())
    
    if total == 0:
        return {}
    
    return {char: count / total for char, count in counts.items()}

def extract_features(text):
    """
    Wrapper function that runs full feature extraction on raw input text.
    
    Args:
        text (str): Raw input text
    
    Returns:
        dict: Feature dictionary (letter frequencies)
    """
    return extract_letter_frequencies(text)

# Optional standalone test
if __name__ == "__main__":
    sample = "Bonjour! Je m'appelle Élodie. こんにちは。你好！"
    features = extract_features(sample)
    for char, freq in sorted(features.items(), key=lambda x: -x[1])[:10]:
        print(f"{char}: {freq:.4f}")
