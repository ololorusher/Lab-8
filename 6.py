dict = dict()
sl = open('en-ru6.txt')
another_dic = open('output.txt', 'w')
s = sl.readline().rstrip()
while len(s) > 0:
    trans, russkiy = list(s.split('\t-\t'))
    if ',' in russkiy:
        for i in russkiy.split(','):
            i = i.lstrip()
            if i in dict:
                dict[i] = dict[i]+', '+trans
            else:
                dict[i] = trans
    else:
        if russkiy in dict:
            dict[russkiy] = dict[russkiy]+', '+trans
        else:
            dict[russkiy] = trans

    s = sl.readline().rstrip()

key_sort = sorted(dict.keys())
for i in key_sort:
    print('\t-\t'.join((i, dict[i])), file=another_dic)