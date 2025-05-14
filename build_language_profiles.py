import os
import json
from feature_extractor import extract_features

def build_profile(text):
    return extract_features(text)

def save_profile(profile, language, output_dir='profiles'):
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, f"{language}.json")
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(profile, f, ensure_ascii=False, indent=2)

def build_all_profiles(corpus_dir='clean_corpora'):
    for file in os.listdir(corpus_dir):
        if file.endswith('.txt'):
            lang = file.replace('.txt', '')
            with open(os.path.join(corpus_dir, file), 'r', encoding='utf-8') as f:
                text = f.read()
            profile = build_profile(text)
            save_profile(profile, lang)
            print(f"[✓] Profile saved for {lang}")

if __name__ == "__main__":
    build_all_profiles()
