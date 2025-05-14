def detect_script(text):
    for char in text:
        code = ord(char)
        if 0x4E00 <= code <= 0x9FFF:
            return "Mandarin"
        elif 0x3040 <= code <= 0x309F or 0x30A0 <= code <= 0x30FF:
            return "Japanese"
    return "Latin"
def detect_language(text):
    script = detect_script(text)
    if script in ["Mandarin", "Japanese"]:
        return script

    #Lowercase the text for case-insensitivity? solve that issue 
    text = text.lower()
    
    #Heuristics for Latin languages!
    if "the" in text or "and" in text:
        return "English"
    elif "el" in text or "ñ" in text:
        return "Spanish"
    elif "le" in text or "é" in text:
        return "French"
    elif "der" in text or "ß" in text:
        return "German"
    elif "che" in text or "è" in text:
        return "Italian"
    
    return "Unknown"
