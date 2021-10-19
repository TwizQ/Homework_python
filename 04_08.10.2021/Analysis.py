import string
import random

def rand_strok(num):
    new_str = ''
    for i in range(num):
        new_str += random.choice(string.ascii_letters)
    return new_str

def rand_list_strok(num1, num2):
    llist = [''] * num1
    for i in range(num1):
        for ii in range(num2):
            llist[i] += random.choice(string.ascii_letters)
    return llist

def str_list(spisok):
    bb = 0; ll = 0; oo = 0
    for i in range(len(spisok)):
        b = 0; l = 0
        for ii in range(len(spisok[i])):
            if spisok[i][ii].isupper():
                b +=1
            else:
                l += 1
        if b > l:
            bb +=1
        elif b < l:
            ll += 1
        else:
            oo += 1
    Capital_letters = bb / (bb + ll + oo) * 100
    Lowercase_letters = ll / (bb + ll + oo) * 100
    Equality_of_letters = oo / (bb + ll + oo) * 100
    print(spisok)
    print('Процент слов, где заглавных букв больше: ', Capital_letters, '%', sep = '')
    print('Процент слов, где строчных букв больше: ', Lowercase_letters, '%', sep = '')
    print('Процент слов, где их одинаково: ', Equality_of_letters, '%', sep = '')

rand_strok = rand_strok(10)
str(rand_strok)
rand_list_strok = rand_list_strok(17, 10)
str_list(rand_list_strok)