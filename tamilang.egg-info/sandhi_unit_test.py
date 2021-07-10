import regex

def split_text(text):
    return regex.findall(r'\X', text, regex.U)

# Example to check the Sandhi Rules
def split_test_data(text):
    result = {}
    lines = text.split('\n')
    for line in lines:
        if line !='':
            split1 = line.split(' = ')
            result[tuple(split1[0].split(' + '))] = split1[0]
    
    return result



# 6.1.1 சுட்டு, வினா அடியாகத் தோன்றிய சொற்கள் முன் வல்லினம் மிகல்
examples_611 = """
அ + காலம் = அக்காலம்
எ + திசை = எத்திசை
அந்த + பையன் = அந்தப் பையன்
எந்த + பொருள் = எந்தப் பொருள்
அங்கு + கண்டான் = அங்குக் கண்டான்
எங்கு + போனான் = எங்குப் போனான்
யாங்கு + சென்றான் = யாங்குச் சென்றான்
அப்படி + சொல் = அப்படிச் சொல்
எப்படி + சொல்வான் = எப்படிச் சொல்வான்
ஈண்டு + காண்போம் = ஈண்டுக் காண்போம்
யாண்டு + காண்பேன் = யாண்டுக் காண்பேன்
அவ்வகை + செய்யுள் = அவ்வகைச் செய்யுள்
எத்துணை + பெரியது = எத்துணைப் பெரியது
"""

# 6.1.2 ஓர் எழுத்துச் சொற்களின் முன் வல்லினம் மிகல்
example_612 = """
கை + குழந்தை = கைக்குழந்தை
கை + பிடி = கைப்பிடி
தீ + பிடித்தது = தீப்பிடித்தது
தீ + பெட்டி = தீப்பெட்டி
தீ + புண் = தீப்புண்
தை + பொங்கல் = தைப்பொங்கல்
தை + திருநாள் = தைத்திருநாள்
பூ + பறித்தாள் = பூப்பறித்தாள்
பூ + பல்லக்கு = பூப்பல்லக்கு
மை + கூடு = மைக்கூடு
மை + பேனா = மைப்பேனா
"""