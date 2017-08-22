import glob
import os
import re
import math


class BagOfWords(object):
    def __init__(self, f, filename):
        self.d = {}
        self.f = f
        self.filename = filename

    def insertWords(self):
        for line in self.f:
            for word in re.findall(r'\w+', line):
                if word in self.d:
                    self.d[word.lower()] += 1
                else:
                    self.d[word.lower()] = 1

    def __str__(self):
        return str(self.filename)

    def mod(self):
        prod = 0
        for j in self.d:
            prod += (self.d[j])**2
        return math.sqrt(prod)

    def compare(self, other):
        dotprod = 0
        for i in self.d.keys():
            try:
                dotprod = dotprod + (self.d[i]*other.d[i])
            except KeyError:
                continue
        return dotprod/(self.mod()*other.mod()) * 100

path = str(input())
assert os.path.exists(path)
l = []
for filename in glob.glob(os.path.join(path, '*.txt')):
    f = open(filename, "r")
    f1 = BagOfWords(f, filename)
    l.append(f1)
    f1.insertWords()
k = [[] for i in range(len(l))]
for i in range(0, len(l)):
    for j in range(0, len(l)):
        k[i].append(l[i].compare(l[j]))
for i in range(len(k)):
    print(k[i])
