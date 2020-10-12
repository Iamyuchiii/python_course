# exam question

trans_dic = {
'long': ['lang'],
'tall': ['lang', 'groot', 'hoog'],
'big': ['groot'],
'large': ['groot'],
'short': ['kort', 'klein'],
'small': ['klein']
}

def add_translation (d, source, translation):
    if source not in d:
        d[source] = [translation]
    else:
        d[source] += [translation]

def invert_dictionary(dic):
    invert_dic = {}
    for key, value in trans_dic.items():
        for e in value:
            add_translation(invert_dic, e, key)
    return invert_dic

print (invert_dictionary(trans_dic))