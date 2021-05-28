import sys
user_text = sys.argv[1]
with open('bakery.csv', 'a', encoding='utf-8') as file_1:
    file_1.write(user_text + '\n')