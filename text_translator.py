from deep_translator import GoogleTranslator
to_translate = 'سخته, ولی اخرش قشنگه'
translated = GoogleTranslator(source='fa', target='en').translate(to_translate)
print(translated)
