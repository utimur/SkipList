class DictionaryWord:
    # Конструктор
    def __init__(self, word='', definition=''):
        self.word = word  # Слово
        self.definition = definition  # Определение

    def __repr__(self):
        return "{}: {}".format(self.word,self.definition)
