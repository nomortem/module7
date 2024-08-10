import string


class WordsFinder:
    def __init__(self, *file_names):
        # Запоминаем имена файлов в атрибуте file_names
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        # Перебираем все файлы
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    # Считываем файл, переводим в нижний регистр и убираем пунктуацию
                    text = file.read().lower()
                    for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        text = text.replace(punct, '')
                    # Разбиваем текст на слова
                    words = text.split()
                    # Добавляем в словарь
                    all_words[file_name] = words
            except FileNotFoundError:
                all_words[file_name] = []

        return all_words

    def find(self, word):
        # Получаем все слова из файлов
        all_words = self.get_all_words()
        word = word.lower()
        result = {}
        # Ищем слово в каждом файле
        for name, words in all_words.items():
            if word in words:
                result[name] = words.index(word) + 1  # Номер позиции начинается с 1
            else:
                result[name] = None  # Если слово не найдено, возвращаем None

        return result

    def count(self, word):
        # Получаем все слова из файлов
        all_words = self.get_all_words()
        word = word.lower()
        result = {}
        # Считаем количество вхождений слова в каждом файле
        for name, words in all_words.items():
            result[name] = words.count(word)

        return result


# Пример выполнения программы:
finder2 = WordsFinder('test_file.txt')

# Получаем все слова
print(finder2.get_all_words())

# Находим слово и его позицию
print(finder2.find('TEXT'))


print(finder2.count('teXT'))

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))