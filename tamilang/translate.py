from tamil import utf8
from charmaps import tamil_to_eng

def tamil_2_eng_phonetic(text):
    chars = utf8.get_letters(text)
    result = [tamil_to_eng.get(char,char) for char in chars]
    return ''.join(result)