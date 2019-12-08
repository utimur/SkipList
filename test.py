from skiplist.SkipList import SkipList
from dictionaryWord import DictionaryWord


# Меню программы
def menu():
    print("Главное меню программы")
    print("Введите команду 0-3")
    print("1. Показать все слова в словаре")
    print("2. Добавить новое слово")
    print("3. Найти слово")
    print("4. Показать меню")
    print("0. Завершить работу программы")


# Заполнение скип листа начальными данными
def inputDictionary(dictionary):
    # Массив со словами
    arr = [DictionaryWord('car', 'машина'),DictionaryWord('phone', 'телефон'),DictionaryWord('window', 'окно'),
           DictionaryWord('door', 'дверь'),DictionaryWord('blanket', 'одеяло'),DictionaryWord('move', 'двигаться'),
           DictionaryWord('water', 'вода'),DictionaryWord('floor', 'этаж'), DictionaryWord('bad', 'плохо'),
           DictionaryWord('good', 'хорошо'),DictionaryWord('try', 'попытка'), DictionaryWord('orange', 'апельсин'),
           DictionaryWord('apple', 'яблоко'), DictionaryWord('banan', 'банан'), DictionaryWord('bird', 'птица'),
           DictionaryWord('dog', 'собака'), DictionaryWord('cat', 'кот'),  DictionaryWord('leaves', 'листья'),
           DictionaryWord('tree', 'дерево'),DictionaryWord('road', 'дорога') ]
    # Добавление слов в скип лист
    for word in arr:
        dictionary.insert(word)


# Функция добавления слова в словарь
def addNewWord(dictionary):
    word = input("Введите слово: ")
    definition = input("Введите определение: ")
    dictWord = DictionaryWord(word, definition)
    dictionary.insert(dictWord)


# Функция поиска слова в словаре
def findWord(dictionary):
    word = input("Введите слово: ")
    print(dictionaryList.find(word))


# Инициализация скип листа
dictionaryList = SkipList()

# Переменная отвечающая за команду в меню
flag = -1

if __name__ == '__main__':
    # Заполнение словаря начальными данными
    inputDictionary(dictionaryList)
    menu()
    while flag != 0:
        try:  # Обработка введенной команды
            flag = int(input("Введите команду: "))
        except ValueError as error:
            print("Некорректная команда")
        if flag == 1:  # Вывод всех слов в словаре
            print("----------------")
            dictionaryList.printAll()
            print("----------------")
        if flag == 2:  # Добавить новое слово в словарь
            addNewWord(dictionaryList)
        if flag == 3:  # Найти слово в словаре
            findWord(dictionaryList)
        if flag == 4:  # Повторный вывод меню
            menu()
        if flag == 0:  # Завершить работу программы
            print("Работы программы завершена.")
            break
