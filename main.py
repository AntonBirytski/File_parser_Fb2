from xml.dom import minidom
from book import Book
from search_file import search_move_files
from db_input import DB_input


def show_file_name(file_name):
    db = DB_input('Book_db.db')
    xmldoc = minidom.parse(file_name)
    book = Book(xmldoc)

    b_title = book.get_book_name()
    num_p = book.get_prg_num()
    num_w = book.get_words_num()
    num_l = book.get_letters_num()
    num_cap_w = book.get_capital_words()
    num_low_w = book.get_lower_case_words()
    book_id = db.insert_tbooks(b_title,num_p,num_w,num_l,num_cap_w,num_low_w)
    db.create_tstatisticsbookid(book_id)

    words = sorted(book.get_format_text.split(), key=lambda word: word.lower())
    db.insert_tstatisticsbookid(book_id, words)

for file in search_move_files('C:\\Input', 'C:\\Incorrect_input'):
    show_file_name(file)
