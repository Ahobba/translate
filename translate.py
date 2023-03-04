from googletrans import Translator
from pyperclip import copy

def translate(text, dest='en'):
    translator = Translator()
    translation = translator.translate(text, dest)
    return translation.text

while True:

    original_text = input('\n> ')
    translated_text = translate(original_text, 'pt')
    back_translated_text = translate(translated_text, 'en')

    if original_text == translated_text:
        copy(back_translated_text)
        print(back_translated_text)

    else:
        print(translated_text)
