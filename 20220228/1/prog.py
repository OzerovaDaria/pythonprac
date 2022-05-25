
import textdistance as td

def dist(s1, s2):
    return td.levenshtein(s1, s2)

a, b = input(), input()
res = dist(a, b)
