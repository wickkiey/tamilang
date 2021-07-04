import regex
from tamilang.constants import *

def split_text(text):
    return regex.findall(r'\X', text, regex.U)

def conv_base(text):
    return [split_map.get(k) for k in split_text(text)]

def is_valid_char(char):
    if char in char_list:
        return True
    return False

def check_otru(text1,text2):

    #6.1.1 சுட்டு, வினா அடியாகத் தோன்றிய சொற்கள் முன் வல்லினம் மிகல்
    text1_split = [split_map[k] for k in split_text(text1)]
    text2_split = [split_map[k] for k in split_text(text2)]

    if (text1 in suttu_vina_words) and (text2[0][0] in vallina_mei):
        return text1 + text2_split[0][0], text2
    
    