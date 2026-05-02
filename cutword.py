# -*- coding: utf-8 -*-





def cutword(bhrammajala):
    Alphabetic = {
             '0':'อ',
             'h':'า',
             'i':'ิ',
             'j':'ี',
             'k':'ุ',
             'l':'ู',
             'm':'เ',
             'n':'โ',
             'g':'ํ',
             'o':'ฺ',
            'p':' ',
            'q':'ฯ',
            'r':'\n',
            'r1':'\t',
            '1': '๑',
            '2': '๒',
            '3': '๓',
            '4': '๔',
            '5': '๕',
            '6': '๖',
            '7': '๗',
            '8': '๘',
            '9': '๙',
            's': '๐',
            's1':'§',
            's2':'+',
            's3':'`',
            's4':'ै',
            's5':'ऋ',
            't': '.',
            'u': '–',
            'u1':'-',
            'u2':'!',
            'v': ',',
            'w': ';',
            'x': '[',
            'y': ']',
            'y1':'=',
            'z': '(',
            'z1': ')',
            'z2': '’',
            'z3': '‘',
            'z4': '\uf711',
            'z5': '…',
            'z6':'ः',
            'z7':'“',
            'z8':'์',
            'z9':'ิํ',
            'z10':'"',
            'z11':'?',
            'z12':':',
            'z13':'\x87',
        'A' : 'ก',
        'B' : 'ข',
        'C' : 'ค',
        'D' : 'ฆ',
        'E' : 'ง',
        'F' : 'จ',
        'G' : 'ฉ',
        'H' : 'ช',
        'I' : 'ฌ',
        'J' : 'ญ',
        'K' : 'ฏ',
        'L' : 'ฐ',
        'M' : 'ฑ',
        'N' : 'ฒ',
        'O' : 'ณ',
        'P' : 'ต',
        'Q' : 'ถ',
        'R' : 'ท',
        'S' : 'ธ',
        'T' : 'น',
        'U' : 'ป',
        'V' : 'ผ',
        'W' : 'พ',
        'X' : 'ภ',
        'Y' : 'ม',
        'Z' : 'ย',
        'a' : 'ร',
        'b' : 'ล',
        'c' : 'ว',
        'd' : 'ส',
        'e' : 'ห',
        'f' : 'ฬ'
    }




    keysA = ['0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f']
    havA = {x:Alphabetic[x] for x in keysA}



    Vowels = ['g','h','i','j','k','l','m','n','o']
    changA = {x:Alphabetic[x] for x in Vowels}


    keysB = ['h','i','j','k','l']
    backA = {x:changA[x] for x in keysB}

    def mergedict(dict1,dict2):
        dict3 = dict()
        for key1,value1 in dict1.items():
            for key2,value2 in dict2.items():
                dict3[key1+key2] =value1+value2
        return dict3


    keysC = ['m','n']
    frontA = {x:changA[x] for x in keysC}



    keysD = ['o']
    haftA = {x:changA[x] for x in keysD}



    keysE = ['g']
    am = {x:changA[x] for x in keysE}



    keysF = ['i']
    im = {x:changA[x] for x in keysF}

    def mergedict2(dict1,dict2,dict3):
        dict4 = dict()
        for key1,value1 in dict1.items():
            for key2,value2 in dict2.items():
                for key3,value3 in dict3.items():
                    dict4[key1+key2+key3] = value1+value2+value3
        return dict4



    keysG = ['k']
    um = {x:changA[x] for x in keysG}

    group1 = havA
    group2 = mergedict(havA,backA)
    group3 = mergedict(frontA,havA)
    group4 = mergedict(havA,haftA)
    group5 = mergedict(havA,am)
    group6 = mergedict2(havA,im,am)
    group7 = mergedict2(havA,um,am)


    wordpali = dict()
    wordpali.update(group1)
    wordpali.update(group2)
    wordpali.update(group3)
    wordpali.update(group4)
    wordpali.update(group5)
    wordpali.update(group6)
    wordpali.update(group7)

    allword = wordpali.keys()

    cut_unit = ['p', 'q', 'r', '1', '2', '3', '4', '5', '6', '7', '8', '9', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                    'z1', 'z2', 'z3', 'z4', 'z5']
    g = []
    def lstostring(w):
        out_str= ""
        for x in w:
            g.append(out_str.join(x))
        return g


    def sortreversed(y):
        i = []
        for a in range(0, len(y)):
            i.append(y[-1 - a])
        return i


    def converttovalues(bb):
        g =[]
        for i in range(0, len(bb)):
            d = bb[i]

            def tovalues(d):
                h = []
                d = bb[i]
                j = 0
                while j >= 0 and j < len(d):
                    w = Alphabetic[d[j]]
                    h.append(w)
                    j += 1
                return h

            g.append(tovalues(d))
        return g



    r=0
    w = []
    def groupword(q):
        r = len(q)-1
        c = []
        while r>=0 and r < len(q):
            if q[r] in keysA and q[r-1] in keysC:
                w.append(q[r-1]+q[r])
                r -= 2
            elif q[r] in keysE and q[r-1] in ['i','k']:
                w.append(q[r-2]+q[r-1]+q[r])
                r -= 3
            elif q[r] in keysE and q[r-1] in keysA:
                w.append(q[r-1]+q[r])
                r -= 2
            elif q[r] in keysD and q[r-1] in keysA:
                w.append(q[r-1]+q[r])
                r -= 2
            elif q[r] in keysB and q[r-1] in keysA:
                w.append(q[r-1]+q[r])
                r -= 2
            else:
                w.append(q[r])
                r -= 1

        b = sortreversed(w)

        i = 0
        t = len(b)-1
        while t >= 0 and t < len(b):

            if b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and \
                    b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
                t - 9] in \
                    allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
                t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword and b[
                t - 17] in allword and b[t - 18] in allword and b[t - 19] in allword and b[t - 20] in allword and b[
                t - 21] in allword and b[t - 22] in allword and b[t - 23] in allword and b[t - 24] in allword and b[
                t - 25] in allword and b[t - 26] in allword and b[t - 27] in allword and b[t - 28] in allword and b[
                t - 29] in allword and b[t - 30] in allword and b[t - 31] in allword and b[t - 32] in allword and b[
                t - 33] in allword and b[t - 34] in allword and b[t - 35] in allword and b[t - 36] in allword and b[
                t - 37] in allword and b[t - 38] in allword and b[t - 39] in allword and b[t - 40] in allword and b[
                t - 41] in allword and b[t - 42] in allword and b[t - 43] in allword and b[t-44] in allword and b[t-45] in allword and b[t-46] in allword and b[t-47] in allword and b[t-48] in allword and b[t-49] in allword:
                c.append(
                    b[t-49] + b[t-48] + b[t-47] + b[t-46] + b[t-45] + b[t-44] + b[t - 43] + b[t - 42] + b[t - 41] + b[t - 40] + b[t - 39] + b[t - 38] + b[t - 37] + b[t - 36] + b[
                        t - 35] + b[t - 34] + b[t - 33] + b[t - 32] + b[t - 31] + b[t - 30] + b[t - 29] + b[t - 28] + b[
                        t - 27] + b[t - 26] + b[t - 25] + b[t - 24] + b[t - 23] + b[t - 22] + b[t - 21] + b[t - 20] + b[
                        t - 19] + b[t - 18] + b[t - 17] + b[t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[
                        t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[
                        t - 3] + b[t - 2] + b[t - 1] + b[t])
                t -= 49


            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and \
                    b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
                t - 9] in \
                    allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
                t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword and b[
                t - 17] in allword and b[t - 18] in allword and b[t - 19] in allword and b[t - 20] in allword and b[
                t - 21] in allword and b[t - 22] in allword and b[t - 23] in allword and b[t - 24] in allword and b[
                t - 25] in allword and b[t - 26] in allword and b[t - 27] in allword and b[t - 28] in allword and b[
                t - 29] in allword and b[t - 30] in allword and b[t - 31] in allword and b[t - 32] in allword and b[
                t - 33] in allword and b[t - 34] in allword and b[t - 35] in allword and b[t - 36] in allword and b[
                t - 37] in allword and b[t - 38] in allword and b[t - 39] in allword and b[t - 40] in allword and b[
                t - 41] in allword and b[t - 42] in allword and b[t - 43] in allword and b[t-44] in allword and b[t-45] in allword and b[t-46] in allword and b[t-47] in allword and b[t-48] in allword:
                c.append(
                    b[t-48] + b[t-47] + b[t-46] + b[t-45] + b[t-44] + b[t - 43] + b[t - 42] + b[t - 41] + b[t - 40] + b[t - 39] + b[t - 38] + b[t - 37] + b[t - 36] + b[
                        t - 35] + b[t - 34] + b[t - 33] + b[t - 32] + b[t - 31] + b[t - 30] + b[t - 29] + b[t - 28] + b[
                        t - 27] + b[t - 26] + b[t - 25] + b[t - 24] + b[t - 23] + b[t - 22] + b[t - 21] + b[t - 20] + b[
                        t - 19] + b[t - 18] + b[t - 17] + b[t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[
                        t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[
                        t - 3] + b[t - 2] + b[t - 1] + b[t])
                t -= 48

            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and \
                    b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
                t - 9] in \
                    allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
                t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword and b[
                t - 17] in allword and b[t - 18] in allword and b[t - 19] in allword and b[t - 20] in allword and b[
                t - 21] in allword and b[t - 22] in allword and b[t - 23] in allword and b[t - 24] in allword and b[
                t - 25] in allword and b[t - 26] in allword and b[t - 27] in allword and b[t - 28] in allword and b[
                t - 29] in allword and b[t - 30] in allword and b[t - 31] in allword and b[t - 32] in allword and b[
                t - 33] in allword and b[t - 34] in allword and b[t - 35] in allword and b[t - 36] in allword and b[
                t - 37] in allword and b[t - 38] in allword and b[t - 39] in allword and b[t - 40] in allword and b[
                t - 41] in allword and b[t - 42] in allword and b[t - 43] in allword and b[t-44] in allword and b[t-45] in allword and b[t-46] in allword and b[t-47] in allword:
                c.append(
                    b[t-47] + b[t-46] + b[t-45] + b[t-44] + b[t - 43] + b[t - 42] + b[t - 41] + b[t - 40] + b[t - 39] + b[t - 38] + b[t - 37] + b[t - 36] + b[
                        t - 35] + b[t - 34] + b[t - 33] + b[t - 32] + b[t - 31] + b[t - 30] + b[t - 29] + b[t - 28] + b[
                        t - 27] + b[t - 26] + b[t - 25] + b[t - 24] + b[t - 23] + b[t - 22] + b[t - 21] + b[t - 20] + b[
                        t - 19] + b[t - 18] + b[t - 17] + b[t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[
                        t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[
                        t - 3] + b[t - 2] + b[t - 1] + b[t])
                t -= 47
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and \
                    b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
                t - 9] in \
                    allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
                t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword and b[
                t - 17] in allword and b[t - 18] in allword and b[t - 19] in allword and b[t - 20] in allword and b[
                t - 21] in allword and b[t - 22] in allword and b[t - 23] in allword and b[t - 24] in allword and b[
                t - 25] in allword and b[t - 26] in allword and b[t - 27] in allword and b[t - 28] in allword and b[
                t - 29] in allword and b[t - 30] in allword and b[t - 31] in allword and b[t - 32] in allword and b[
                t - 33] in allword and b[t - 34] in allword and b[t - 35] in allword and b[t - 36] in allword and b[
                t - 37] in allword and b[t - 38] in allword and b[t - 39] in allword and b[t - 40] in allword and b[
                t - 41] in allword and b[t - 42] in allword and b[t - 43] in allword and b[t-44] in allword and b[t-45] in allword and b[t-46] in allword:
                c.append(
                    b[t-46] + b[t-45] + b[t-44] + b[t - 43] + b[t - 42] + b[t - 41] + b[t - 40] + b[t - 39] + b[t - 38] + b[t - 37] + b[t - 36] + b[
                        t - 35] + b[t - 34] + b[t - 33] + b[t - 32] + b[t - 31] + b[t - 30] + b[t - 29] + b[t - 28] + b[
                        t - 27] + b[t - 26] + b[t - 25] + b[t - 24] + b[t - 23] + b[t - 22] + b[t - 21] + b[t - 20] + b[
                        t - 19] + b[t - 18] + b[t - 17] + b[t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[
                        t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[
                        t - 3] + b[t - 2] + b[t - 1] + b[t])
                t -= 46

            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and \
                    b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
                t - 9] in \
                    allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
                t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword and b[
                t - 17] in allword and b[t - 18] in allword and b[t - 19] in allword and b[t - 20] in allword and b[
                t - 21] in allword and b[t - 22] in allword and b[t - 23] in allword and b[t - 24] in allword and b[
                t - 25] in allword and b[t - 26] in allword and b[t - 27] in allword and b[t - 28] in allword and b[
                t - 29] in allword and b[t - 30] in allword and b[t - 31] in allword and b[t - 32] in allword and b[
                t - 33] in allword and b[t - 34] in allword and b[t - 35] in allword and b[t - 36] in allword and b[
                t - 37] in allword and b[t - 38] in allword and b[t - 39] in allword and b[t - 40] in allword and b[
                t - 41] in allword and b[t - 42] in allword and b[t - 43] in allword and b[t-44] in allword and b[t-45] in allword:
                c.append(
                    b[t-45] + b[t-44] + b[t - 43] + b[t - 42] + b[t - 41] + b[t - 40] + b[t - 39] + b[t - 38] + b[t - 37] + b[t - 36] + b[
                        t - 35] + b[t - 34] + b[t - 33] + b[t - 32] + b[t - 31] + b[t - 30] + b[t - 29] + b[t - 28] + b[
                        t - 27] + b[t - 26] + b[t - 25] + b[t - 24] + b[t - 23] + b[t - 22] + b[t - 21] + b[t - 20] + b[
                        t - 19] + b[t - 18] + b[t - 17] + b[t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[
                        t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[
                        t - 3] + b[t - 2] + b[t - 1] + b[t])
                t -= 45

            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and \
                    b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[t - 8] in allword and b[
                t - 9] in \
                    allword and b[t - 10] in allword and b[t - 11] in allword and b[t - 12] in allword and b[
                t - 13] in allword and b[t - 14] in allword and b[t - 15] in allword and b[t - 16] in allword and b[
                t - 17] in allword and b[t - 18] in allword and b[t - 19] in allword and b[t - 20] in allword and b[
                t - 21] in allword and b[t - 22] in allword and b[t - 23] in allword and b[t - 24] in allword and b[
                t - 25] in allword and b[t - 26] in allword and b[t - 27] in allword and b[t - 28] in allword and b[
                t - 29] in allword and b[t - 30] in allword and b[t - 31] in allword and b[t - 32] in allword and b[
                t - 33] in allword and b[t - 34] in allword and b[t - 35] in allword and b[t - 36] in allword and b[
                t - 37] in allword and b[t - 38] in allword and b[t - 39] in allword and b[t - 40] in allword and b[
                t - 41] in allword and b[t - 42] in allword and b[t - 43] in allword and b[t-44] in allword:
                c.append(
                    b[t-44] + b[t - 43] + b[t - 42] + b[t - 41] + b[t - 40] + b[t - 39] + b[t - 38] + b[t - 37] + b[t - 36] + b[
                        t - 35] + b[t - 34] + b[t - 33] + b[t - 32] + b[t - 31] + b[t - 30] + b[t - 29] + b[t - 28] + b[
                        t - 27] + b[t - 26] + b[t - 25] + b[t - 24] + b[t - 23] + b[t - 22] + b[t - 21] + b[t - 20] + b[
                        t - 19] + b[t - 18] + b[t - 17] + b[t - 16] + b[t - 15] + b[t - 14] + b[t - 13] + b[t - 12] + b[
                        t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[
                        t - 3] + b[t - 2] + b[t - 1] + b[t])
                t -= 44

            elif b[t] in allword and b[t-1] in allword and b[t-2] in allword and b[t-3] in allword and b[t-4] in allword and \
                    b[t-5] in allword and b[t-6] in allword and b[t-7] in allword and b[t-8] in allword and b[t-9] in \
                    allword and b[t-10] in allword and b[t-11] in allword and b[t-12] in allword and b[t-13] in allword and b[t-14] in allword and b[t-15] in allword and b[t-16] in allword and b[t-17] in allword and b[t-18] in allword and b[t-19] in allword and b[t-20] in allword and b[t-21] in allword and b[t-22] in allword and b[t-23] in allword and b[t-24] in allword and b[t-25] in allword and b[t-26] in allword and b[t-27] in allword and b[t-28] in allword and b[t-29] in allword and b[t-30] in allword and b[t-31] in allword and b[t-32] in allword and b[t-33] in allword and b[t-34] in allword and b[t-35] in allword and b[t-36] in allword and b[t-37] in allword and b[t-38] in allword and b[t-39] in allword and b[t-40] in allword and b[t-41] in allword and b[t-42] in allword and b[t-43] in allword:
                c.append(b[t-43] + b[t-42] + b[t-41] + b[t-40] + b[t-39] + b[t-38] + b[t-37] + b[t-36] + b[t-35] + b[t-34] + b[t-33] + b[t-32] + b[t-31] + b[t-30] + b[t-29] + b[t-28] + b[t-27] + b[t-26] + b[t-25] + b[t-24] + b[t-23] + b[t-22] + b[t-21] + b[t-20] + b[t-19] + b[t-18] + b[t-17] + b[t-16] + b[t-15] + b[t-14] + b[t-13] + b[t-12] + b[t-11] + b[t-10] + b[t-9] + b[t-8] + b[t-7] + b[t-6] + b[t-5] + b[t-4] + b[t-3] + b[t-2] + b[t-1] + b[t])
                t-=43
            elif b[t] in allword and b[t-1] in allword and b[t-2] in allword and b[t-3] in allword and b[t-4] in allword and \
                    b[t-5] in allword and b[t-6] in allword and b[t-7] in allword and b[t-8] in allword and b[t-9] in \
                    allword and b[t-10] in allword and b[t-11] in allword and b[t-12] in allword and b[t-13] in allword and b[t-14] in allword and b[t-15] in allword and b[t-16] in allword and b[t-17] in allword and b[t-18] in allword and b[t-19] in allword and b[t-20] in allword and b[t-21] in allword and b[t-22] in allword and b[t-23] in allword and b[t-24] in allword and b[t-25] in allword and b[t-26] in allword and b[t-27] in allword and b[t-28] in allword and b[t-29] in allword and b[t-30] in allword and b[t-31] in allword and b[t-32] in allword and b[t-33] in allword and b[t-34] in allword and b[t-35] in allword and b[t-36] in allword and b[t-37] in allword and b[t-38] in allword and b[t-39] in allword and b[t-40] in allword and b[t-41] in allword and b[t-42] in allword:
                c.append(b[t-42] + b[t-41] + b[t-40] + b[t-39] + b[t-38] + b[t-37] + b[t-36] + b[t-35] + b[t-34] + b[t-33] + b[t-32] + b[t-31] + b[t-30] + b[t-29] + b[t-28] + b[t-27] + b[t-26] + b[t-25] + b[t-24] + b[t-23] + b[t-22] + b[t-21] + b[t-20] + b[t-19] + b[t-18] + b[t-17] + b[t-16] + b[t-15] + b[t-14] + b[t-13] + b[t-12] + b[t-11] + b[t-10] + b[t-9] + b[t-8] + b[t-7] + b[t-6] + b[t-5] + b[t-4] + b[t-3] + b[t-2] + b[t-1] + b[t])
                t-=42
            elif b[t] in allword and b[t-1] in allword and b[t-2] in allword and b[t-3] in allword and b[t-4] in allword and \
                    b[t-5] in allword and b[t-6] in allword and b[t-7] in allword and b[t-8] in allword and b[t-9] in \
                    allword and b[t-10] in allword and b[t-11] in allword and b[t-12] in allword and b[t-13] in allword and b[t-14] in allword and b[t-15] in allword and b[t-16] in allword and b[t-17] in allword and b[t-18] in allword and b[t-19] in allword and b[t-20] in allword and b[t-21] in allword and b[t-22] in allword and b[t-23] in allword and b[t-24] in allword and b[t-25] in allword and b[t-26] in allword and b[t-27] in allword and b[t-28] in allword and b[t-29] in allword and b[t-30] in allword and b[t-31] in allword and b[t-32] in allword and b[t-33] in allword and b[t-34] in allword and b[t-35] in allword and b[t-36] in allword and b[t-37] in allword and b[t-38] in allword and b[t-39] in allword and b[t-40] in allword and b[t-41] in allword:
                c.append(b[t-41] + b[t-40] + b[t-39] + b[t-38] + b[t-37] + b[t-36] + b[t-35] + b[t-34] + b[t-33] + b[t-32] + b[t-31] + b[t-30] + b[t-29] + b[t-28] + b[t-27] + b[t-26] + b[t-25] + b[t-24] + b[t-23] + b[t-22] + b[t-21] + b[t-20] + b[t-19] + b[t-18] + b[t-17] + b[t-16] + b[t-15] + b[t-14] + b[t-13] + b[t-12] + b[t-11] + b[t-10] + b[t-9] + b[t-8] + b[t-7] + b[t-6] + b[t-5] + b[t-4] + b[t-3] + b[t-2] + b[t-1] + b[t])
                t-=41
            elif b[t] in allword and b[t-1] in allword and b[t-2] in allword and b[t-3] in allword and b[t-4] in allword and \
                    b[t-5] in allword and b[t-6] in allword and b[t-7] in allword and b[t-8] in allword and b[t-9] in \
                    allword and b[t-10] in allword and b[t-11] in allword and b[t-12] in allword and b[t-13] in allword and b[t-14] in allword and b[t-15] in allword and b[t-16] in allword and b[t-17] in allword and b[t-18] in allword and b[t-19] in allword and b[t-20] in allword and b[t-21] in allword and b[t-22] in allword and b[t-23] in allword and b[t-24] in allword and b[t-25] in allword and b[t-26] in allword and b[t-27] in allword and b[t-28] in allword and b[t-29] in allword and b[t-30] in allword and b[t-31] in allword and b[t-32] in allword and b[t-33] in allword and b[t-34] in allword and b[t-35] in allword and b[t-36] in allword and b[t-37] in allword and b[t-38] in allword and b[t-39] in allword and b[t-40] in allword:
                c.append(b[t-40] + b[t-39] + b[t-38] + b[t-37] + b[t-36] + b[t-35] + b[t-34] + b[t-33] + b[t-32] + b[t-31] + b[t-30] + b[t-29] + b[t-28] + b[t-27] + b[t-26] + b[t-25] + b[t-24] + b[t-23] + b[t-22] + b[t-21] + b[t-20] + b[t-19] + b[t-18] + b[t-17] + b[t-16] + b[t-15] + b[t-14] + b[t-13] + b[t-12] + b[t-11] + b[t-10] + b[t-9] + b[t-8] + b[t-7] + b[t-6] + b[t-5] + b[t-4] + b[t-3] + b[t-2] + b[t-1] + b[t])
                t-=40
            elif b[t] in allword and b[t-1] in allword and b[t-2] in allword and b[t-3] in allword and b[t-4] in allword and \
                    b[t-5] in allword and b[t-6] in allword and b[t-7] in allword and b[t-8] in allword and b[t-9] in \
                    allword and b[t-10] in allword and b[t-11] in allword and b[t-12] in allword and b[t-13] in allword and b[t-14] in allword and b[t-15] in allword and b[t-16] in allword and b[t-17] in allword and b[t-18] in allword and b[t-19] in allword and b[t-20] in allword and b[t-21] in allword and b[t-22] in allword and b[t-23] in allword and b[t-24] in allword and b[t-25] in allword and b[t-26] in allword and b[t-27] in allword and b[t-28] in allword and b[t-29] in allword and b[t-30] in allword and b[t-31] in allword and b[t-32] in allword and b[t-33] in allword and b[t-34] in allword and b[t-35] in allword and b[t-36] in allword and b[t-37] in allword and b[t-38] in allword and b[t-39] in allword:
                c.append(b[t-39] + b[t-38] + b[t-37] + b[t-36] + b[t-35] + b[t-34] + b[t-33] + b[t-32] + b[t-31] + b[t-30] + b[t-29] + b[t-28] + b[t-27] + b[t-26] + b[t-25] + b[t-24] + b[t-23] + b[t-22] + b[t-21] + b[t-20] + b[t-19] + b[t-18] + b[t-17] + b[t-16] + b[t-15] + b[t-14] + b[t-13] + b[t-12] + b[t-11] + b[t-10] + b[t-9] + b[t-8] + b[t-7] + b[t-6] + b[t-5] + b[t-4] + b[t-3] + b[t-2] + b[t-1] + b[t])
                t-=39
            elif b[t] in allword and b[t-1] in allword and b[t-2] in allword and b[t-3] in allword and b[t-4] in allword and \
                    b[t-5] in allword and b[t-6] in allword and b[t-7] in allword and b[t-8] in allword and b[t-9] in \
                    allword and b[t-10] in allword and b[t-11] in allword and b[t-12] in allword and b[t-13] in allword and b[t-14] in allword and b[t-15] in allword and b[t-16] in allword and b[t-17] in allword and b[t-18] in allword and b[t-19] in allword and b[t-20] in allword and b[t-21] in allword and b[t-22] in allword and b[t-23] in allword and b[t-24] in allword and b[t-25] in allword and b[t-26] in allword and b[t-27] in allword and b[t-28] in allword and b[t-29] in allword and b[t-30] in allword and b[t-31] in allword and b[t-32] in allword and b[t-33] in allword and b[t-34] in allword and b[t-35] in allword and b[t-36] in allword and b[t-37] in allword and b[t-38] in allword:
                c.append(b[t-38] + b[t-37] + b[t-36] + b[t-35] + b[t-34] + b[t-33] + b[t-32] + b[t-31] + b[t-30] + b[t-29] + b[t-28] + b[t-27] + b[t-26] + b[t-25] + b[t-24] + b[t-23] + b[t-22] + b[t-21] + b[t-20] + b[t-19] + b[t-18] + b[t-17] + b[t-16] + b[t-15] + b[t-14] + b[t-13] + b[t-12] + b[t-11] + b[t-10] + b[t-9] + b[t-8] + b[t-7] + b[t-6] + b[t-5] + b[t-4] + b[t-3] + b[t-2] + b[t-1] + b[t])
                t-=38
            elif b[t] in allword and b[t-1] in allword and b[t-2] in allword and b[t-3] in allword and b[t-4] in allword and \
                    b[t-5] in allword and b[t-6] in allword and b[t-7] in allword and b[t-8] in allword and b[t-9] in \
                    allword and b[t-10] in allword and b[t-11] in allword and b[t-12] in allword and b[t-13] in allword and b[t-14] in allword and b[t-15] in allword and b[t-16] in allword and b[t-17] in allword and b[t-18] in allword and b[t-19] in allword and b[t-20] in allword and b[t-21] in allword and b[t-22] in allword and b[t-23] in allword and b[t-24] in allword and b[t-25] in allword and b[t-26] in allword and b[t-27] in allword and b[t-28] in allword and b[t-29] in allword and b[t-30] in allword and b[t-31] in allword and b[t-32] in allword and b[t-33] in allword and b[t-34] in allword and b[t-35] in allword and b[t-36] in allword and b[t-37] in allword:
                c.append(b[t-37] + b[t-36] + b[t-35] + b[t-34] + b[t-33] + b[t-32] + b[t-31] + b[t-30] + b[t-29] + b[t-28] + b[t-27] + b[t-26] + b[t-25] + b[t-24] + b[t-23] + b[t-22] + b[t-21] + b[t-20] + b[t-19] + b[t-18] + b[t-17] + b[t-16] + b[t-15] + b[t-14] + b[t-13] + b[t-12] + b[t-11] + b[t-10] + b[t-9] + b[t-8] + b[t-7] + b[t-6] + b[t-5] + b[t-4] + b[t-3] + b[t-2] + b[t-1] + b[t])
                t-=37
            elif b[t] in allword and b[t-1] in allword and b[t-2] in allword and b[t-3] in allword and b[t-4] in allword and \
                    b[t-5] in allword and b[t-6] in allword and b[t-7] in allword and b[t-8] in allword and b[t-9] in \
                    allword and b[t-10] in allword and b[t-11] in allword and b[t-12] in allword and b[t-13] in allword and b[t-14] in allword and b[t-15] in allword and b[t-16] in allword and b[t-17] in allword and b[t-18] in allword and b[t-19] in allword and b[t-20] in allword and b[t-21] in allword and b[t-22] in allword and b[t-23] in allword and b[t-24] in allword and b[t-25] in allword and b[t-26] in allword and b[t-27] in allword and b[t-28] in allword and b[t-29] in allword and b[t-30] in allword and b[t-31] in allword and b[t-32] in allword and b[t-33] in allword and b[t-34] in allword and b[t-35] in allword and b[t-36] in allword:
                c.append(b[t-36] + b[t-35] + b[t-34] + b[t-33] + b[t-32] + b[t-31] + b[t-30] + b[t-29] + b[t-28] + b[t-27] + b[t-26] + b[t-25] + b[t-24] + b[t-23] + b[t-22] + b[t-21] + b[t-20] + b[t-19] + b[t-18] + b[t-17] + b[t-16] + b[t-15] + b[t-14] + b[t-13] + b[t-12] + b[t-11] + b[t-10] + b[t-9] + b[t-8] + b[t-7] + b[t-6] + b[t-5] + b[t-4] + b[t-3] + b[t-2] + b[t-1] + b[t])
                t-=36
            elif b[t] in allword and b[t-1] in allword and b[t-2] in allword and b[t-3] in allword and b[t-4] in allword and \
                    b[t-5] in allword and b[t-6] in allword and b[t-7] in allword and b[t-8] in allword and b[t-9] in \
                    allword and b[t-10] in allword and b[t-11] in allword and b[t-12] in allword and b[t-13] in allword and b[t-14] in allword and b[t-15] in allword and b[t-16] in allword and b[t-17] in allword and b[t-18] in allword and b[t-19] in allword and b[t-20] in allword and b[t-21] in allword and b[t-22] in allword and b[t-23] in allword and b[t-24] in allword and b[t-25] in allword and b[t-26] in allword and b[t-27] in allword and b[t-28] in allword and b[t-29] in allword and b[t-30] in allword and b[t-31] in allword and b[t-32] in allword and b[t-33] in allword and b[t-34] in allword and b[t-35] in allword:
                c.append(b[t-35] + b[t-34] + b[t-33] + b[t-32] + b[t-31] + b[t-30] + b[t-29] + b[t-28] + b[t-27] + b[t-26] + b[t-25] + b[t-24] + b[t-23] + b[t-22] + b[t-21] + b[t-20] + b[t-19] + b[t-18] + b[t-17] + b[t-16] + b[t-15] + b[t-14] + b[t-13] + b[t-12] + b[t-11] + b[t-10] + b[t-9] + b[t-8] + b[t-7] + b[t-6] + b[t-5] + b[t-4] + b[t-3] + b[t-2] + b[t-1] + b[t])
                t-=35
            elif b[t] in allword and b[t-1] in allword and b[t-2] in allword and b[t-3] in allword and b[t-4] in allword and \
                    b[t-5] in allword and b[t-6] in allword and b[t-7] in allword and b[t-8] in allword and b[t-9] in \
                    allword and b[t-10] in allword and b[t-11] in allword and b[t-12] in allword and b[t-13] in allword and b[t-14] in allword and b[t-15] in allword and b[t-16] in allword and b[t-17] in allword and b[t-18] in allword and b[t-19] in allword and b[t-20] in allword and b[t-21] in allword and b[t-22] in allword and b[t-23] in allword and b[t-24] in allword and b[t-25] in allword and b[t-26] in allword and b[t-27] in allword and b[t-28] in allword and b[t-29] in allword and b[t-30] in allword and b[t-31] in allword and b[t-32] in allword and b[t-33] in allword and b[t-34] in allword:
                c.append(b[t-34] + b[t-33] + b[t-32] + b[t-31] + b[t-30] + b[t-29] + b[t-28] + b[t-27] + b[t-26] + b[t-25] + b[t-24] + b[t-23] + b[t-22] + b[t-21] + b[t-20] + b[t-19] + b[t-18] + b[t-17] + b[t-16] + b[t-15] + b[t-14] + b[t-13] + b[t-12] + b[t-11] + b[t-10] + b[t-9] + b[t-8] + b[t-7] + b[t-6] + b[t-5] + b[t-4] + b[t-3] + b[t-2] + b[t-1] + b[t])
                t-=34
            elif b[t] in allword and b[t-1] in allword and b[t-2] in allword and b[t-3] in allword and b[t-4] in allword and \
                    b[t-5] in allword and b[t-6] in allword and b[t-7] in allword and b[t-8] in allword and b[t-9] in \
                    allword and b[t-10] in allword and b[t-11] in allword and b[t-12] in allword and b[t-13] in allword and b[t-14] in allword and b[t-15] in allword and b[t-16] in allword and b[t-17] in allword and b[t-18] in allword and b[t-19] in allword and b[t-20] in allword and b[t-21] in allword and b[t-22] in allword and b[t-23] in allword and b[t-24] in allword and b[t-25] in allword and b[t-26] in allword and b[t-27] in allword and b[t-28] in allword and b[t-29] in allword and b[t-30] in allword and b[t-31] in allword and b[t-32] in allword and b[t-33] in allword:
                c.append(b[t-33] + b[t-32] + b[t-31] + b[t-30] + b[t-29] + b[t-28] + b[t-27] + b[t-26] + b[t-25] + b[t-24] + b[t-23] + b[t-22] + b[t-21] + b[t-20] + b[t-19] + b[t-18] + b[t-17] + b[t-16] + b[t-15] + b[t-14] + b[t-13] + b[t-12] + b[t-11] + b[t-10] + b[t-9] + b[t-8] + b[t-7] + b[t-6] + b[t-5] + b[t-4] + b[t-3] + b[t-2] + b[t-1] + b[t])
                t-=33
            elif b[t] in allword and b[t-1] in allword and b[t-2] in allword and b[t-3] in allword and b[t-4] in allword and \
                    b[t-5] in allword and b[t-6] in allword and b[t-7] in allword and b[t-8] in allword and b[t-9] in \
                    allword and b[t-10] in allword and b[t-11] in allword and b[t-12] in allword and b[t-13] in allword and b[t-14] in allword and b[t-15] in allword and b[t-16] in allword and b[t-17] in allword and b[t-18] in allword and b[t-19] in allword and b[t-20] in allword and b[t-21] in allword and b[t-22] in allword and b[t-23] in allword and b[t-24] in allword and b[t-25] in allword and b[t-26] in allword and b[t-27] in allword and b[t-28] in allword and b[t-29] in allword and b[t-30] in allword and b[t-31] in allword and b[t-32] in allword:
                c.append(b[t-32] + b[t-31] + b[t-30] + b[t-29] + b[t-28] + b[t-27] + b[t-26] + b[t-25] + b[t-24] + b[t-23] + b[t-22] + b[t-21] + b[t-20] + b[t-19] + b[t-18] + b[t-17] + b[t-16] + b[t-15] + b[t-14] + b[t-13] + b[t-12] + b[t-11] + b[t-10] + b[t-9] + b[t-8] + b[t-7] + b[t-6] + b[t-5] + b[t-4] + b[t-3] + b[t-2] + b[t-1] + b[t])
                t-=32
            elif b[t] in allword and b[t-1] in allword and b[t-2] in allword and b[t-3] in allword and b[t-4] in allword and \
                    b[t-5] in allword and b[t-6] in allword and b[t-7] in allword and b[t-8] in allword and b[t-9] in \
                    allword and b[t-10] in allword and b[t-11] in allword and b[t-12] in allword and b[t-13] in allword and b[t-14] in allword and b[t-15] in allword and b[t-16] in allword and b[t-17] in allword and b[t-18] in allword and b[t-19] in allword and b[t-20] in allword and b[t-21] in allword and b[t-22] in allword and b[t-23] in allword and b[t-24] in allword and b[t-25] in allword and b[t-26] in allword and b[t-27] in allword and b[t-28] in allword and b[t-29] in allword and b[t-30] in allword and b[t-31] in allword:
                c.append(b[t-31] + b[t-30] + b[t-29] + b[t-28] + b[t-27] + b[t-26] + b[t-25] + b[t-24] + b[t-23] + b[t-22] + b[t-21] + b[t-20] + b[t-19] + b[t-18] + b[t-17] + b[t-16] + b[t-15] + b[t-14] + b[t-13] + b[t-12] + b[t-11] + b[t-10] + b[t-9] + b[t-8] + b[t-7] + b[t-6] + b[t-5] + b[t-4] + b[t-3] + b[t-2] + b[t-1] + b[t])
                t-=31
            elif b[t] in allword and b[t-1] in allword and b[t-2] in allword and b[t-3] in allword and b[t-4] in allword and \
                    b[t-5] in allword and b[t-6] in allword and b[t-7] in allword and b[t-8] in allword and b[t-9] in \
                    allword and b[t-10] in allword and b[t-11] in allword and b[t-12] in allword and b[t-13] in allword and b[t-14] in allword and b[t-15] in allword and b[t-16] in allword and b[t-17] in allword and b[t-18] in allword and b[t-19] in allword and b[t-20] in allword and b[t-21] in allword and b[t-22] in allword and b[t-23] in allword and b[t-24] in allword and b[t-25] in allword and b[t-26] in allword and b[t-27] in allword and b[t-28] in allword and b[t-29] in allword and b[t-30] in allword:
                c.append(b[t-30] + b[t-29] + b[t-28] + b[t-27] + b[t-26] + b[t-25] + b[t-24] + b[t-23] + b[t-22] + b[t-21] + b[t-20] + b[t-19] + b[t-18] + b[t-17] + b[t-16] + b[t-15] + b[t-14] + b[t-13] + b[t-12] + b[t-11] + b[t-10] + b[t-9] + b[t-8] + b[t-7] + b[t-6] + b[t-5] + b[t-4] + b[t-3] + b[t-2] + b[t-1] + b[t])
                t-=30
            elif b[t] in allword and b[t-1] in allword and b[t-2] in allword and b[t-3] in allword and b[t-4] in allword and \
                    b[t-5] in allword and b[t-6] in allword and b[t-7] in allword and b[t-8] in allword and b[t-9] in \
                    allword and b[t-10] in allword and b[t-11] in allword and b[t-12] in allword and b[t-13] in allword and b[t-14] in allword and b[t-15] in allword and b[t-16] in allword and b[t-17] in allword and b[t-18] in allword and b[t-19] in allword and b[t-20] in allword and b[t-21] in allword and b[t-22] in allword and b[t-23] in allword and b[t-24] in allword and b[t-25] in allword and b[t-26] in allword and b[t-27] in allword and b[t-28] in allword and b[t-29] in allword:
                c.append(b[t-29] + b[t-28] + b[t-27] + b[t-26] + b[t-25] + b[t-24] + b[t-23] + b[t-22] + b[t-21] + b[t-20] + b[t-19] + b[t-18] + b[t-17] + b[t-16] + b[t-15] + b[t-14] + b[t-13] + b[t-12] + b[t-11] + b[t-10] + b[t-9] + b[t-8] + b[t-7] + b[t-6] + b[t-5] + b[t-4] + b[t-3] + b[t-2] + b[t-1] + b[t])
                t-=29
            elif b[t] in allword and b[t-1] in allword and b[t-2] in allword and b[t-3] in allword and b[t-4] in allword and \
                    b[t-5] in allword and b[t-6] in allword and b[t-7] in allword and b[t-8] in allword and b[t-9] in \
                    allword and b[t-10] in allword and b[t-11] in allword and b[t-12] in allword and b[t-13] in allword and b[t-14] in allword and b[t-15] in allword and b[t-16] in allword and b[t-17] in allword and b[t-18] in allword and b[t-19] in allword and b[t-20] in allword and b[t-21] in allword and b[t-22] in allword and b[t-23] in allword and b[t-24] in allword and b[t-25] in allword and b[t-26] in allword and b[t-27] in allword and b[t-28] in allword:
                c.append(b[t-28] + b[t-27] + b[t-26] + b[t-25] + b[t-24] + b[t-23] + b[t-22] + b[t-21] + b[t-20] + b[t-19] + b[t-18] + b[t-17] + b[t-16] + b[t-15] + b[t-14] + b[t-13] + b[t-12] + b[t-11] + b[t-10] + b[t-9] + b[t-8] + b[t-7] + b[t-6] + b[t-5] + b[t-4] + b[t-3] + b[t-2] + b[t-1] + b[t])
                t-=28
            elif b[t] in allword and b[t-1] in allword and b[t-2] in allword and b[t-3] in allword and b[t-4] in allword and \
                    b[t-5] in allword and b[t-6] in allword and b[t-7] in allword and b[t-8] in allword and b[t-9] in \
                    allword and b[t-10] in allword and b[t-11] in allword and b[t-12] in allword and b[t-13] in allword and b[t-14] in allword and b[t-15] in allword and b[t-16] in allword and b[t-17] in allword and b[t-18] in allword and b[t-19] in allword and b[t-20] in allword and b[t-21] in allword and b[t-22] in allword and b[t-23] in allword and b[t-24] in allword and b[t-25] in allword and b[t-26] in allword and b[t-27] in allword:
                c.append(b[t-27] + b[t-26] + b[t-25] + b[t-24] + b[t-23] + b[t-22] + b[t-21] + b[t-20] + b[t-19] + b[t-18] + b[t-17] + b[t-16] + b[t-15] + b[t-14] + b[t-13] + b[t-12] + b[t-11] + b[t-10] + b[t-9] + b[t-8] + b[t-7] + b[t-6] + b[t-5] + b[t-4] + b[t-3] + b[t-2] + b[t-1] + b[t])
                t-=27
            elif b[t] in allword and b[t-1] in allword and b[t-2] in allword and b[t-3] in allword and b[t-4] in allword and \
                    b[t-5] in allword and b[t-6] in allword and b[t-7] in allword and b[t-8] in allword and b[t-9] in \
                    allword and b[t-10] in allword and b[t-11] in allword and b[t-12] in allword and b[t-13] in allword and b[t-14] in allword and b[t-15] in allword and b[t-16] in allword and b[t-17] in allword and b[t-18] in allword and b[t-19] in allword and b[t-20] in allword and b[t-21] in allword and b[t-22] in allword and b[t-23] in allword and b[t-24] in allword and b[t-25] in allword and b[t-26] in allword:
                c.append(b[t-26] + b[t-25] + b[t-24] + b[t-23] + b[t-22] + b[t-21] + b[t-20] + b[t-19] + b[t-18] + b[t-17] + b[t-16] + b[t-15] + b[t-14] + b[t-13] + b[t-12] + b[t-11] + b[t-10] + b[t-9] + b[t-8] + b[t-7] + b[t-6] + b[t-5] + b[t-4] + b[t-3] + b[t-2] + b[t-1] + b[t])
                t-=26
            elif b[t] in allword and b[t-1] in allword and b[t-2] in allword and b[t-3] in allword and b[t-4] in allword and \
                    b[t-5] in allword and b[t-6] in allword and b[t-7] in allword and b[t-8] in allword and b[t-9] in \
                    allword and b[t-10] in allword and b[t-11] in allword and b[t-12] in allword and b[t-13] in allword and b[t-14] in allword and b[t-15] in allword and b[t-16] in allword and b[t-17] in allword and b[t-18] in allword and b[t-19] in allword and b[t-20] in allword and b[t-21] in allword and b[t-22] in allword and b[t-23] in allword and b[t-24] in allword and b[t-25] in allword:
                c.append(b[t-25] + b[t-24] + b[t-23] + b[t-22] + b[t-21] + b[t-20] + b[t-19] + b[t-18] + b[t-17] + b[t-16] + b[t-15] + b[t-14] + b[t-13] + b[t-12] + b[t-11] + b[t-10] + b[t-9] + b[t-8] + b[t-7] + b[t-6] + b[t-5] + b[t-4] + b[t-3] + b[t-2] + b[t-1] + b[t])
                t-=25
            elif b[t] in allword and b[t-1] in allword and b[t-2] in allword and b[t-3] in allword and b[t-4] in allword and \
                    b[t-5] in allword and b[t-6] in allword and b[t-7] in allword and b[t-8] in allword and b[t-9] in \
                    allword and b[t-10] in allword and b[t-11] in allword and b[t-12] in allword and b[t-13] in allword and b[t-14] in allword and b[t-15] in allword and b[t-16] in allword and b[t-17] in allword and b[t-18] in allword and b[t-19] in allword and b[t-20] in allword and b[t-21] in allword and b[t-22] in allword and b[t-23] in allword and b[t-24] in allword:
                c.append(b[t-24] + b[t-23] + b[t-22] + b[t-21] + b[t-20] + b[t-19] + b[t-18] + b[t-17] + b[t-16] + b[t-15] + b[t-14] + b[t-13] + b[t-12] + b[t-11] + b[t-10] + b[t-9] + b[t-8] + b[t-7] + b[t-6] + b[t-5] + b[t-4] + b[t-3] + b[t-2] + b[t-1] + b[t])
                t-=24
            elif b[t] in allword and b[t-1] in allword and b[t-2] in allword and b[t-3] in allword and b[t-4] in allword and \
                    b[t-5] in allword and b[t-6] in allword and b[t-7] in allword and b[t-8] in allword and b[t-9] in \
                    allword and b[t-10] in allword and b[t-11] in allword and b[t-12] in allword and b[t-13] in allword and b[t-14] in allword and b[t-15] in allword and b[t-16] in allword and b[t-17] in allword and b[t-18] in allword and b[t-19] in allword and b[t-20] in allword and b[t-21] in allword and b[t-22] in allword and b[t-23] in allword:
                c.append(b[t-23] + b[t-22] + b[t-21] + b[t-20] + b[t-19] + b[t-18] + b[t-17] + b[t-16] + b[t-15] +b[t-14] + b[t-13] + b[t-12] + b[t-11] + b[t-10] + b[t-9] + b[t-8] + b[t-7] + b[t-6] + b[t-5] + b[t-4] + b[t-3] + b[t-2] + b[t-1] + b[t])
                t-=23
            elif b[t] in allword and b[t-1] in allword and b[t-2] in allword and b[t-3] in allword and b[t-4] in allword and \
                    b[t-5] in allword and b[t-6] in allword and b[t-7] in allword and b[t-8] in allword and b[t-9] in \
                    allword and b[t-10] in allword and b[t-11] in allword and b[t-12] in allword and b[t-13] in allword and b[t-14] in allword and b[t-15] in allword and b[t-16] in allword and b[t-17] in allword and b[t-18] in allword and b[t-19] in allword and b[t-20] in allword and b[t-21] in allword and b[t-22] in allword:
                c.append(b[t-22] + b[t-21] + b[t-20] + b[t-19] + b[t-18] + b[t-17] + b[t-16] + b[t-15] + b[t-14] + b[t-13] + b[t-12] + b[t-11] + b[t-10] + b[t-9] + b[t-8] + b[t-7] + b[t-6] + b[t-5] + b[t-4] + b[t-3] + b[t-2] + b[t-1] + b[t])
                t-=22
            elif b[t] in allword and b[t-1] in allword and b[t-2] in allword and b[t-3] in allword and b[t-4] in allword and \
                    b[t-5] in allword and b[t-6] in allword and b[t-7] in allword and b[t-8] in allword and b[t-9] in \
                    allword and b[t-10] in allword and b[t-11] in allword and b[t-12] in allword and b[t-13] in allword and b[t-14] in allword and b[t-15] in allword and b[t-16] in allword and b[t-17] in allword and b[t-18] in allword and b[t-19] in allword and b[t-20] in allword and b[t-21] in allword:
                c.append(b[t-21] + b[t-20] + b[t-19] + b[t-18] + b[t-17] + b[t-16] + b[t-15] + b[t-14] + b[t-13] + b[t-12] + b[t-11] + b[t-10] + b[t-9] + b[t-8] + b[t-7] + b[t-6] + b[t-5] + b[t-4] + b[t-3] + b[t-2] + b[t-1] + b[t])
                t-=21
            elif b[t] in allword and b[t-1] in allword and b[t-2] in allword and b[t-3] in allword and b[t-4] in allword and \
                    b[t-5] in allword and b[t-6] in allword and b[t-7] in allword and b[t-8] in allword and b[t-9] in \
                    allword and b[t-10] in allword and b[t-11] in allword and b[t-12] in allword and b[t-13] in allword and b[t-14] in allword and b[t-15] in allword and b[t-16] in allword and b[t-17] in allword and b[t-18] in allword and b[t-19] in allword and b[t-20] in allword:
                c.append(b[t-20] + b[t-19] + b[t-18] + b[t-17] + b[t-16] + b[t-15] + b[t-14] + b[t-13] + b[t-12] + b[t-11] + b[t-10] + b[t-9] + b[t-8] + b[t-7] + b[t-6] + b[t-5] + b[t-4] + b[t-3] + b[t-2] + b[t-1] + b[t])
                t-=20
            elif b[t] in allword and b[t-1] in allword and b[t-2] in allword and b[t-3] in allword and b[t-4] in allword and \
                    b[t-5] in allword and b[t-6] in allword and b[t-7] in allword and b[t-8] in allword and b[t-9] in \
                    allword and b[t-10] in allword and b[t-11] in allword and b[t-12] in allword and b[t-13] in allword and b[t-14] in allword and b[t-15] in allword and b[t-16] in allword and b[t-17] in allword and b[t-18] in allword and b[t-19] in allword:
                c.append(b[t-19] + b[t-18] + b[t-17] + b[t-16] + b[t-15] + b[t-14] + b[t-13] + b[t-12] + b[t-11] + b[t-10] + b[t-9] + b[t-8] + b[t-7] + b[t-6] + b[t-5] + b[t-4] + b[t-3] + b[t-2] + b[t-1] + b[t])
                t-=19
            elif b[t] in allword and b[t-1] in allword and b[t-2] in allword and b[t-3] in allword and b[t-4] in allword and \
                    b[t-5] in allword and b[t-6] in allword and b[t-7] in allword and b[t-8] in allword and b[t-9] in \
                    allword and b[t-10] in allword and b[t-11] in allword and b[t-12] in allword and b[t-13] in allword and b[t-14] in allword and b[t-15] in allword and b[t-16] in allword and b[t-17] in allword and b[t-18] in allword:
                c.append(b[t-18] + b[t-17] + b[t-16] + b[t-15] + b[t-14] + b[t-13] + b[t-12] + b[t-11] + b[t-10] + b[t-9] + b[t-8] + b[t-7] + b[t-6] + b[t-5] + b[t-4] + b[t-3] + b[t-2] + b[t-1] + b[t])
                t-=18
            elif b[t] in allword and b[t-1] in allword and b[t-2] in allword and b[t-3] in allword and b[t-4] in allword and \
                    b[t-5] in allword and b[t-6] in allword and b[t-7] in allword and b[t-8] in allword and b[t-9] in \
                    allword and b[t-10] in allword and b[t-11] in allword and b[t-12] in allword and b[t-13] in allword and b[t-14] in allword and b[t-15] in allword and b[t-16] in allword and b[t-17] in allword:
                c.append(b[t-17] + b[t-16] + b[t-15] + b[t-14] + b[t-13] + b[t-12] + b[t-11] + b[t-10] + b[t-9] + b[t-8] + b[t-7] + b[t-6] + b[t-5] + b[t-4] + b[t-3] + b[t-2] + b[t-1] + b[t])
                t-=17
            elif b[t] in allword and b[t-1] in allword and b[t-2] in allword and b[t-3] in allword and b[t-4] in allword and \
                    b[t-5] in allword and b[t-6] in allword and b[t-7] in allword and b[t-8] in allword and b[t-9] in \
                    allword and b[t-10] in allword and b[t-11] in allword and b[t-12] in allword and b[t-13] in allword and b[t-14] in allword and b[t-15] in allword and b[t-16] in allword:
                c.append(b[t-16] + b[t-15] + b[t-14] + b[t-13] + b[t-12] + b[t-11] + b[t-10] + b[t-9] + b[t-8] + b[t-7] + b[t-6] + b[t-5] + b[t-4] + b[t-3] + b[t-2] + b[t-1] + b[t])
                t-=16
            elif b[t] in allword and b[t-1] in allword and b[t-2] in allword and b[t-3] in allword and b[t-4] in allword and \
                    b[t-5] in allword and b[t-6] in allword and b[t-7] in allword and b[t-8] in allword and b[t-9] in \
                    allword and b[t-10] in allword and b[t-11] in allword and b[t-12] in allword and b[t-13] in allword and b[t-14] in allword and b[t-15] in allword:
                c.append(b[t-15] + b[t-14] + b[t-13] + b[t-12] + b[t-11] + b[t-10] + b[t-9] + b[t-8] + b[t-7] + b[t-6] + b[t-5] + b[t-4] + b[t-3] + b[t-2] + b[t-1] + b[t])
                t-=15
            elif b[t] in allword and b[t-1] in allword and b[t-2] in allword and b[t-3] in allword and b[t-4] in allword and \
                    b[t-5] in allword and b[t-6] in allword and b[t-7] in allword and b[t-8] in allword and b[t-9] in \
                    allword and b[t-10] in allword and b[t-11] in allword and b[t-12] in allword and b[t-13] in allword and b[t-14] in allword:
                c.append(b[t-14] + b[t-13] + b[t-12] + b[t-11] + b[t-10] + b[t-9] + b[t-8] + b[t-7] + b[t-6] + b[t-5] + b[t-4] + b[t-3] + b[t-2] + b[t-1] + b[t])
                t-=14
            elif b[t] in allword and b[t-1] in allword and b[t-2] in allword and b[t-3] in allword and b[t-4] in allword and \
                    b[t-5] in allword and b[t-6] in allword and b[t-7] in allword and b[t-8] in allword and b[t-9] in \
                    allword and b[t-10] in allword and b[t-11] in allword and b[t-12] in allword and b[t-13] in allword:
                c.append(b[t-13] + b[t-12] + b[t-11] + b[t-10] + b[t-9] + b[t-8] + b[t-7] + b[t-6] + b[t-5] + b[t-4] + b[t-3] + b[t-2] + b[t-1] + b[t])
                t-=13
            elif b[t] in allword and b[t-1] in allword and b[t-2] in allword and b[t-3] in allword and b[t-4] in allword and \
                    b[t-5] in allword and b[t-6] in allword and b[t-7] in allword and b[t-8] in allword and b[t-9] in \
                    allword and b[t-10] in allword and b[t-11] in allword and b[t-12] in allword:
                c.append(b[t-12] + b[t-11] + b[t-10] + b[t-9] + b[t-8] + b[t-7] + b[t-6] + b[t-5] + b[t-4] + b[t-3] + b[t-2] + b[t-1] + b[t])
                t-=12
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[
                     t - 8] in allword and b[t - 9] in allword and b[t - 10] in allword and b[t - 11] in allword:
                c.append(
            b[t - 11] + b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] +
            b[t - 1] + b[t])
                t-=11
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[
                 t - 8] in allword and b[t - 9] in allword and b[t - 10] in allword:
                c.append(
                b[t - 10] + b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] +
                b[t])
                t -= 10
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[
                     t - 8] in allword and b[t - 9] in allword:
                c.append(b[t - 9] + b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
                t -= 9
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword and b[
                     t - 8] in allword:
                c.append(b[t - 8] + b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
                t -= 8
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and b[t - 5] in allword and b[t - 6] in allword and b[t - 7] in allword:
                c.append(b[t - 7] + b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
                t -= 7
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and b[t - 5] in allword and b[t - 6] in allword:
                c.append(b[t - 6] + b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
                t -= 6
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword and b[t - 5] in allword:
                c.append(b[t - 5] + b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
                t -= 5
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword and b[
                t - 4] in allword:
                c.append(b[t - 4] + b[t - 3] + b[t - 2] + b[t - 1] + b[t])
                t -= 4
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword and b[t - 3] in allword:
                c.append(b[t - 3] + b[t - 2] + b[t - 1] + b[t])
                t -= 3
            elif b[t] in allword and b[t - 1] in allword and b[t - 2] in allword:
                c.append(b[t - 2] + b[t - 1] + b[t])
                t -= 2
            elif b[t] in allword and b[t - 1] in allword:
                c.append(b[t - 1] + b[t])
                t -= 1
            elif b[t] in allword:
                c.append(b[t])
            t-=1

        return sortreversed(c)



    def groupsound(q):
        r = len(q)-1
        w = []
        while r>=0 and r < len(q):
            if q[r] in keysA and q[r-1] in keysC:
                w.append(q[r-1]+q[r])
                r -= 2
            elif q[r] in keysE and q[r-1] in ['i','k']:
                w.append(q[r-2]+q[r-1]+q[r])
                r -= 3
            elif q[r] in keysE and q[r-1] in keysA:
                w.append(q[r-1]+q[r])
                r -= 2
            elif q[r] in keysD and q[r-1] in keysA:
                w.append(q[r-1]+q[r])
                r -= 2
            elif q[r] in keysB and q[r-1] in keysA:
                w.append(q[r-1]+q[r])
                r -= 2
            else:
                w.append(q[r])
                r -= 1

        return sortreversed(w)

    def convertfunction(x):
        u = []
        for y in x:
            j = list(Alphabetic.keys())[list(Alphabetic.values()).index(y)]
            u.append(j)
        return u

    def convertcommand(x):
        j = []
        for i in range(0, len(x)):
            a = convertfunction(x[i])
            j.append(a)

        return j

    def listtostring(s):
        str1 = ""
        for ele in s:
            str1 += ele
        return str1


    in_word = []
    def tostring_inlist(in_word):
        x = len(in_word)
        word = []
        for item in range(x):
            output = ""
            for w in in_word[item]:
                output += w
            word.append(output)
        return word

    convert = convertcommand(bhrammajala)
    group = groupword(lstostring(convert))
    form_word = converttovalues(group)
    result = tostring_inlist(form_word)

    return result




if __name__ == '__main__':
    from tipitaka_org import tipitaka
    x = tipitaka

    form_word = cutword(x)

    import sys
    result = []
    for x in form_word:
        result.append(x)

    sys.stdout = open(r"output.py","w",encoding='utf-8')
    b = [x for x in result]
    print(b)
    sys.stdout.close()
