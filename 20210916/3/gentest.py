import random
randomlist = random.sample(range(0, 100), 10)
randomlist[random.randint(0,9)] = int(input())
f = open('./tests/1.in', 'w')
f.write(str(randomlist))
f.close()
