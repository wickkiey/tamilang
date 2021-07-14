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

def join_space(text1,text2):
    return text1 +  ' ' + text2

def _firstmap(text):
    return text[0][0]

def _lasttext(text):
    return text[-1]

def merge1(text1,mid,text2):
    return text1 + mid + text2

def merge2(text1,mid,text2):
    return text1 + mid +' ' +text2
  

def fix_otru(text1,text2):
    text1_list = split_text(text1)
    text2_list = split_text(text2)

    text1_map = [split_map[k] for k in text1_list]
    text2_map = [split_map[k] for k in text2_list]

    if (_firstmap(text2_map) in vall_migu):
        # 6.1.1 சுட்டு, வினா அடியாகத் தோன்றிய சொற்கள் முன் வல்லினம் மிகல்
        # அங்கு + கண்டான் = அங்குக் கண்டான்

        if (text1 in suttu_vina_words):
            if len(text1_list)==1:
                return merge1(text1,_firstmap(text2_map),text2)
            return merge2(text1,_firstmap(text2_map),text2)

        # 6.1.2 ஓர் எழுத்துச் சொற்களின் முன் வல்லினம் மிகல்
        # கை + குழந்தை = கைக்குழந்தை

        if (len(text1_list)==1):
            return merge1(text1,_firstmap(text2_map),text2)

        # 6.1.3 குற்றியலுகரச் சொற்கள் முன் வல்லினம் மிகல்
        # வன்தொடர்க் குற்றியலுகரம் முன் வல்லினம் மிகல் or சில மென்தொடர்க் குற்றியலுகரம் முன் வல்லினம் மிகல்
        if text1.endswith(van_kutriyalugaram) or  text1.endswith(men_kutriyalugaram):
            return merge2(text1,_firstmap(text2_map),text2)


        # சில உயிர்த்தொடர்க் குற்றியலுகரம் முன் வல்லினம் மிகல்
        if text1.endswith(kutriya_lugaram) and text1_map[-2][1] in uyir_chars:
            return merge2(text1,_firstmap(text2_map),text2)
        

        # 6.1.4 முற்றியலுகரச் சொற்கள் முன் வல்லினம் மிகல்
        

    return False

def check_otru(text1,text2):
    # http://www.tamilvu.org/courses/degree/c021/c0214/html/c0214661.htm
    
    text1_split = split_text(text1)
    text2_split = split_text(text2)

    text1_map = [split_map[k] for k in split_text(text1)]
    text2_map = [split_map[k] for k in split_text(text2)]

    # 6.1.1 சுட்டு, வினா அடியாகத் தோன்றிய சொற்கள் முன் வல்லினம் மிகல்
    # அங்கு + கண்டான் = அங்குக் கண்டான்
    if (text1 in suttu_vina_words) and (text2_map[0][0] in vall_migu):
        if len(text1_split) ==1 :
            return text1 + text2_map[0][0]+ text2
        return text1 + text2_map[0][0] + ' ' + text2

    # 6.1.2 ஓர் எழுத்துச் சொற்களின் முன் வல்லினம் மிகல்
    # கை + குழந்தை = கைக்குழந்தை
    if (len(text1_split)==1) and (text2_map[0][0] in vall_migu):
        return text1 + text2_map[0][0], text2

    # 6.1.3 குற்றியலுகரச் சொற்கள் முன் வல்லினம் மிகல்
    # வன்தொடர்க் குற்றியலுகரம் முன் வல்லினம் மிகல்
    if text1.endswith(van_kutriyalugaram) and (text2_map[0][0] in vall_migu):




    
    
    