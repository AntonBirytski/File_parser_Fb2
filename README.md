# File_parser_Fb2 
HT_1 

1)Monitor folder 'input' for files for .fb2 files (if other file exist - move it to 'incorrect_input' folder) 
2)Analyze and write in SQLite database results: 
           First table is common for all input files and include information about text: 
book_name	number_of_paragraph	number_of_words	number_of_letters	words_with_capital_letters	words_in_lowercase
           Second table is personal for each input file and should include frequency of each word from input file: 
word	count	count_uppercase
