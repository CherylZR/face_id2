# -*- coding: UTF-8 -*-
import csv
import os
import string
import unidecode
from googletrans import Translator
translator = Translator()
from wikiapi import WikiApi
wiki = WikiApi()
import logging
import time

def is_number(uchar):
    return uchar >= u'0' and uchar<=u'9'

def is_alphabet(uchar):
    return (uchar >= u'a' and uchar<=u'z') or (uchar >= u'A' and uchar<=u'Z')

def check_english(name):
    flag_en = True
    flag_ac = True
    count = 0
    for uchar in name:
        # 对英文字母宽松规定
        if (not is_alphabet(uchar)) and (not is_number(uchar)) and (uchar!=u' ') and (uchar!=u'-') and \
                (uchar!=u'.') and (uchar!=u"'"):
            flag_en = False
            count += 1
    if count > len(name)/2:
        flag_ac = False
    return [flag_en, flag_ac]

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

def find_idx(name):
    idx = 0
    for uchar in name:
        if is_number(uchar):
            idx += 1
        else:
            return idx

if __name__ == '__main__':
    inname = '.\\files\person-id-name_utf8.txt'
    outname = '.\\files\out_person\person_list_'
    infile = open(inname, 'r', encoding='utf8')
    # outfile = open(outname, 'w', encoding='utf8')
    i = 0
    for row in infile.readlines()[87685:]:

        # if i>20:
        #     break
        strip_row = row.strip()
        idx = find_idx(strip_row)
        name = strip_row[idx:]
        check_en_result = check_english(name)
        if not check_en_result[0]:
            if check_en_result[1]:
                name = unidecode.unidecode(name)
            else:
                # for try_times in range(10):
                #     try:
                #         name = translator.translate(name).txt
                #         break
                #     except:
                #         time.sleep(5)
                #         logging.warning('%s fail %s times' % (name, try_times+1))
                #         if try_times == 9:
                #             os._exit(0)
                #         else:
                #             continue
                name = translator.translate(name).text

        name = name.replace(' ','_').replace('-','_').replace('.','_').replace('___','_').replace('__','_')

        outname_full = outname + str(1001//1000).zfill(4) + '.txt'
        outfile = open(outname_full, 'a', encoding='utf8')
        outfile.write(' '.join([row[:idx], name]) + '\n')
        outfile.close()
        # print(name)
        # outfile.write(' '.join([row[:9], name]) + '\n')
        print(name)
    # outfile.close()
        i += 1
    infile.close()