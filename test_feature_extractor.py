# testing if feature_extractor.py works

from feature_extractor import extract_features
from text_cleaner import clean_text

def test_extract_features():
    sample_text = """
    Bonjour! Je m'appelle Élodie. こんにちは。你好！¡Hola! ¿Cómo estás?
    Hello, my name is Gideon.
    """

    print("=== RAW TEXT ===")
    print(sample_text.strip())
    
    cleaned = clean_text(sample_text)
    print("\n=== CLEANED TEXT ===")
    print(cleaned)

    features = extract_features(sample_text)
    
    print("\n=== TOP 10 CHARACTER FREQUENCIES ===")
    for char, freq in sorted(features.items(), key=lambda x: -x[1])[:10]:
        print(f"{char}: {freq:.4f}")

if __name__ == "__main__":
    test_extract_features()
