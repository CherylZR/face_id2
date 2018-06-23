# -*- coding: UTF-8 -*-

from googletrans import Translator
from wikiapi import WikiApi
import unidecode
import csv

from googletrans import Translator
import unidecode
import csv
from wikiapi import WikiApi
import string

# def count_upper(word):
#     return len(list(filter(lambda c: c.isupper(), word)))
#
# def is_short_name(name):
#     name = name.replace('.',' ')
#     name_split = name.split(' ')
#     for word in name_split:
#         if len(word)==1 or count_upper(word) == len(word):
#             return True
#     return False
#
# def get_full_name_from_wiki(name):
#     wiki = WikiApi()
#     results = wiki.find(name)
#     if len(results) > 0:
#         article = wiki.get_article(results[0])
#         new_name = article.summary
#         new_name = new_name[:new_name.find('(')-1]
#         if new_name.find(' refer ') != -1:
#             if len(results) > 1:
#                 article = wiki.get_article(results[1])
#                 new_name = article.summary
#                 new_name = new_name[:new_name.find('(') - 1]
#             else:
#                 return None
#         table = str.maketrans({key: None for key in string.punctuation + '\r\n'})
#         new_name = new_name.translate(table)
#         if len(new_name) > 4 and len(new_name) < 50:
#             return new_name
#         else:
#             return None
#     else:
#         return None
#
# if __name__ == '__main__':
#     name = 'Amanda.S'
#
#     if is_short_name(name):
#         new_name = get_full_name_from_wiki(name)
#         if new_name is not None:
#             print(new_name)
#             print(1)
#         else:
#             print(name)





# i = 0
# # with open('e:\datasets\id\checked_entity_list_20180612.csv', 'r', encoding="utf8") as csvfile:
#     spamreader = csv.reader(csvfile)
#     for row in spamreader:
#         i += 1
#         if i > 5:
#             break
#         print(row)

# translator = Translator()
# # unidecode.unidecode
# name = translator.translate(u'Kelly A. O\'Leary \'la\'')
# name = translator.translate(u'Vladimír Hlavatý').text
# name = name.replace('-','').replace(' ','_').replace('.','_').replace('__','_')
# print(name)
# print(u'哈')


# i = 0
# with open('e:\datasets\id\checked_entity_list_20180612.csv', 'r', encoding="utf8") as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
#     for row in spamreader:
#         i+=1
#         if i>3:
#             break
#         name = row[0].strip()[10:].replace('.','._').replace('__','_')
#         if name == 'a._proper_name':
#             continue
#         print(name)
#         if not check_english(name):
#             # If half of the names are regular English characters, see it as an accent.
#             if non_english_character_count(name) < len(name) / 2:
#                 name = unidecode.unidecode(name)
#             # Or, take it as a foreign language.
#             else:
#                 name = translator.translate(name.replace('_', ' ')).text.replace(' ', '_')
#             row[1] = ' "' + name + '"'
#             print(row)

infile = open('.\\files\checked_entity_list_20180612.txt', encoding='utf8')
i = 0
for line in infile.readlines():
    i += 1
    if i>5:
        break
    print(line)