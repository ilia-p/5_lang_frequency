from collections import Counter
import re, os
import argparse

parser = argparse.ArgumentParser(description = 'file_name')
parser.add_argument('-p', '--file', type = str, required = True, help = 'text file to explore')
arg = parser.parse_args()

word_re = re.compile(r'[А-Я]+')

def load_data(filepath):
    with open(filepath, 'r', encoding = 'utf-8') as in_file:
        row_list_initial = in_file.readlines()
        row_list = [row.upper() for row in row_list_initial]
    return row_list
        
def process_data(row_list):
    word_list = []
    row_list_cleaned = [re.sub(r'^[а-я]', '', row, flags=re.IGNORECASE) for row in row_list]
    for row in row_list_cleaned:
        words = word_re.findall(row)
        word_list = word_list + words
    first_most_common_words_to_show = 10
    word_counter = Counter(word_list)
    word_counter_first_ten = word_counter.most_common(first_most_common_words_to_show)
    return word_counter_first_ten

def get_most_frequent_words(word_counter_first_ten):
    for item in word_counter_first_ten:
        print('%s - %s' % item)
   
if __name__ == '__main__':
    row_list = load_data(arg.file)
    word_counter_first_ten = process_data(row_list)
    get_most_frequent_words(word_counter_first_ten)