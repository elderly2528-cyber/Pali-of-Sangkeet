# -*- coding: utf-8 -*-
from source_pali import *
from convert_Pali import *




rassa_sara = ['a','i','u']
digha_sara = ['ā','ī','ū','e','o']
byanjana_sithila = ['k','g','c','j','ṭ','ḍ','p','b']
special_byanjana = ['y','r','l','v','s','h','ḷ']
nigghahita = 'ṃ'
ha = 'h'
vagganta = ['ṅ','ñ','ṇ','n','m']
byanjana_dhanita = [item+ha for item in byanjana_sithila]
sara_plus = [item+nigghahita for item in rassa_sara]

def romantothaipali(book):
    dict_roman_eng = {
        '1':'a',
        '2':'ā',
        '3':'i',
        '4':'ī',
        '5':'u',
        '6':'ū',
        '7':'e',
        '8':'o',
        '9':'ṃ',
        'A':'k',
        'B':'g',
        'C':'ṅ',
        'D':'c',
        'E':'j',
        'F':'ñ',
        'G':'ṭ',
        'H':'ḍ',
        'I':'ṇ',
        'J':'t',
        'K':'d',
        'L':'n',
        'M':'p',
        'N':'b',
        'O':'m',
        'P':'y',
        'Q':'r',
        'R':'l',
        'S':'v',
        'T':'s',
        'U':'h',
        'V':'ḷ',
        'W':' '
    }
    def changekeyvalue(dic):
        dic = dict()
        for key,value in dict_roman_eng.items():
            dic[value]= key
        return dic

    eng_roman = changekeyvalue(dict_roman_eng)


    sara = {
        '1':'อ',
        '2':'อา',
        '3':'อิ',
        '4':'อี',
        '5':'อุ',
        '6':'อู',
        '7':'เอ',
        '8':'โอ'
    }

    sara_akkhara = {
        '0':'ฺ',
        '1':'',
        '2':'า',
        '3':'ิ',
        '4':'ี',
        '5':'ุ',
        '6':'ู'
    }
    byanjana = {
        'A':'ก',
        'AU':'ข',
        'B':'ค',
        'BU':'ฆ',
        'C':'ง',
        'D':'จ',
        'DU':'ฉ',
        'E':'ช',
        'EU':'ฌ',
        'F':'ญ',
        'G':'ฏ',
        'GU':'ฐ',
        'H':'ฑ',
        'HU':'ฒ',
        'I':'ณ',
        'J':'ต',
        'JU':'ถ',
        'K':'ท',
        'KU':'ธ',
        'L':'น',
        'M':'ป',
        'MU':'ผ',
        'N':'พ',
        'NU':'ภ',
        'O':'ม',
        'P':'ย',
        'Q':'ร',
        'R':'ล',
        'S':'ว',
        'T':'ส',
        'U':'ห',
        'V':'ฬ'
    }

    byanjana_saraakkhara = mergedict(byanjana,sara_akkhara)

    sara_flib = {
        '7':'เ',
        '8':'โ'
    }


    def mergedict3(dict1, dict2):
        dict3 = dict()
        for key1, value1 in dict1.items():
            for key2, value2 in dict2.items():
                dict3[key1 + key2] = value2 + value1
        return dict3




    byanjana_saraflib = mergedict3(byanjana,sara_flib)

    nigahita = {
        '9':'ํ'
    }

    vagga = {
        'W':' '
    }

    word_pali = dict()
    word_pali.update(sara)
    word_pali.update(byanjana_saraakkhara)
    word_pali.update(byanjana_saraflib)
    word_pali.update(nigahita)
    word_pali.update(vagga)

    boot = list(book)
    boong =[]

    boong.append(boot[0].lower())
    if len(boot) > 0:
        i = 1
        while i > 0 and i < len(boot):
            boong.append(boot[i].lower())
            i = i+1

    x = []
    for item in boong:
        x.append(eng_roman[item])

    pwd = ['1','2','3','4','5','6','7','8']
    pwe = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V']
    pwf = ['A','B','D','E','G','H','J','K','M','N']
    z = []
    i = 0

    while i >= 0 and i < len(x):
        if x[i] in pwd:
            z.append(x[i])
        elif x[i] in pwf and x[i+1] == 'U' and x[i+2] in pwd:
            z.append(x[i]+x[i+1]+x[i+2])
            i = i+2
        elif x[i] in pwe and x[i+1] in pwd:
            z.append(x[i]+x[i+1])
            i = i+1
        elif x[i] == 'U' and x[i+1] in pwd:
            z.append(x[i]+x[i+1])
            i = i+1
        elif x[i] in pwe and x[i+1] in pwf and x[i+2] == 'U' and x[i+3] in pwd:
            z.append(x[i]+'0')
        elif x[i] in pwe and x[i+1] in pwe and x[i+2] in pwd:
            z.append(x[i]+'0')
        elif x[i] == '9':
            z.append(x[i])
        else:
            z.append(x[i])
        i = i+1

    y = []
    for item in z:
        y.append(word_pali[item])
    return listtostring(y)


if __name__ == '__main__':
    word = 'niyaṃputtaṃ'
    print(romantothaipali(word))