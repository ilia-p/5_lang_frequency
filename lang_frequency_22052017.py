from collections import Counter
import re

def load_data(filepath):
    word_list = []
    with open(filepath, 'r', encoding = 'utf-8') as in_file:
        for row in in_file:
            row = row.replace('\n' , '')
            row = row.lstrip()
            row = row.rstrip()
            words = row.split(' ')
            for word in words:
                word_list.append(word)
    return word_list
 
def word_clean(list):
    cleaned_word_list = []
    bad_symbol_list = [',', '.', '(', ')', '«', '»', '%', '!', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '–', '—']
    for word in word_list:
        for symbol in word:
            if symbol in bad_symbol_list:
                word = word.replace(symbol, '')            
        if word != '':
            word = word.upper()
            cleaned_word_list.append(word)
    return cleaned_word_list

def get_most_frequent_words(text):
    word_cnt = Counter(cleaned_word_list)
    word_cnt_first_ten = word_cnt.most_common(10)
    for item in word_cnt_first_ten:
        print('%s - %s' % item)
   
if __name__ == '__main__':
    path = 'Эра_современных_ракет.txt'
    word_list = load_data(path)
    cleaned_word_list = word_clean(word_list)
    get_most_frequent_words(cleaned_word_list)
