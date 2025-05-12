def detect_script(text):
    for char in text:
        code = ord(char)
        if 0x4E00 <= code <= 0x9FFF:
            return "Mandarin"
        elif 0x3040 <= code <= 0x309F or 0x30A0 <= code <= 0x30FF:
            return "Japanese"
    return "Latin"
