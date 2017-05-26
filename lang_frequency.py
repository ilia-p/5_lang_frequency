from collections import Counter
import re, os

def load_data(filepath):
    word_list_initial = []
    word_list_final   = []
    with open(filepath, 'r', encoding = 'utf-8') as in_file:
        row_list = in_file.readlines()
        for row in row_list:
            row = re.sub(r'\d|\n|\(|\)|\.|\,|\–|\—|\.?\-\.?|\%|\«|\»|[a-zA-Z]', '', row, flags=re.IGNORECASE)
            words = row.split(' ')
            word_list_initial = word_list_initial + words
        for word in word_list_initial:
            if word:
                word = word.upper()
                word_list_final.append(word)
    return word_list_final

def get_most_frequent_words(word_list_final):
    first_most_common_words_to_show = 10
    word_counter = Counter(word_list_final)
    word_counter_first_ten = word_counter.most_common(first_most_common_words_to_show)
    for item in word_counter_first_ten:
        print('%s - %s' % item)
   
if __name__ == '__main__':
    path = input('Пожалуйста, введите имя файла (путь)\n')
    word_list_final = load_data(path)
    get_most_frequent_words(word_list_final)
    

    