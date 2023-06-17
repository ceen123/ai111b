# pip install googletrans==4.0.0-rc1



from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    return translated.text

def main():
    print("Automatic Translator")
    print("--------------------")
    print("Supported languages:")
    print("1. English")
    print("2. Spanish")
    print("3. French")
    print("4. German")
    print("5. Italian")
    print("6. Portuguese")
    print("7. Russian")
    print("8. Chinese (Simplified)")
    print("9. Japanese")
    print("10. Korean")
    print("--------------------")

    text = input("Enter the text to translate: ")
    target_language = input("Enter the target language number (e.g., 1 for English): ")
    
    language_codes = {
        1: 'en',
        2: 'es',
        3: 'fr',
        4: 'de',
        5: 'it',
        6: 'pt',
        7: 'ru',
        8: 'zh-cn',
        9: 'ja',
        10: 'ko'
    }

    if target_language.isdigit() and int(target_language) in language_codes:
        target_language = language_codes[int(target_language)]
        translated_text = translate_text(text, target_language)
        print("Translated text:")
        print(translated_text)
    else:
        print("Invalid target language number.")

if __name__ == '__main__':
    main()
