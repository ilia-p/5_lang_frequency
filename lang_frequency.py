from collections import Counter
import re, os
import argparse

parser = argparse.ArgumentParser(description = 'file_name')
parser.add_argument('-p', '--file', type = str, required = True, help = 'text file to explore')

def load_data(filepath):
    with open(filepath, 'r', encoding = 'utf-8') as in_file:
        row_list_initial = in_file.read()
    return row_list_initial
        
def process_data(row_list_initial):
    row_list_upper = row_list_initial.upper()
    words_list = re.compile(r'[А-Я]+').findall(row_list_upper)
    word_list_cleaned = [word for word in words_list if word]
    first_most_common_words_to_show = 10
    word_counter = Counter(word_list_cleaned)
    word_counter_first_ten = word_counter.most_common(first_most_common_words_to_show)
    return word_counter_first_ten

def get_most_frequent_words(word_counter_first_ten):
    for item in word_counter_first_ten:
        print('{0} - {1}'.format(item[0],item[1]))
   
if __name__ == '__main__':
    arg = parser.parse_args()
    row_list = load_data(arg.file)
    word_counter_first_ten = process_data(row_list)
    get_most_frequent_words(word_counter_first_ten)