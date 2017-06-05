import re

word_re = re.compile(r'[а-я]+')

mystr = 'и или если бы'

words = word_re.findall(mystr)

print(words)