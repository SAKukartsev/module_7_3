import re


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file in self.file_names:
            with open(file, encoding='utf-8') as f:
                words = []
                for line in f:
                    words += (re.sub('[,.=!?;:-]', ' ', line.lower()).split())
                all_words[file] = words
        return all_words

    def find(self, word):
        for item in self.get_all_words().items():
            i = 1
            for item_word in item[1]:
                if str(word).lower() == item_word:
                    return {item[0]: i}
                i += 1
        return f"No word"

    def count(self, word):
        dict_word = {}
        for item in self.get_all_words().items():
            i = 0
            for item_word in item[1]:
                if str(word).lower() == item_word:
                    i += 1
            dict_word[item[0]] = i
        return dict_word


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

# finder = WordsFinder('products.txt', 'test.txt')
# print(finder.get_all_words())
# print(finder.find('tell'))
# print(finder.find('SPaghetti'))
# print(finder.count('tell'))
# print(finder.count('SPagheti'))
