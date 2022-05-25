import multiprocessing as mp
import textdistance as td

def dist(s1, s2, s3):
    if s3 == 'L':
        return td.levenshtein(s1, s2)
    elif s3 == 'D':
        return td.damerau_levenshtein(s1, s2)
    else:
        return -1
    

a, b, c = input(), input(), input()
pool = mp.Pool(1)
pr = pool.apply_async(dist, (a, b, c))
#res = pr.get()
try:
    res = pr.get(1000)
except:
    res = -1
