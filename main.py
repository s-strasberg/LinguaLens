import sys
from predict_language import predict_language
from detector import detect_language as heuristic_guess

def get_user_input():
    """
    Prompt the user to choose input method and return the raw text.
    """
    choice = input("Would you like to (1) paste text or (2) load a text file? Enter 1 or 2: ").strip()
    
    if choice == "1":
        print("\nPaste your text below (press Enter when done):")
        return input("> ")

    elif choice == "2":
        filepath = input("Enter the path to your .txt file (e.g., corpora/english.txt): ").strip()
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print("⚠️  File not found. Please try again.")
            sys.exit(1)
    else:
        print("⚠️  Invalid input. Please enter 1 or 2.")
        sys.exit(1)

def display_results(language, confidence, top_matches, fallback):
    """
    Print language prediction results in a readable format.
    """
    print("\n🧠 Predicted Language:", language)
    print(f"📊 Confidence Score: {confidence:.4f}")
    print("\n🔎 Top Matches:")
    for lang, score in top_matches:
        print(f"- {lang}: {score:.4f}")
    
    if fallback and language != fallback:
        print(f"\n💡 Heuristic Guess (fallback): {fallback}")

def main():
    print("Welcome to LinguaLens 🌍")
    user_text = get_user_input()

    predicted_lang, confidence, top_matches = predict_language(user_text)
    fallback_guess = heuristic_guess(user_text)
    
    display_results(predicted_lang, confidence, top_matches, fallback_guess)

if __name__ == "__main__":
    main()
