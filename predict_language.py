import os
import json
from scipy.spatial.distance import cosine
from feature_extractor import extract_features

def load_language_profiles(profile_dir='profiles'):
    """
    Loads all saved language profiles from JSON files in the given directory.

    Returns:
        dict: {language: {char: frequency, ...}}
    """
    profiles = {}
    for filename in os.listdir(profile_dir):
        if filename.endswith('.json'):
            lang = filename.replace('.json', '')
            with open(os.path.join(profile_dir, filename), 'r', encoding='utf-8') as f:
                profiles[lang] = json.load(f)
    return profiles

def vectorize(profile, vocab):
    """
    Converts a frequency dictionary into a vector using the full vocab.

    Args:
        profile (dict): character frequencies
        vocab (set): union of all characters

    Returns:
        list: frequency vector aligned with vocab
    """
    return [profile.get(char, 0) for char in vocab]

def predict_language(user_text, profile_dir='profiles'):
    """
    Predicts the language of the input text based on profile comparison.

    Args:
        user_text (str): raw user input

    Returns:
        tuple: (best_language, confidence_score, top_matches)
    """
    user_features = extract_features(user_text)
    language_profiles = load_language_profiles(profile_dir)
    
    vocab = set(user_features)
    for lang_profile in language_profiles.values():
        vocab |= set(lang_profile.keys())

    user_vec = vectorize(user_features, vocab)

    scores = {}
    for lang, profile in language_profiles.items():
        lang_vec = vectorize(profile, vocab)
        try:
            sim = 1 - cosine(user_vec, lang_vec)
        except ZeroDivisionError:
            sim = 0
        scores[lang] = sim

    # Sort languages by score
    sorted_scores = sorted(scores.items(), key=lambda x: -x[1])
    best_lang, best_score = sorted_scores[0]
    top_matches = sorted_scores[:3]

    return best_lang, best_score, top_matches

# Optional test
if __name__ == "__main__":
    text = "Bonjour, je m'appelle Élodie. Comment allez-vous aujourd'hui?"
    lang, confidence, top = predict_language(text)
    print(f"\n Predicted Language: {lang}")
    print(f" Confidence Score: {confidence:.4f}")
    print("\n Top Matches:")
    for lang, score in top:
        print(f"- {lang}: {score:.4f}")
