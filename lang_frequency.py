from collections import Counter

def load_data(filepath):
    
    word_list       = []
    bad_word_list   = ['', '–', '—']
    bad_symbol_list = [',', '.', '(', ')', '«', '»', '%', '!']

    with open(filepath, 'r', encoding = 'utf-8') as in_file:

        for row in in_file:

            row = row.replace('\n' , '')
            row = row.lstrip()
            row = row.rstrip()

            words = row.split(' ')

            for word in words:

                if word not in bad_word_list:

                    for symbol in word:

                        if symbol in bad_symbol_list:
                            
                            word = word.replace(symbol , '')
                   
                    word = word.upper()

                    try:

                        int(word)

                    except ValueError: 

                        word_list.append(word)

    return word_list


def get_most_frequent_words(text):
    
    word_cnt = Counter(word_list)

    word_cnt_first_ten = word_cnt.most_common(10)

    for item in word_cnt_first_ten:

        print('%s - %s' % item)

    # with open('result.txt', 'w', encoding = 'utf-8') as out_file:

    #     for item in word_cnt_first_ten:

    #         out_file.write('%s - %s\n' % (item))


if __name__ == '__main__':
    
    path = 'Эра_современных_ракет.txt'

    word_list = load_data(path)

    get_most_frequent_words(word_list)
