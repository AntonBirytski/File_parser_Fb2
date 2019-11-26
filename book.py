class Book:
    def __init__(self, xmldoc):
        self.body = xmldoc.getElementsByTagName('body')[0]
        self.prgs = self.body.getElementsByTagName('p')
        self.xmldoc = xmldoc
        self.get_format_text = get_format_text(self.prgs)

    def get_book_name(self):
        book_name = self.xmldoc.getElementsByTagName('book-name')[0].firstChild.nodeValue
        return book_name

    def get_prg_num(self):
        prgNum = len(self.prgs)
        return prgNum

    def get_words_num(self):
        text = self.get_format_text
        wordsNum = len(text.split(' '))
        return wordsNum

    def get_letters_num(self):
        lettersNum = 0
        text = self.get_format_text
        for letter in text:
            if letter != ' ':
                lettersNum += 1
        return lettersNum

    def get_lower_case_words(self):
        return sum(1 for c in self.get_format_text.split(' ') if c.islower())

    def get_capital_words(self):
        return sum(1 for c in self.get_format_text.split(' ') if not c.islower())

def get_format_text(prgs):
    format_text = ''
    for prg in prgs:
        chars = '!@#$%^&*()[]{};:,./<>\\?\"\'…|`~-=_+—«»'
        text = prg.firstChild.nodeValue
        if isinstance(text, str):
            text = text.translate({ord(i): None for i in chars})
            format_text = format_text + ' ' + text
    return format_text
