import string
f = open('en-ru.txt')
dic = f.read().split('\n')
a = {}
for i in dic:
    tmp = i.split('\t-\t')
    a[tmp[0]] = tmp[len(tmp)-1]
f = open('input.txt')
text = f.read().split()
for i in range(len(text)):
    k = ''
    for j in text[i]:
        if j not in string.punctuation:
            k += j
        else:
            k += ' ' + j
    text[i] = k
k = ''
for i in text:
    k += i + ' '
k = k.split()
text = k
for i in text:
    if i in a:
        text[text.index(i)] = a[i]
print(*text)