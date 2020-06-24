import math as mt
import pandas as pd

class   UjiF :
    def __init__(self,urutanatribut,rsquare,features,labels,fsig):
        self.__urutanatribut = urutanatribut
        self.__rsquare = rsquare
        self.__feature = features
        self.__labels = labels
        self.__fsig = fsig
        self.fhitungg = []
        self.ftabell = []
        self.det1 = []
        self.det2 = []
        self.ftables = []
        self.__hasil = []

    def fhitung(self):
        i =0
        n = len(self.__feature)
        k = 1
        while i<len(self.__feature.columns):
            k += 1
            self.fhitungg.append((self.__rsquare[0][i] *(n-k-1)) / (k*(1-self.__rsquare[0][i])) )
            i+=1

        ##print('ini fhitung',self.fhitungg)

        ##print('inipanjang', len(self.__feature.columns) )
        ##print('inirsquare',self.__rsquare[0][1])

    def ftable(self):
        k = 1
        n = len(self.__feature)
        i =0
        while i < len(self.__feature.columns):
            k+=1
            self.det1.append(k - 1)
            self.det2.append(n - k)
            i+=1
        ##print('det1', self.det1, 'det2', self.det2)
        ##print('ini belum',self.det2[1])
        #print('ini sudah', self.det2[1] = 21)
        #self.det2[1] = 21

        i = 0
        while i< len(self.__feature.columns):
            if 15 < self.det2[i] <= 20:
                self.det2[i] = 18
            elif 20 < self.det2[i] <= 24:
                self.det2[i] = 19
            elif 24 < self.det2[i] <= 30:
                self.det2[i] = 20
            elif 30 < self.det2[i] <= 40:
                self.det2[i] = 21
            elif 40 < self.det2[i] <= 60:
                self.det2[i] = 22
            elif 60 < self.det2[i] <= 120:
                self.det2[i] = 23
            elif self.det2[i] >120:
                self.det2[i] = 24
            i+=1

        while i< len(self.__feature.columns):
            if 25 < self.det1[i] <= 30:
                self.det2[i] = 26
            elif 30 < self.det1[i] <= 40:
                self.det2[i] = 27
            elif 40 < self.det1[i] <= 50:
                self.det2[i] = 28
            elif 50 < self.det1[i] <= 60:
                self.det2[i] = 29
            elif 60 < self.det1[i] <= 100:
                self.det2[i] = 30
            elif 100 < self.det1[i] <= 120:
                self.det2[i] = 31
            elif self.det1[i] >120:
                self.det2[i] = 32
            i+=1


        ##print('det1',self.det1,'det2',self.det2)
        ##print('ini det1 baris 1',self.det1[1],'ini det1 baris 2',self.det2[1])
        ##print('ininah',self.__fsig.iloc[1,1])

        i=0
        while i<len(self.__feature.columns):
            self.ftables.append(self.__fsig.iloc[self.det1[i],self.det1[i]])
            i+=1
        ##print(self.fhitungg)
        ##print(self.ftables)

        #self.ftables.append(self.__fsig.loc(self.det1[1]),self.det2[1])
        i=0
        while i<len(self.__feature.columns):
            if self.fhitungg [i] > self.ftables [i]:
                ##print(self.fhitungg[i],self.ftables[i])
                self.__hasil.append(self.__urutanatribut[i])

            i+=1

        #print('ini apa ya',self.__hasil)
        return self.__hasil