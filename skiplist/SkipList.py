from dictionaryWord import DictionaryWord


class SkipNode:
    def __init__(self, height=0, elem=None):
        self.elem = elem
        self.next = [None] * height


class SkipList:
    # Конструктор
    def __init__(self):
        self.head = SkipNode()

    # Вспомогательная функция обновляющая лист
    def updateList(self, elem):
        update = [None] * len(self.head.next)
        x = self.head

        if str(type(elem)) == "<class 'str'>":
            elem = DictionaryWord(elem)
        for i in reversed(range(len(self.head.next))):
            while x.next[i] is not None and x.next[i].elem.word < elem.word:
                x = x.next[i]
            update[i] = x

        return update

    # Метод поиска слова в скип листе
    def find(self, elem, update=None):
        if str(type(elem)) == "<class 'str'>":
            elem = DictionaryWord(elem)
        if update is None:
            update = self.updateList(elem)
        if len(update) > 0:
            candidate = update[0].next[0]
            if candidate is not None and candidate.elem.word == elem.word:
                return candidate.elem
        return None

    # Метод вставки слова в скип лист
    def insert(self, elem):
        node = SkipNode(3, elem)

        while len(self.head.next) < len(node.next):
            self.head.next.append(None)

        update = self.updateList(elem)
        if self.find(elem, update) == None:
            for i in range(len(node.next)):
                node.next[i] = update[i].next[i]
                update[i].next[i] = node

    # Метод вывода всех слов в спип листе
    def printAll(self):
        x = self.head
        for i in reversed(range(len(self.head.next))):
            while x.next[i] is not None:
                x = x.next[i]
                print(x.elem)
