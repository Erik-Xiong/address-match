from __future__ import unicode_literals
from FuzzyMatch import fuzz
from collections import Counter
import csv
import numpy as np

class AddrMatcher:

  def __init__(self, path):
    self.data= []
    with open(path, encoding='utf-8') as csvfile:
      addrReader = csv.reader(csvfile, delimiter=';')
      for row in addrReader:
        self.data.append((row[0], np.int(row[1])))

  def predict(self, addr):
    similarAddrs = {}
    for sample, zd in self.data:
      if fuzz.UWRatio(addr, sample) >= 80:
        similarAddrs[sample] = zd
    print(similarAddrs)
    print(Counter(similarAddrs.values()))


a = AddrMatcher('addr_to_zd.csv')
result = a.predict("北京海淀区五环到六环之间海淀区西三旗桥东建材城西二里小区2号楼1单元201室")
