import difflib
import ast
import sys
import webbrowser
import os

import string

def calculate_dst(a1, a2):
    ch = ['(', ',', '#', "'", ')']
    st1 = plagiat_checker(a1, ch)
    st2 = plagiat_checker(a2, ch)
    import textdistance
    dst = textdistance.damerau_levenshtein.normalized_distance(st1, st2)
    print("distance =", dst)
    return dst

def get_txt(file):
    f = open(file)
    txt = f.read()
    f.close()
    return txt

def diff(arg1, arg2):
    return difflib.HtmlDiff().make_file(arg1, arg2)

def replace_ch(st):
    str1 = '##'
    str2 = '#'
    while True:
        if st != st.replace(str1, str2):
            break
        st = st.replace(str1, str2)
    for ch in ["'#'", "''"]:
        st = st.replace(ch, '')
    ch = '#)'
    st = st.replace(ch, ')')
    ch = '#,'
    st = st.replace(ch, ',')
    return st

def time_wait():
    import time
    time.sleep(1)

def check(ch, m):
    if ch in m:
        return True
    return False

def plagiat_checker(text_, lst):
    txt = ast.unparse(ast.parse(text_))
    st = ast.dump(ast.parse(txt), annotate_fields=False)[8:-6]

    for ch in string.ascii_uppercase:
        st = st.replace(ch, '#')

    for s in st:
        if s not in lst:
            st = st.replace(s, '')

    return replace_ch(st)

txt1, txt2 = get_txt(sys.argv[1]), get_txt(sys.argv[2])
dst = calculate_dst(txt1, txt2)
str2 = txt2.split('\n')
str1 = txt1.split('\n')
if dst <= 0.1:
    txt = diff(str1, str2)
    f = open('plagiat.html', 'w')
    f.write(txt)
    f.close()
    webbrowser.open('file://' + os.getcwd() + '/plagiat.html')
    time_wait()
    os.remove('plagiat.html')
