import random

str_numbers = '1234567890'
str_words = 'qwertyuiopasdfghjklzxcvbnm'
str_final = str_numbers+str_words
ls = list(str_final)
random.shuffle(ls)
new_key = ''.join([random.choice(ls) for x in range(6)])