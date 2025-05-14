# LinguaLens

**CS Final Project**  
**Due: May 14, 2025**

---

## Overview  
**LinguaLens** is a Python-based tool that automatically detects the language of a given text input. Users can either paste a text string or upload a `.txt` file, and the program will analyze the input using statistical character frequency profiling to determine the most likely language. The tool supports five Latin-script languages and outputs a best guess, a confidence score, and a fallback heuristic guess.

All setup (data collection, preprocessing, and profile generation) runs automatically when executing `main.py`.

---

## Team Members  
- **Liliana Cunha**  
- **Sawyer Strasberg**  
- **Gideon Buddenhagen**

---

## Supported Languages  
LinguaLens supports detection for five **Latin-script languages**:
- English
- Spanish
- French
- German
- Italian

Detection is based on:
- Normalized character frequency comparison using cosine similarity
- A simple keyword-based fallback detector for verification

---

## Project Structure  

| File Name                   | Purpose                                                                 | Owner               |
|-----------------------------|-------------------------------------------------------------------------|---------------------|
| `FinalDataCollectionCode.py`| Downloads and cleans training corpora from Project Gutenberg             | **Liliana**         |
| `feature_extractor.py`      | Extracts text features from user input (letter frequencies)              | **Gideon**          |
| `predict_language.py`       | Compares input to language profiles and returns best guess + confidence | **Gideon**          |
| `build_language_profiles.py`| Builds `.json` profiles for each language from cleaned corpora           | **Gideon**          |
| `detector.py`               | Uses keyword heuristics to generate a fallback guess                     | **Sawyer**          |
| `main.py`                   | CLI entry point; integrates all modules and manages full pipeline        | **All**             |
| `README.md`                 | Project documentation and usage guide                                   | **All**             |

---

## Division of Labor

### Liliana Cunha
- Collect sample corpora and manage training dataset creation (`FinalDataCollectionCode.py`)
- Implement input cleaning and preprocessing pipeline
- Support `main.py` integration and documentation

### Sawyer Strasberg
- Design and implement fallback keyword-based language detector (`detector.py`)
- Assist with profile verification and edge case handling

### Gideon Buddenhagen
- Develop feature extraction and similarity scoring logic (`feature_extractor.py`, `predict_language.py`)
- Build profile generation tools (`build_language_profiles.py`)
- Lead integration testing and CLI development (`main.py`)

> All members contributed to final documentation, debugging, and polish.

---

## Timeline

| Date        | Task                                                             |
|-------------|------------------------------------------------------------------|
| May 5–6     | Finalize language list; gather corpora; set up GitHub branches   |
| May 7–8     | Build training profiles; write input cleaner; develop fallback   |
| May 9–10    | Implement feature extraction; draft prediction function          |
| May 11      | Test integration; run sample inputs through full pipeline        |
| May 12–13   | Polish outputs, finalize confidence scoring, debug edge cases    |
| May 14      | Final documentation and submission                               |

---

## Deliverables

- Fully functioning Python program (`main.py`) for text-based language detection
- Automatically generated profiles from real corpora
- Sample inputs and test cases with expected outputs
- Clear documentation and usage instructions

---


## Collaboration Workflow

- Work occurs on individual feature branches:
  - `liliana-data-preprocessing`
  - `sawyer-unicode-profiles`
  - `gideon-features-prediction`

- Merges happen through pull requests to the shared `main` branch  
- Group sync meetings every 2–3 days or as needed  
- All major components tested before merge



