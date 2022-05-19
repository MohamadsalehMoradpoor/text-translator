from deep_translator import GoogleTranslator
to_translate = 'باعث افتخار من است که در خدمت شما هستم'
translated = GoogleTranslator(source='fa', target='en').translate(to_translate)
print(translated)