from collections import Counter
import re, os

def load_data(filepath):
    with open(filepath, 'r', encoding = 'utf-8') as in_file:
        row_list = in_file.readlines()
    return row_list
        
def process_data(row_list):
    word_list_initial = []
    row_list_cleaned = [re.sub(r'\d|\n|\(|\)|\.|\,|\–|\—|\.?\-\.?|\%|\«|\»', '', row, flags=re.IGNORECASE) for row in row_list]
    for words in row_list_cleaned:
        words = words.split(' ')
        word_list_initial = word_list_initial + words
    word_list_final = [word.upper() for word in word_list_initial if word]
    first_most_common_words_to_show = 10
    word_counter = Counter(word_list_final)
    word_counter_first_ten = word_counter.most_common(first_most_common_words_to_show)
    return word_counter_first_ten

def get_most_frequent_words(word_counter_first_ten):
    for item in word_counter_first_ten:
        print('%s - %s' % item)
   
if __name__ == '__main__':
    path = input('Пожалуйста, введите имя файла (путь)\n')
    row_list = load_data(path)
    word_counter_first_ten = process_data(row_list)
    get_most_frequent_words(word_counter_first_ten)