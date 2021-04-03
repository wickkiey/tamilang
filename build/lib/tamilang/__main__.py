from tamilang.charmaps import tamil_to_eng

import sys 
from importlib import resources

from tamilang.translate import tamil_2_eng_phonetic

def main():
    if len(sys.argv) > 1:
        text = ' '.join(sys.argv[1:])
        phonetic_result = tamil_2_eng_phonetic(text)
        print("English Sentence :",text)
        print("Phonetic Tamil version :",phonetic_result)
    # If no ID is given, show a list of all articles
    else:
        print("Usage ... ")
        print("python -m tamilang வணக்கம் ! வாழ்க வளமுடன் !")
        

if __name__ == "__main__":
    main()