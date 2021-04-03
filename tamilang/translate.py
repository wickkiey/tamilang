from tamil import utf8
from tamilang.charmaps import tamil_to_eng

def tamil_2_eng_phonetic(text):
    chars = utf8.get_letters(text)
    result = [tamil_to_eng.get(char,char) for char in chars]
    return ''.join(result)

def tamil_2_eng_file(file_name):
    with open(file_name,'r',encoding='utf-8') as f:
        text = f.read()
    
    return tamil_2_eng_phonetic(text)

