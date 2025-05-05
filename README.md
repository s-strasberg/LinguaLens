# LinguaLens

**CS Final Project**  
**Due: May 14, 2025**

---

## Overview  
**LinguaLens** is a Python-based tool that automatically detects the language of a given text input. Users can either paste a text string or upload a `.txt` file, and the program will analyze the input using a combination of Unicode script detection and statistical language profiling to determine the most likely language. The tool is designed to work across multiple languages, including both Latin-script and non-Latin-script languages, and will provide a confidence score along with a brief explanation of the features that contributed to the prediction.

---

## Team Members  
- **Liliana Cunha**  
- **Sawyer Strasberg**  
- **Gideon Buddenhagen**

---

## Confirmed Languages  
LinguaLens will support detection for at least **seven languages**:  
- **Latin-script:** English, Spanish, French, German, Italian  
- **Non-Latin-script:** Japanese, Mandarin Chinese  

This allows us to implement two distinct detection strategies:
1. **Unicode-based script detection** for languages with unique character sets (Japanese, Mandarin).
2. **Feature-based frequency comparison** for Latin-alphabet languages using letter frequencies, digraphs/trigraphs, and common word presence.

---

## Project Structure  

| File Name              | Purpose                                                                 | Owner               |
|------------------------|-------------------------------------------------------------------------|---------------------|
| `data_collector.py`    | Gathers training corpora from Project Gutenberg or other sources        | **Liliana**         |
| `text_cleaner.py`      | Preprocesses and tokenizes user input (lowercase, punctuation removal)  | **Liliana**         |
| `unicode_detector.py`  | Identifies language family using Unicode script ranges                  | **Sawyer**          |
| `language_profiles.py` | Builds reference profiles for each language using frequency analysis     | **Sawyer**          |
| `feature_extractor.py` | Extracts text features from input (letter/digraph frequencies)          | **Gideon**          |
| `predict_language.py`  | Compares input to language profiles and returns best guess + confidence | **Gideon**          |
| `main.py`              | Manages CLI interaction and integrates all modules                      | **All**             |
| `README.md`            | Project documentation and usage guide                                   | **All**             |

---

## Division of Labor

### Liliana Cunha
- Collect sample corpora and manage training dataset creation (`data_collector.py`)
- Implement input cleaning and preprocessing pipeline (`text_cleaner.py`)
- Support `main.py` integration and documentation

### Sawyer Strasberg
- Design and implement Unicode-based script detection (`unicode_detector.py`)
- Generate reference language profiles from training corpora (`language_profiles.py`)
- Assist with sample validation and mixed-language handling

### Gideon Buddenhagen
- Develop feature extraction and similarity scoring logic (`feature_extractor.py`, `predict_language.py`)
- Lead integration testing and CLI output formatting (`main.py`)
- Coordinate optional batch analysis (stretch goal)

> All members will contribute to final documentation, code testing, and feature refinement.

---

## Timeline

| Date        | Task                                                             |
|-------------|------------------------------------------------------------------|
| May 5–6     | Finalize language list; gather corpora; set up GitHub branches   |
| May 7–8     | Build training profiles; write input cleaner; Unicode detector   |
| May 9–10    | Implement feature extraction; draft prediction function          |
| May 11      | Test integration; run sample inputs through full pipeline        |
| May 12–13   | Polish outputs, finalize confidence score logic, debug edge cases|
| May 14      | Final documentation and submission                               |

---

## Deliverables

- Fully functioning Python program (`main.py`) for text-based language detection
- Supporting scripts for data processing, feature analysis, and prediction
- Sample inputs and test cases with expected outputs
- *(Optional)* Batch analysis output showing language trends in literature
- Clear, concise documentation and instructions for running the program

---

## Collaboration Workflow

- Work occurs on individual feature branches:
  - `liliana-data-preprocessing`
  - `sawyer-unicode-profiles`
  - `gideon-features-prediction`

- Merges happen through pull requests to the shared `main` branch  
- Group sync meetings every 2–3 days or as needed  
- All major components tested before merge
