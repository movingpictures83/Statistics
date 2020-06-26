import sys
import numpy
#import PyPluMA


class StatisticsPlugin:
   def input(self, filename):
      self.myfile = filename

   def run(self):
      filestuff = open(self.myfile, 'r')
      firstline = filestuff.readline()
      self.bacteria = firstline.split(',')
      if (self.bacteria.count('\"\"') != 0):
         self.bacteria.remove('\"\"')
      self.n = len(self.bacteria)
      self.ADJ = []
      self.m = 0
      for line in filestuff:
         contents = line.split(',')
         self.ADJ.append([])
         for j in range(self.n):
            value = float(contents[j+1])
            self.ADJ[self.m].append(value)
         self.m += 1

   def output(self, filename):
      means = []
      for j in range(self.n):
         vec = []
         for i in range(self.m):
            vec.append(round(self.ADJ[i][j]*100, 2))
         means.append((numpy.mean(vec), numpy.std(vec), self.bacteria[j], vec))

      means.sort()
      means.reverse()
      print("OTU\tMean\tStd Dev\tAbundances")
      for element in means:
         if (element[0] >= 0.5):
           print(element[2], "\t", round(element[0], 2), "%\t", round(element[1], 2), "%\t", element[3]) 


