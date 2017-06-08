import re

word_re = re.compile(r'[а-яА-Я]+')

in_file=open('test.txt', 'r', encoding = 'utf-8')
row_list_initial = in_file.read()
row_list_initial = row_list_initial.upper()
words_list = word_re.findall(row_list_initial)

print(words_list)

words_list_cleaned = [word for word in words_list if word]


# word_list = word_list + words
print(words_list_cleaned)

in_file.close()
# row_list = [row.upper() for row in row_list_initial]
# print(row_list)