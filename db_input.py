import sqlite3
import itertools

class DB_input:
    def __init__(self,DBname):
        self._DBname = DBname
        self.connection = sqlite3.connect(self._DBname)
        self.create_tbooks()

    def get_cursor(self):
        return self.connection.cursor()

    def commit(self):
        self.connection.commit()

    def create_tbooks(self):
        query = self.get_cursor()
        query.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='tBooks' ''')
        if not query.fetchone()[0] == 1: {
            query.execute('''CREATE TABLE tBooks
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            Book_name TEXT NOT NULL,
                            Num_of_paragraph INTEGER,
                            Num_of_words INTEGER,
                            Num_of_letters INTEGER,
                            Num_capital_words INTEGER,
                            Num_lowercase_words INTEGER);''')}

    def insert_tbooks(self,b_title,num_p,num_w,num_l,num_cap_w,num_low_w):
        query = self.get_cursor()
        query.execute('''INSERT INTO tBooks (Book_name,Num_of_paragraph, Num_of_words,
            Num_of_letters, Num_capital_words, Num_lowercase_words)
            VALUES (:title, :num_prg, :num_wrd, :num_ltt, :num_cap_w, :num_low_w)''',
                  {
                      "title": b_title,
                      "num_prg": num_p,
                      "num_wrd": num_w,
                      "num_ltt": num_l,
                      "num_cap_w": num_cap_w,
                      "num_low_w": num_low_w })
        self.commit()
        return str(query.lastrowid)

    def create_tstatisticsbookid(self,book_id):
        query =  self.get_cursor()
        query.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name= "tStatisticsBookId_''' + str(book_id) + '''"''')
        if not query.fetchone()[0] == 1: {
            query.execute('''CREATE TABLE tStatisticsBookId_''' + str(book_id) +
                          '''(All_words TEXT, Words_cnt INTEGER, Uppercase_cnt INTEGER)''')}

    def insert_tstatisticsbookid(self,book_id,words):
        query = self.get_cursor()
        for k, g in itertools.groupby(words, key=lambda word: word.lower()):
            l = list(g)
            length = len(l)
            upper = sum(1 for word in l if not word.islower())
            query.execute("INSERT INTO tStatisticsBookId_" + str(book_id) + " (All_words, Words_cnt, Uppercase_cnt) "
                      "VALUES(:words,:count,:uppercase)",
                          {"words": k,
                           "count": length,
                           "uppercase": upper })
        self.commit()
