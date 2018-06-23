# -*- coding: UTF-8 -*-
import csv
import os
import string
import unidecode
from googletrans import Translator
translator = Translator()
from wikiapi import WikiApi
wiki = WikiApi()
import time

def is_number(uchar):
    return uchar >= u'0' and uchar<=u'9'

def is_alphabet(uchar):
    return (uchar >= u'a' and uchar<=u'z') or (uchar >= u'A' and uchar<=u'Z')

def check_english(name):
    flag = True
    for uchar in name:
        # 字母，数字，空格，-，_, ., !, 都视为英文名的一部分
        if (not is_alphabet(uchar)) and (not is_number(uchar)) and (uchar != u'\u0020') and (uchar != u'-') and \
               (uchar != u'.') and (uchar != u'!'):
            flag = False
    return flag

def non_english_character_count(name):
    count = 0
    for uchar in name:
        if (not is_alphabet(uchar)) and (not is_number(uchar)) and (uchar != u'\u0020') and (uchar != u'-') and (uchar != u'.'):
            count = count + 1
    return count

def get_full_name_from_wiki(name):
    wiki = WikiApi()
    results = wiki.find(name)
    if len(results) > 0:
        article = wiki.get_article(results[0])
        new_name = article.summary
        new_name = new_name[:new_name.find('(')-1]
        if new_name.find(' refer ') != -1:
            if len(results) > 1:
                article = wiki.get_article(results[1])
                new_name = article.summary
                new_name = new_name[:new_name.find('(') - 1]
            else:
                return None
        table = str.maketrans({key: None for key in string.punctuation + '\r\n'})
        new_name = new_name.translate(table)
        if len(new_name) > 4 and len(new_name) < 50:
            return new_name
        else:
            return None
    else:
        return None

def count_upper(word):
    return len(list(filter(lambda c: c.isupper(), word)))

def is_short_name(name):
    name = name.replace('.','')
    name_split = name.split('_')
    for word in name_split:
        if len(word)==1 or count_upper(word) == len(word):
            return True
    return False

if __name__ == '__main__':
    infile = '.\\files\checked_entity_list_20180612.csv'
    outfile = '.\\files\entity_list_en.csv'
    file = open(outfile, 'w', encoding='utf8')
    i = 0
    with open(infile, 'r', encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            # i += 1
            # if i > 5:
            #     break
            # name = row[0].strip()[10:].replace('.', '._').replace(' ', '_')
            name = row[0].strip()[10:]
            start_time = time.clock()
            if name == 'a._proper_name':
                continue
            end_time = time.clock()
            print('time1=%f' % (end_time-start_time))
            start_time = time.clock()
            if not check_english(name):
                end_time = time.clock()
                print('time2=%f' % (end_time-start_time))
                # If half of the names are regular English characters, see it as an accent.
                start_time = time.clock()
                if non_english_character_count(name) < len(name) / 2:
                    end_time = time.clock()
                    print('time3=%f' % (end_time - start_time))
                    start_time = time.clock()
                    name = unidecode.unidecode(name)
                    end_time = time.clock()
                    print('time4=%f' % (end_time - start_time))
                # Or, take it as a foreign language.
                else:
                    start_time = time.clock()
                    name = translator.translate(name).text
                    end_time = time.clock()
                    print('time5=%f' % (end_time - start_time))
                    # name = translator.translate(name.replace('_', ' ')).text.replace(' ', '_')
                # row[0] = ' "' + name + '"'
            name = name.replace(' ','_').replace('-','_').replace('.','_').replace('___','_').replace('__','_')

            # print(name)
            '''
            # If there is only one capital character in one word, we think this is a short name.
            # We will find the best matched full name from wikipedia.
            if is_short_name(name):
                new_row = row
                new_name = get_full_name_from_wiki(name)
                if new_name is not None:
                    new_row[1] = ' "' + new_name + '"'
                    file.write(','.join(new_row) + '\n')
                else:
                    file.write(','.join(row) + '\n')
            else:
            '''
            # file.write(' '.join([row[0][:9], name, '[', row[0][10:].strip(), ']', '1']) + '\n')
            file.write(' '.join([row[0][:9], name]) + '\n')
            print(name)
            # If the name has only one word, we think this is a nickname,
            # then we will try to find the full name via Wikipedia,
            # and add a new entry into the list with the same Class_ID
    #         if len(name.split('_')) == 1:
    #             new_row = row
    #             new_name = get_full_name_from_wiki(name)
    #             if new_name is not None:
    #                 new_row[1] = ' "' + new_name + '"'
    #                 file.write(','.join(new_row) + '\n')
    #
    file.close()