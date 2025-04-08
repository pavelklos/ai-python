# 190 : Exercise: Translator
# TODO: googletrans: online translation service
# - https://pypi.org/project/googletrans/
# from googletrans import Translator
# TODO: translate: offline translation service
# - https://pypi.org/project/translate/
# from translate import Translator
# TODO: use translate module to translate the text
# - https://pypi.org/project/translate/
# - install translate module:
#   > pip install translate
# - add package in PyCharm:
#   File > Settings > Project > Python Interpreter > '+' > translate

from translate import Translator


def translate_text(text):
    # cz: Czech, es: Spanish, zh-CN: Chinese, ja: Japanese, ko: Korean
    languages = ["cs", "es", "ZH-CN", "ja", "ko"]
    for lang in languages:
        # translate text to specific language and print the result
        print(f"translating to {lang}...")
        translator = Translator(to_lang=lang)
        translation = translator.translate(text)
        print(translation)
        print()
        # save translation for specific language to a file
        with open(f"translation_{lang}.txt", mode="w", encoding="utf-8") as my_file:
            my_file.write(translation)


try:
    with open("translate.txt", mode="r") as my_file:
        original_text = my_file.read()
        translate_text(original_text)
except Exception as e:
    print(type(e))  # <class 'FileNotFoundError'>
    print(e)  # [Errno 2] No such file or directory: 'translate.txt'
