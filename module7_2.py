def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        for i, string in enumerate(strings, 1):
            # Получаем текущую позицию курсора (начало строки в байтах)
            position = file.tell()
            # Записываем строку в файл
            file.write(string + '\n')
            # Запоминаем позицию строки
            strings_positions[(i, position)] = string

    return strings_positions


# Пример работы программы
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)