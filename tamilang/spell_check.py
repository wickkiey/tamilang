from tamilang.constants import *
import regex

_d = True

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

def _lastmap(text):
    if len(text[-1])>1:
        return text[-1][-1]
    return text[-1][0]

def _lasttext(text):
    return text[-1]

def merge1(text1,mid,text2):
    return text1 + mid + text2

def merge2(text1,mid,text2):
    return text1 + mid +' ' +text2
  

def fix_otru(text1,text2):
    # http://www.tamilvu.org/courses/degree/c021/c0214/html/c0214661.htm
    text1_list = split_text(text1)
    text2_list = split_text(text2)

    text1_map = [split_map[k] for k in text1_list]
    text2_map = [split_map[k] for k in text2_list]

    if (_firstmap(text2_map) in vall_migu):
        # 6.1.1 சுட்டு, வினா அடியாகத் தோன்றிய சொற்கள் முன் வல்லினம் மிகல்
        # அங்கு + கண்டான் = அங்குக் கண்டான்

        if (text1 in suttu_vina_words):
            if _d: print("6.1.1")
            if len(text1_list)==1:
                return merge1(text1,_firstmap(text2_map),text2)
            return merge2(text1,_firstmap(text2_map),text2)

        # 6.1.2 ஓர் எழுத்துச் சொற்களின் முன் வல்லினம் மிகல்
        # கை + குழந்தை = கைக்குழந்தை

        if (len(text1_list)==1):
            if _d: print("6.1.2")
            return merge1(text1,_firstmap(text2_map),text2)

        # 6.1.3 குற்றியலுகரச் சொற்கள் முன் வல்லினம் மிகல்
        # வன்தொடர்க் குற்றியலுகரம் முன் வல்லினம் மிகல் or சில மென்தொடர்க் குற்றியலுகரம் முன் வல்லினம் மிகல்
        if text1.endswith(van_kutriyalugaram) or  text1.endswith(men_kutriyalugaram):
            if _d: print("6.1.3")
            return merge2(text1,_firstmap(text2_map),text2)


        # சில உயிர்த்தொடர்க் குற்றியலுகரம் முன் வல்லினம் மிகல்
        if len(text1_list)>2 and text1.endswith(kutriya_lugaram) and text1_map[-2][1] in uyir_chars:
            if _d: print("6.1.3.2")
            return merge2(text1,_firstmap(text2_map),text2)
        

        # 6.1.4 முற்றியலுகரச் சொற்கள் முன் வல்லினம் மிகல்
        if len(text1_list)>=2:
            if (text1_map[-2][-1] in kuril) and (text1_map[-1][-1] =='உ'):
                if _d: print("6.1.4.1")
                return merge2(text1,_firstmap(text2_map),text2)

        if text1_list[-1] == "வு":
            if _d: print("6.1.4.2")
            return merge2(text1,_firstmap(text2_map),text2)

        # 6.1.5 வேற்றுமைப் புணர்ச்சியில் வரும் வல்லினம் மிகல்
        # 6.1.5.1 Need to collect noun words in tamil 
        # 6.1.5.2 

        # 6.1.5.3 வேற்றுமை உருபு விரிந்து வருவது
        # 6.1.5.3.1 இரண்டாம் வேற்றுமை விரியின் (ஐ உருபின்) முன் வரும் வல்லினம் மிகும்.
        
        if _lastmap(text1_map) =="ஐ":
            return merge2(text1,_firstmap(text2_map),text2)

        # 6.1.5.3.2 நான்காம் வேற்றுமை விரியின் (கு உருபின்) முன்வரும் வல்லினம் மிகும்.

        if _lastmap(text1_map) =="கு":
            return merge2(text1,_firstmap(text2_map),text2)

        # 6.1.5.3.3 நான்காம் வேற்றுமைத் தொகையில் நிலைமொழி அஃறிணையாயின் அதன்முன் வரும் வல்லினம் மிகும்.
        # Collect agrinai words. Hope noun is also agrinai

        # 6.1.5.3.4 இரண்டாம் வேற்றுமை உருபும் பயனும் உடன்தொக்க தொகையில் வரும் வல்லினம் மிகும்.
        # 6.1.5.3.5 மூன்றாம் வேற்றுமை உருபும் பயனும் உடன்தொக்க தொகையில் வரும் வல்லினம் மிகும்
        # 6.1.5.3.6 நான்காம் வேற்றுமை உருபும் பயனும் உடன்தொக்க தொகையில் வரும் வல்லினம் பெரும்பாலும் மிகும்.
        # 6.1.5.3.7 ஐந்தாம் வேற்றுமை உருபும் பயனும் உடன்தொக்க தொகையில் வரும் வல்லினம் மிகும்.
        # 6.1.5.3.8 ஏழாம் வேற்றுமை உருபும் பயனும் உடன்தொக்க தொகையில் வரும் வல்லினம் மிகும்.



    return False



    
    
    