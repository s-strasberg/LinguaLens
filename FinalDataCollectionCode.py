import re

def clean_text(text):
# Lowercases all characters, removes punctuation, digits, and non-letter characters, preserves accented Latin characters and CJK (Chinese, Japanese, Korean) characters
    start_idx = text.find("*** START OF")
    end_idx = text.find("*** END OF")
    if start_idx != -1 and end_idx != -1:
        text = text[start_idx:end_idx]

    # Remove all non-letter characters except spaces (including numbers, punctuation, etc.)
    text = re.sub(r'[^A-Za-zÀ-ÿ\s]', '', text)
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with one
    return text.strip().lower()

import requests
import os

def download_text(url, filename, download_dir = 'corpora'):
    # Downloading a .txt file from Project Gurtenberg and saving it

    os.makedirs(download_dir, exist_ok=True)
    # To ensure the folder exists

    response = requests.get(url)
    if response.status_code == 200:
      path = os.path.join(download_dir, filename)
      with open(path, 'w', encoding = 'utf-8') as f:
        f.write(response.text)
      print(f"Downloaded and saved to {path}.")
    else:
      print("Failed to download.")

def load_corpus(filepath):
  # Load raw text from file
  with open(filepath, 'r', encoding = 'utf-8') as f:
    return f.read()

def save_cleaned_text(language, cleaned_text, output_dir = 'clean_corpora'):
  # Save clean text to new file
  os.makedirs(output_dir, exist_ok=True)
  out_path = os.path.join(output_dir, f"{language}.txt")
  with open(out_path, 'w', encoding = 'utf-8') as f:
    f.write(cleaned_text)

def process_all_languages(gutenberg_urls, output_dir = 'corpora'):
  # Download, clean, and save corpora from URLs

  download_dir = 'corpora' # Separate directory

  for lang, url in gutenberg_urls.items():
    filename = f"{lang}.txt"
    download_text(url, filename, output_dir)
    path = os.path.join(download_dir, filename)
    raw_text = load_corpus(path)
    cleaned = clean_text(raw_text)
    save_cleaned_text(lang, cleaned, output_dir)
    print(f"Processed: {lang}")


gutenberg_urls = {
        "english": "https://www.gutenberg.org/cache/epub/1342/pg1342.txt", # Pride and Prejudice
        "french": "https://www.gutenberg.org/cache/epub/17489/pg17489.txt", # Candide
        "german": "https://www.gutenberg.org/cache/epub/2000/pg2000.txt", # Faust
        "spanish": "https://www.gutenberg.org/cache/epub/16172/pg16172.txt", # Don Quixote
        "italian": "https://www.gutenberg.org/cache/epub/1012/pg1012.txt" # Divine Comedy
    }
process_all_languages(gutenberg_urls)
