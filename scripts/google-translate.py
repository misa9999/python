# 
# TRANSLATE
from googletrans import Translator

trans = Translator()
#word = input('Word:')
t = trans.translate('bom dizzza para voce', src='pt', dest='en')
print(f'Source: {t.src}')
print(f'Destination: {t.dest}')
print(f'{t.origin} -> {t.text}')

# LIST SUPPORTED LANGUAGES
#from googletrans import LANGUAGES

#for lang in LANGUAGES:
    #print(f'{lang} - {LANGUAGES[lang]}')

# LIST POSSIBLE MISTAKES AND TRANSLATIONS
pm = t.extra_data['possible-mistakes']
pt = t.extra_data['possible-translations']

print(f'Possible Mistakes: {pm}')
print(f'Possible Translations: {pt}')
